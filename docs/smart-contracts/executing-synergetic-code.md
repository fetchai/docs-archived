<h1>Executing synergetic contract code</h1>

!!! Warning
    Synergetic contracts are currently an experimental feature.

To test synergetic contracts, run a ledger node in synergetic mode using specific flags.

``` bash
./constellation -standalone -block-interval 1000 -experimental synergetic,naive-synergetic-mining
```

In the Python API `examples` folder, take a look at the `synergetic.py` script.

``` python
import os
import random
import json

from fetchai.ledger.api import LedgerApi
from fetchai.ledger.crypto import Entity, Address
from fetchai.ledger.contract import SynergeticContract

CONTRACT_TEXT = """
@problem
function createProblem(data : Array<StructuredData>) : Int32
  var value = 0;
  for (i in 0:data.count() - 1)
    value += data[i].getInt32("value");
  endfor
  return value;
endfunction

@objective
function evaluateWork(problem : Int32, solution : Int32 ) : Int64
  return abs(toInt64(problem) - toInt64(solution));
endfunction

@work
function doWork(problem : Int32, nonce : BigUInt) :  Int32
  return nonce.toInt32();
endfunction

@clear
function applyWork(problem : Int32, solution : Int32)
  var result = State<Int32>("solution", 0);
  result.set(solution);
endfunction

"""


def main():
    # create the API
    api = LedgerApi('127.0.0.1', 8100)

    # create an entity and provide it some wealth
    print('Setup...')
    entity = Entity()
    api.sync(api.tokens.wealth(entity, 100000000))
    print('Setup...complete')

    # create the contract on the ledger
    synergy_contract = SynergeticContract(CONTRACT_TEXT)
    print(synergy_contract.digest)

    api.sync(api.contracts.create(entity, synergy_contract, 4096))

    # create a whole series of random data to submit to the DAG
    random_ints = [random.randint(0, 200) for _ in range(4000)]
    api.sync([api.synergetic.submit_data(entity, synergy_contract.digest, value=value) for value in random_ints])


if __name__ == '__main__':
    main()


```

In the synergetic contract example above, the `@problem` function sets up a calculation over an array and returns the value. 

The `@objective` function evaluates the work done on the problem giving a measure as to how close the current solution is to the correct result.

The `@doWork` function returns a nonce to kick start the calculations.

The `@clear` function tidies up once a solution has been found and saves the correct result to the ledger.

<br/>