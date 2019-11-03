<h1>Smart contract in stages</h1>

Let's look at the three Python scripts in the `contract_in_stages` directory in the Python API.

To run the code in this demo, you will need a running node. Details are <a href="../../getting-started/run-a-node/" target=_blank>here</a>.

Details of the Python API are <a href="../../getting-started/python-api-install/" target=_blank>here</a>.

## Stage 1

The first script `01_create_private_key.py` creates an `Entity` object and inserts the private key from the `private.key` file in the same directory.

Once this is done, the script gives the `Entity` 10000 tokens.

``` python
def main():
    print('Creating private key...')

    # create our first private key pair
    entity1 = Entity()

    # save the private key to disk
    with open('private.key', 'w') as private_key_file:
        entity1.dump(private_key_file)

    print('Creating private key...complete')

    # build the ledger API
    api = LedgerApi('127.0.0.1', 8100)

    print('Creating initial balance...')

    # create wealth so that we have the funds to be able to create contracts on the network
    api.sync(api.tokens.wealth(entity1, 10000))

    print('Creating initial balance...complete')

```

## Stage 2

In the `02_create_contract.py` file, we embed the `etch` smart contract code into the script as a string.

We have an `init()` function which receives an `Address` object and sets its balance to 1000000 tokens in a `State` variable.

The `transfer()` function grabs or creates the `State` objects from two `Address` objects.

After a check to make sure there are enough funds in the from_account, the `from_account` transfers the `amount` to the `to_account`.

The `query()` function allows you to query the balance of an `Address` on the ledger via a `State` construct.

``` c++
@init
function setup(owner : Address)
  var owner_balance = State<UInt64>(owner);
  owner_balance.set(1000000u64);
endfunction

@action
function transfer(from: Address, to: Address, amount: UInt64)

  // define the accounts
  var from_account = State<UInt64>(from);
  var to_account = State<UInt64>(to); // if new sets to 0u

  // Check if the sender has enough balance to proceed
  if (from_account.get() >= amount)

    // update the account balances
    from_account.set(from_account.get() - amount);
    to_account.set(to_account.get(0u64) + amount);
  endif

endfunction

@query
function balance(address: Address) : UInt64
    var account = State<UInt64>(address);
    return account.get(0u64);
endfunction
```

The Python script loads the private key created in the first step, connects to the running ledger node, and deploys the contract to the ledger paying 2000 tokens to do so and designating `entity1` as the owner of the contract.

``` python
def main():

    print('Loading private key...')

    # load up the previously created private key
    with open('private.key', 'r') as private_key_file:
        entity1 = Entity.load(private_key_file)

    print('Loading private key...complete')

    # build the ledger API
    api = LedgerApi('127.0.0.1', 8100)

    # create the smart contract
    contract = SmartContract(CONTRACT_TEXT)

    print('Deploying contract...')

    # deploy the contract to the network
    api.sync(api.contracts.create(entity1, contract, 2000))

    print('Deploying contract...complete')

    # save the contract to the disk
    with open('sample.contract', 'w') as contract_file:
        contract.dump(contract_file)
```

## Stage 3

In `03_transfer.py` we load up the demo private key and the smart contract file. 

!!! note
    Remember, the smart contract is now on the ledger and can be referenced with the correct hash.

 We then perform a transfer using the contract code between the owner and a new user we create as `entity2`.

``` python
def main():
    # load up the previously created private key
    with open('private.key', 'r') as private_key_file:
        entity1 = Entity.load(private_key_file)

    # load up the deployed contract
    with open('sample.contract', 'r') as contract_file:
        contract = SmartContract.load(contract_file)

    # for the purposes of this example create a second private key pair to transfer funds to
    entity2 = Entity()

    # build the ledger API
    api = LedgerApi('127.0.0.1', 8100)

    # print the current status of all the tokens
    print('-- BEFORE --')
    print_address_balances(api, contract, [entity1, entity2])

    # transfer from one to the other using our newly deployed contract
    tok_transfer_amount = 200
    fet_tx_fee = 40
    api.sync(contract.action(api, 'transfer', fet_tx_fee, [entity1], Address(entity1), Address(entity2),
                             tok_transfer_amount))

    print('-- AFTER --')
    print_address_balances(api, contract, [entity1, entity2])

```
You should see a result like this:

``` bash
-- BEFORE --
Address0: 8540   bFET 1000000    TOK
Address1: 0      bFET 0          TOK

-- AFTER --
Address0: 8508   bFET 999800     TOK
Address1: 0      bFET 200        TOK

```

<br/>