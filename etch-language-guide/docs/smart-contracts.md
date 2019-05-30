<h1>Smart contracts</h1>

Smart contract code runs on the `etch` VM. 

All ledger nodes maintain `etch` VM and smart contract code.

Unlike the common cryptographic transactions we have just seen, smart contract code computes more complex functions on the `etch` VM.

The identity  of a smart contract is calculated by performing a `SHA256` hash of the contract code as an initial step. Next, a further `SHA256` hash is calculated from the previous result concatenated with a public key `Address`.

On the ledger, the `etch` VM stores the contract name, the contract source code, and the data resources that are mapped by a `data.json` file.

Taking this contract identity data, the `etch` VM performs a modulo 16 calculation from which it decides how to store the data on the ledger, i.e. onto which shard.

!!! note
	Coming soon: details on how developers may dictate the sharding storage design for a smart contract.



## Basic Smart contract

Smart contract functions are annotated depending on the activity they perform.

<H3>@init</H3>	

The `@init` function defines a contract constructor that sets the state of the contract prior to any operations performed on it. It is called once and once only on contract initialisation.

The name of the `@init` function can be anything you like.

For example, the following function initialises a contract by creating a `State` type that represents the owner's account which sets an initial supply of FET tokens. 


``` java
@init
function initialise(owner: Address)

    var INITIAL_SUPPLY = 100000000000u64;
    var account = State<UInt64>(owner, 0u64);
    account.set(INITIAL_SUPPLY);

endfunction
```


<H3>@action</H3>

The `@action` annotation signifies a function which deals with transaction details. You cannot create a contract in `etch` without an `@action` function and it is these functions that trigger the charging rules for data persistence fees.

The following function performs a transaction between two parties.

``` java
@action
function transfer(from: Address, to: Address, amount: UInt64)
	var from_balance = State<UInt64>(from, 0u64); 
	var to_balance = State<UInt64>(to, 0u64);

	// check if all the conditions are valid
	var valid = from.signed_tx() && (from_balance.get() >= amount);

	if (valid)
		// update the funds
		from_balance.set(from_balance.get() - amount);
		to_balance.set(to_balance.get() + amount);
	endif
endfunction
```

In the worst case, the above function needs two shards for data.


<h3>@query</h3>

Query functions are read-only functions that allow you to view data on the ledger. 

The following function queries the balance of an `Address`.

``` java
@query
function balance(address : Address) : UInt64

	var account = State<UInt64>(address, 0u64);
	return account.get();

endfunction
```

## Data confirmation

If you run an `etch` contract containing one or more `State` types and flag the compiler with `-data` and a filename, it will create a `json` file containing data details.

`./vm-lang *filename* -data data.json`

`data.json` may contain the following:

``` json
	{"var": "0a000000"}
```

## Utility functions

```getBlockNumber()``` : returns the number of the current block in `UInt64`.



## Python compilation

!!! note 
	Coming soon: author is researching this.


## Run against testnet

!!! note 

	Coming soon: author is researching how the Fetch Ledger Python API communicates with `etch` smart contract code.

	Research includes the following documentation:

	* Spinning up some test nodes - instructions <a href="https://community.fetch.ai/getting-started/building-fetchai-ledger-node/develop/" target="_blank">here</a>.

	* Setting up the Python API - instructions <a href="https://community.fetch.ai/getting-started/send-transaction-over-http-using-python-sdk/develop/" target="_blank">here</a>.
