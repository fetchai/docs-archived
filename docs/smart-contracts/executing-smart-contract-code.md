<h1>Executing smart contract code</h1>

## Locally

To run smart contract code on your local machine, first download, build, and run a ledger node. You can find the full details of how to do that <a href="../.././getting-started/installation-mac/" target=_blank>here</a>.

For this version of documentation alone, run `git checkout master` before building the ledger and running a node.

If you have been running constellation nodes previously, you should remove the databases as they will be incompatible with a fresh node:

``` bash
rm *.db 
```

For example, to run a standalone ledger node listening on port 8000 from the `build` directory, use the following command:

``` bash
./apps/constellation/constellation -port 8000 -block-interval 3000 -standalone
```

Build the Python API libraries like this:

``` bash
pip3 install -U fetchai-ledger-api
```

The API will install to ```tbc```.


### Running a smart contract example in Python

If you want to examine the code in more detail and look at some examples, you may prefer to clone the repo.

``` bash 
git clone https://github.com/fetchai/ledger-api-py.git 
```
And run the installation script:

``` bash
python3 ledger-api-py/setup.py install
```

Open the `contracts.py` script in the `examples` directory:

``` python
from typing import List

from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address

CONTRACT_TEXT = """
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
  if (from_account.get(0u64) >= amount)

    // update the account balances
    from_account.set(from_account.get(0u64) - amount);
    to_account.set(to_account.get(0u64) + amount);
  endif

endfunction

@query
function balance(address: Address) : UInt64
    var account = State<UInt64>(address);
    return account.get(0u64);
endfunction

"""


def print_address_balances(api: LedgerApi, contract: SmartContract, addresses: List[Address]):
    for idx, address in enumerate(addresses):
        print('Address{}: {:<6d} bFET {:<10d} TOK'.format(idx, api.tokens.balance(address),
                                                          contract.query(api, 'balance', address=address)))
    print()


def main():

    # create our first private key pair
    entity1 = Entity()
    address1 = Address(entity1)

    # create a second private key pair
    entity2 = Entity()
    address2 = Address(entity2)

    # build the ledger API
    api = LedgerApi('127.0.0.1', 8000)

    # create wealth so that we have the funds to be able to create contracts on the network
    api.sync(api.tokens.wealth(entity1, 10000))

    # create the smart contract
    contract = SmartContract(CONTRACT_TEXT)

    # deploy the contract to the network
    api.sync(api.contracts.create(entity1, contract, 2000))

    # print the current status of all the tokens
    print('-- BEFORE --')
    print_address_balances(api, contract, [address1, address2])

    # transfer from one to the other using our newly deployed contract
    tok_transfer_amount = 200
    fet_tx_fee = 40
    api.sync(contract.action(api, 'transfer', fet_tx_fee, [entity1], address1, address2, tok_transfer_amount))

    print('-- AFTER --')
    print_address_balances(api, contract, [address1, address2])


if __name__ == '__main__':
    main()
    
```

The `etch` smart contract is embedded into Python as a string.

This particular example creates a pair of `Entity` accounts. The first account is the contract owner who receives some tokens in order to create the contract and deploy it to the ledger. 

Once the contract is deployed to the ledger, the second account receives a transfer of tokens.



<br/>
## Test network

!!! note
	Implementation details for running smart contract code against a test network are coming soon.



## Public network


!!! note
	In development.


<br/>
