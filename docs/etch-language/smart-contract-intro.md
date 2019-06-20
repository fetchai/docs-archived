<h1>Introduction</h1>

A <a href="https://en.wikipedia.org/wiki/Smart_contract" target="_blank">smart contract</a> facilitates, verifies, and enforces a transaction between two or more parties on a distributed ledger or blockchain. 

Smart contracts store transactional data on the permanent and irreversible blockchain ledger and, on doing so, change the state of the ledger. 

Smart contract programming languages are scripting languages specific to the cryptocurrency or platform, such Bitcoin's Script or Ethereum's Solidity. 

Fetch.AI smart contracts run on the `etch` virtual machine (VM) which is a logical computation layer used to execute smart contract code. The `etch` VM and smart contract code reside on every node of the Fetch distributed ledger.

Smart contracts can be used for voting applications, crowdfunding, auctions, multi-signature wallets, identity verification, and much more.

`etch` builds up smart contracts using `State` data structures and the `Address` type which represents account owners and gives access to respective balances. 





## The Ledger

Smart contract transactions are etched onto the Fetch.AI distributed ledger, or blockchain, and are therefore permanent, traceable, and irreversible.

The Fetch.AI ledger is the blockchain foundation of the `etch` VM. Quick start instructions for spinning up a Fetch.AI ledger node are <a href="../.././getting-started/installation/" target=_blank>here</a>.

The Fetch.AI ledger is unlike more traditional blockchain designs. Instead of a single chain of truth, the Fetch.AI ledger is sharded into parallel lanes. 

<center>![Memory mapping on the Fetch.AI ledger shards](img/shards-basic.png)</center>

This blockchain sharding design speeds up the network as contracts can execute concurrently.


## Determinism

In computer science, <a href="https://en.wikipedia.org/wiki/Deterministic_system#In_computer_science" target="_blank">determinism</a> ensures that an input to an algorithm will always produce the same output. 

When designing `etch` smart contract code which will execute on Fetch ledger nodes, it is essential to avoid non-deterministic behaviour that may break consensus. Any code that causes separate nodes to have different values for the same thing may break consensus.

Smart contract developers should therefore consider the following: 

* Randomness: along with random functions, non-deterministic randomness can arise in other places, such as `Hash Map` implementations and `Map` iterations, for example.
* Concurrency: multiple processes targeting the same state transactions can break consensus.
* Ill-considered imports: e.g. libraries containing non-deterministic functions, such as time functions, or APIs that access external and unpredictable systems.
* Timestamps: watch out for non-deterministic timestamp implementations.
* Asynchronous behaviour can break consensus.

It may be better to implement any essential non-deterministic behaviour outside of smart contract ledger code.




## Fees

Fetch.AI charges developers for computation and storage of data on the ledger in a manner which incentivizes good coding practices.

You can limit the fees paid for smart contract execution by distributing data storage over a single shard and a minimum number of shard lanes.

Fees rise in a linear manner per number of shards up to the maximum number of shards, after which point the fees increase exponentially.

!!! note 
	Coming soon: details of developer fee structures for smart contract data.


<br/>