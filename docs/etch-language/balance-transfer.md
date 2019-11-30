Like `Context`, `Block`, and `Transaction`, the balance and transfer functions must run against a Fetch.ai Ledger node.

## `balance()`

The balance function returns the balance of funds owned by the contract address as a `UInt64` type.

```c++
@action
function check_balance()

    var bal : UInt64 = 0u64;
    bal = balance();
    printLn(bal);

endfunction
```

You can call `balance()` from a smart contract currently invoking against a node in the following annotated smart contract functions:

-   `@init`
-   `@action`
-   `@query`

You can call `balance()` from a synergetic contract currently invoking against a node in the following annotated synergetic contract functions:

-   `@clear`

## `transfer(target : Address, amount : UInt64)`

The transfer function allows the smart contract to transfer an amount of FET to a receiving entity.

It takes two parameters:

-   An `Address` type representing the receiving entity.
-   A `UInt64` value representing the amount of FET the entity will receive.

```c++
@action
function transfer_funds(target : Address, amount : UInt64)

  transfer(target, amount);

endfunction
```

You can call `transfer()` from a smart contract currently invoking against a node in the following annotated functions:

-   `@init`
-   `@action`

You can call `transfer()` from a synergetic contract currently invoking against a node in the following annotated functions:

-   `@clear`

## Example

Let's execute an example against a local ledger node. Instructions for starting up a ledger node are <a href="/../getting-started/run-a-node/" target=_blank>here</a>.

### `etch` smart contract code

The `etch` code here and `Python` wrapper code below it comes from <a href="https://github.com/fetchai/ledger/blob/master/scripts/end_to_end_test/smart_contract_tests/transfer.py" target=_blank>a Python Ledger API wrapped example</a> that you can run against a Fetch.ai ledger node.

The first contract code is here.

```c++
persistent balance_state : UInt64;

@action
function set_balance_state()
  use balance_state;

  balance_state.set(balance());
endfunction

@query
function query_balance_state() : UInt64
  use balance_state;

  return balance_state.get(567u64);
endfunction

@action
function transfer_funds(target : Address, amount : UInt64)
  transfer(target, amount);
endfunction
```

And the second smart contract code is here.

```c++
@action
function transfer_funds1(target : Address, amount : UInt64)
  transfer(target, amount);
endfunction
```

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>Full and complete documentation for the <a href="https://github.com/fetchai/ledger-api-py" target=_blank>Python Ledger API</a> is currently in development. Please check <a href="/smart-contracts/pipenv/" target=_blank>here</a> for updates.</p>
</div>

This beautiful example show how smart contracts may interact with each other.

### Python Ledger API wrapper code

```python
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

CONTRACT_TEXT = """first contract as above"""
TRANSFER_CONTRACT_TEXT = """second contract as above"""


def balance_within_range(actual, expected, fees=150):
    return actual >= expected - fees


def setup(api):
    entity1 = Entity()

    api.sync(api.tokens.wealth(entity1, 100000))

    contract1 = Contract(TRANSFER_CONTRACT_TEXT, entity1)
    contract2 = Contract(CONTRACT_TEXT, entity1)

    initial_owner_balance = api.tokens.balance(Address(entity1))
    assert initial_owner_balance == 100000, \
        'Expected initial directly-queried balance to be 0, found {}'.format(
            100000, initial_owner_balance)

    api.sync(api.contracts.create(entity1, contract1, 2000))
    api.sync(api.contracts.create(entity1, contract2, 2000))

    return entity1, contract1, contract2


def transfer_and_verify_balances(api, entity, address_to, amount):
    from_balance_before = api.tokens.balance(Address(entity))
    to_balance_before = api.tokens.balance(address_to)

    assert from_balance_before > amount, \
        'Insufficient funds'

    print('Transfer from {} to {}'.format(Address(entity), address_to))
    api.sync(api.tokens.transfer(entity, address_to, amount, 100))

    from_balance_after = api.tokens.balance(Address(entity))
    assert balance_within_range(from_balance_after, from_balance_before - amount), \
        'Expected balance to decrease by {} - found {} (before); {} (after)'.format(
            amount, from_balance_before, from_balance_after)

    to_balance_after = api.tokens.balance(address_to)
    assert balance_within_range(to_balance_after, to_balance_before + amount), \
        'Expected balance to increase by {} - found {} (before); {} (after)'.format(
            amount, to_balance_before, to_balance_after)


def call_transfer_action_and_verify_balances(api, source_contract, action, signers, target_address, amount):
    from_balance_before = api.tokens.balance(source_contract.address)
    to_balance_before = api.tokens.balance(target_address)

    assert from_balance_before > amount, \
        'Insufficient funds'

    print('Transfer from {} to {}'.format(
        source_contract.address, target_address))
    api.sync(source_contract.action(
        api, action, 100, signers, target_address, amount))

    from_balance_after = api.tokens.balance(source_contract.address)
    assert balance_within_range(from_balance_after, from_balance_before - amount), \
        'Expected balance to decrease by {} - found {} (before); {} (after)'.format(
            amount, from_balance_before, from_balance_after)

    to_balance_after = api.tokens.balance(target_address)
    assert balance_within_range(to_balance_after, to_balance_before + amount), \
        'Expected balance to increase by {} - found {} (before); {} (after)'.format(
            amount, to_balance_before, to_balance_after)


def run(options):
    api = LedgerApi(options['host'], options['port'])

    # Create an entity and have it deploy both contracts
    entity1, contract1, contract2 = setup(api)

    # Have entity1 send contract1 some money
    transfer_and_verify_balances(api, entity1, contract1.address, 2345)

    # Have contract1 send contract2 some of its money
    call_transfer_action_and_verify_balances(
        api,
        contract1,
        'transfer_funds1',
        [entity1],
        contract2.address,
        1345)

    # Have contract2 send some money back to its owner
    call_transfer_action_and_verify_balances(
        api,
        contract2,
        'transfer_funds',
        [entity1],
        Address(entity1),
        1000)


if __name__ == "__main__":
    run({'host': '127.0.0.1', 'port': 8100})
```

You should see similar to the following results.

```bash
WARNING:root:Defaulting to wildcard shard mask as none supplied
WARNING:root:Defaulting to wildcard shard mask as none supplied
Transfer from 2VkKoC7DvBz6wXKZyoypkg2xsRBkE3FdNGXHqShqcEevYray4J to 24sx12GNYMRSFHLyUkiPLmfjeydeV5225RYZfpu2Qvk2LMpWWu
Transfer from 24sx12GNYMRSFHLyUkiPLmfjeydeV5225RYZfpu2Qvk2LMpWWu to 2mfWzyUTgoju5nWYMENf7M1yLE3b2Ma31kmAhKPvAW7ytBydev
Transfer from 2mfWzyUTgoju5nWYMENf7M1yLE3b2Ma31kmAhKPvAW7ytBydev to 2VkKoC7DvBz6wXKZyoypkg2xsRBkE3FdNGXHqShqcEevYray4J

Process finished with exit code 0
```

<br />
