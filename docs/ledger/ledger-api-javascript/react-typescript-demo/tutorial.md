# Overview

The [Ledger API Javascript React Typescript Node.js](https://github.com/fetchai/demo-typescript-ledger-example) is a demo of the [Ledger API Javascript](https://github.com/fetchai/ledger-api-javascript).
The Ledger API Javascript is a browser and Node.js capable NPM module [fetchai-ledger-api](https://www.npmjs.com/package/fetchai-ledger-api) 
which provides high level methods to allow simple interaction with the [Fetch Ledger](https://docs.fetch.ai/). 

Functionality of the [Ledger API Javascript](https://github.com/fetchai/ledger-api-javascript) includes:

- Generation of new Addresses and their associated private keys.
- Checking balances (Fet in 10^-10) held at accounts, using Addresses.
- Transferring Fet between accounts.
- Submitting smart contracts to the Fetch Ledger.
- Finding available servers to connect to on the fetch network(termed Bootstrapping).

Functionality covered in this [demo](https://github.com/fetchai/demo-typescript-ledger-example) includes:

- Generation of new Addresses and their associated private keys.
- Checking balances (Fet in 10^-10) held at accounts.
- Finding available servers to connect to (termed Bootstrapping).    

## Installation of Node
Use node version manager (nvm) to install latest stable version of npm:
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
nvm install node
nvm use node
nvm install --lts
nvm use --lts
```

## Installation of Project
```
git clone https://github.com/fetchai/demo-typescript-ledger-example
npm install 
```
## Run

```
npm run build
npm run start
```

## Requiring the fetchai-ledger-api NPM Module 

- whilst in this demo the above `npm install` will handle the installation of the NPM Module the below command can be used 
    one can install the module like so:

```
npm install -i fetchai-ledger-api
``` 

- One can  require the address class like so
```import {Address} from "fetchai-ledger-api";```

-However in this Demo we combine the imports of the four classes which we use in the below single statement
```
import {Bootstrap, Entity, Address, LedgerApi} from "fetchai-ledger-api";
```
   
## Working with Addresses

### Overview

- An account consist of an Address and a private key. An Address contains a public key and allows one to transfer Fet into an account and one to look-up the balance held by an account.
- A private key allows for withdrawal of funds, and thus ought to be kept secret. 
- The Entity class represents a public/private key pair and some basic operations pertaining to this such as key generation and generation of a 
  an Address from a private key. 
  
- The Address class by contrast contain only Addresses, the public component of an account, and is useful for validating Address formats, and converting between different formats.
 
### Code Explanation
 
- Create a new Private key by instantiating an Entity object without passing any parameters:

```
const entity = new Entity()
```
- Return the the private key in hexadecimal    
```
const private_key_hex = entity.private_key_hex()
```
- We can also return the key as a buffer
```
const private_key_buffer = entity.private_key()
  ``` 
- Which can be converted to a base 64 string
```
const base64_data = private_key_buffer.toString('base64')
  ``` 
- We can construct an Entity from a buffer holding a private key
```
const entity = new Entity(private_key)
```
- We can also construct it from a base64 string
```
const other = Entity.from_base64(base64_data)
``` 
- To get the Address of a our user pass the entity as a parameter to the new Address constructor like so
```
const address = new Address(entity).toString()
```

## Connecting to a Server (Bootstrapping)

### Overview

Whilst anybody may run a node of the [Fetch Ledger](https://docs.fetch.ai/) there are some publicly available servers
whose Addresses can be found using the Bootstrapping functionality. 
The Host and Port values returned will by below code will then be used when querying the balance later in this example, 
or for other actions related to the ledger such as making a transfer or submitting a smart contract. 

Requiring the Bootstrapping Class
```
const Bootstrap = require('fetchai').Bootstrap
```
One can pass in the name of a server ran by Fetch.ai such as 'devnet'.
```        
const [host, port] = await Bootstrap.server_from_name("devnet")
```

## Querying the Balance of an Account

### Overview

Balances are stored as integers in 10^-10 Fet, and can be queried by anybody with an Address.  

### Code Explanation

- Require the LedgerApi class
```
const LedgerApi = require('fetchai').LedgerApi
```
- Create a new Ledger Object with the host (URI) and port of an available server
```
 const api = new LedgerApi(host, port)
```
- To Query the balance (returning an integer value equal to the quantity of Nano Fet held at the account) call the balance method with the public Address 
``` 
        try {
           const balance = await api.tokens.balance(data.address)
        } catch (e) {
           // handle errors
        }
```

