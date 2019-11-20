Run the following Python script and embedded smart contract to test the `getBlockNumber()` function.

You need to run this against a running node on localhost port `8100`. 

Details for running a node are <a href="../../getting-started/run-a-node/" target=_blank>here</a>.


``` c++
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address

CONTRACT_TEXT = """
@action
function set_block_number_state()
  State<UInt64>('block_number_state').set(getBlockNumber());
endfunction

@query
function query_block_number_state() : UInt64
    return State<UInt64>('block_number_state').get(0u64);
endfunction
"""


def main():

    entity1 = Entity()

    # build the ledger API
    api = LedgerApi('127.0.0.1', 8100)

    # create wealth so that we have the funds to be able to create contracts on the network
    api.sync(api.tokens.wealth(entity1, 100000))

    # create the smart contract
    contract = SmartContract(CONTRACT_TEXT)

    # deploy the contract to the network
    api.sync(api.contracts.create(entity1, contract, 2000))

    api.sync(contract.action(api, 'set_block_number_state', 400, [entity1]))

    print(contract.query(api, 'query_block_number_state'))


if __name__ == '__main__':
    main()

```


<br/>