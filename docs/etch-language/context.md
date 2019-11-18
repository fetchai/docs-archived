`Context` is an `etch` language type that provides access to currently invoking ledger transaction data - such as block and transaction information - coming from smart contracts running against ledger nodes.

## Specific annotated functions

-   Smart contract transaction data is available in functions annotated with `@init` and `@action`.

<!--
* Synergetic contract transaction data is available in functions annotated with .. and `@clear`.
-->

This means that, putting `Context` code in `@query` functions or other functions not equipped to access a `Context`, should raise an error.

!!! Note
It is not possible to provide standalone `etch` code snippet examples as `Context` requires a running ledger node.

## Coding with `Context`

!!! Note
The only way to get a `Context` is by calling `getContext()`.

The `Context` object has two member functions.

-   `block()`: returns access to the current `Block` object - see below.
-   `transaction()`: returns access to the current `Transaction`. Check <a href="../transaction/" target=_blank>the `Transaction` documentation</a> for details.

We will execute the example below against a local ledger node. Instructions for running a ledger node are <a href="/../getting-started/run-a-node/" target=_blank>here</a>.

`etch` smart contract code is wrapped inside Python Ledger API scripts which take care of the implementation against a running ledger (think truffle/ganache plus web3).

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>Full and complete documentation for the <a href="https://github.com/fetchai/ledger-api-py" target=_blank>Python Ledger API</a> is currently in development. Please check <a href="/smart-contracts/pipenv/" target=_blank>here</a> for updates.</p>
</div>

## `getContext()`, `block()`, and `blockNumber()`

To get a `Context`, call `getContext()`.

From here, you have access to the `Block` object which has a `blockNumber()` function that returns the current block number.

The following syntax grabs the `Context`, gets the `Block` object from the `Context`, then runs the `blockNumber()` function of `Block` which returns the current block number.

```c++
var context = getContext();
var block = context.block();
var block_number = block.blockNumber();
```

## Example

The following `etch` smart contract tests the `Context` and `Block` types and the `blockNumber()` function.

```c++
persistent init_block_number_state : UInt64;

@init
function set_block_number(owner : Address) : Int64
  use init_block_number_state;

  var context = getContext();
  var block = context.block();
  var block_number = block.blockNumber();

  init_block_number_state.set(block_number);

  return toInt64(block_number);
endfunction

@query
function get_init_block_number_state() : UInt64
  use init_block_number_state;

  return init_block_number_state.get(0u64);
endfunction
```

Now run the above embedded in this script that calls the Python Ledger API.

```python
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity

CONTRACT_TEXT = "[as above]"

def run(options):
    entity1 = Entity()
    # build the ledger API
    api = LedgerApi(options['host'], options['port'])
    # create wealth so that we have the funds to be able to create contracts on the network
    api.sync(api.tokens.wealth(entity1, 100000))

    contract = Contract(CONTRACT_TEXT, entity1)

    # deploy the contract to the network
    status = api.sync(api.contracts.create(entity1, contract, 20000))[0]

    block_number = contract.query(api, 'get_init_block_number_state')

    print(block_number)


if __name__ == "__main__":
    run({'host': '127.0.0.1', 'port': 8100})
```

The script prints the current block number to the console.

<br />
