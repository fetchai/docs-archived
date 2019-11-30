<h1>Etch smart contracts</h1>

Smart contract code runs on the `etch` virtual machine.

All ledger nodes contain the `etch` VM and smart contract code.

The identity of a smart contract is calculated by performing a `SHA256` hash on the contract code string as an initial step. Next, a further `SHA256` hash is calculated from the previous result concatenated with a public key `Address` which represents the contract owner.

On the ledger, the `etch` VM stores the contract identity, the contract source code, and the data resources that are mapped by a `data.json` file.

With this information, the `etch` VM performs a modulo 16 calculation to decide where to store the data on the ledger, i.e. onto which shard.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Coming soon: details on how developers may dictate the sharding storage design for a smart contract.</p>
</div>

## Smart contract addresses

`etch` smart contracts have a unique identification protocol for addressing on the Fetch.ai Ledger.

`etch` smart contract identifiers are a SHA256 hash of the contract source code which is then Base64 encoded and finally concatenated with the Base64 encoded owner's public key.

Using this identifier, smart contract functions are accessible with a subsequent `.` plus function name.

## Data confirmation

If you run an `etch` contract in the simulator containing one or more `State` types and flag the compiler with `-data` and a filename, it will create a `json` file containing the details of the data that will be stored on the ledger.

`./etch *filename* -data data.json`

If we run one of the above code examples in this way, `data.json` may contain the following:

```json
{ "2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9": "8403000000000000" }
```

<!-- removed in respect of Context object tx access methods
## Utility functions

`getBlockNumber()` : returns the number of the current block in `UInt64`.

You need a node running to test this. As well as that, you can only get a result when the function is embedded within smart contract code in Python. See a coded example of `getBlockNumber()` with a running node <a href="../../tutorials/block-number" target=_blank>here</a>.
-->

<br/>
