# Developing smart contracts
We will discuss smart contracts examples in more details in one of the later tutorials, but before we dive into the examples, we will TODO.

## Developing contracts with vm-lang


## Submitting the contract to the ledger


```
import base64
import time
import hashlib
import json
import binascii
import msgpack

from fetchai.ledger.serialisation.objects.transaction_api import create_json_tx
from fetchai.ledger.api import ContractsApi, TransactionApi, submit_json_transaction
from fetchai.ledger.crypto import Identity

HOST = '127.0.0.1'
PORT = 8100


identity = Identity()
next_identity = Identity()

status_api = TransactionApi(HOST, PORT)
contract_api = ContractsApi(HOST, PORT)

create_tx = contract_api.create(identity, contract_source, init_resources = ["owner", identity.public_key])

print('CreateTX:', create_tx)

while True:
    status = status_api.status(create_tx)

    print(status)
    if status == "Executed":
        break

    time.sleep(1)

# re-calc the digest
hash_func = hashlib.sha256()
hash_func.update(contract_source.encode())
source_digest = base64.b64encode(hash_func.digest()).decode()

print('transfer N times')

for index in range(3):

    # create the tx
    tx = create_json_tx(
        contract_name=source_digest + '.' + identity.public_key + '.transfer',
        json_data=msgpack.packb([msgpack.ExtType(77, identity.public_key_bytes), msgpack.ExtType(77, next_identity.public_key_bytes), 1000 + index]),
        resources=['owner', identity.public_key, next_identity.public_key],
        raw_resources=[source_digest],
    )

    # sign the transaction contents
    tx.sign(identity.signing_key)

    wire_fmt = json.loads(tx.to_wire_format())
    print(wire_fmt)

    # # submit that transaction
    code = submit_json_transaction(HOST, PORT, wire_fmt)

    print(code)

    time.sleep(5)

print('Query for owner funds')

source_digest_hex = binascii.hexlify(base64.b64decode(source_digest)).decode()

url = 'http://{}:{}/api/contract/{}/{}/owner_funds'.format(HOST, PORT, source_digest_hex, identity.public_key_hex)

print(url)

r = status_api._session.post(url, json={})
print(r.status_code)
print(r.json())
```