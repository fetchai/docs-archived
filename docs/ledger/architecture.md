!!!	note
	We assume the reader is comfortable with high level concepts that underpin blockchain technology, such as public key cryptography, consensus, blockchain, and smart contracts.

## Sharding

The Fetch.ai Ledger is unlike more traditional blockchain designs. Instead of a single chain of truth, the Fetch.ai Ledger is sharded into parallel lanes. 

<center>![Memory mapping on the Fetch.ai Ledger shards](../smart-contracts/img/shards-basic.png)</center>

This blockchain sharding design speeds up the network as contracts can execute concurrently and so provide a solution to the blockchain scalability problem. Furthermore, by sharding the *world state* in this way, transactions guarantee they only use certain resources, i.e. memory locations.

This means that the *size* of a block can vary by increasing or decreasing the number of shards. This allows the network to balance block sizes against economic incentives, for example. 

The consequence of this design means the *world state* is best sharded across multiple machines to scale access and avoid resource locking. 

*Constellation* is the name of the main controlling node. The shards are termed *lanes*.

The following diagram gives a high level overview of the components making up a constellation application. This is work in progress.


## High level architecture diagram 

![Fetch.ai Ledger architecture high level view](img/architecture.png)


!!!	note
	For a more thorough understanding of the Fetch ledger architecture, please read <a href="https://fetch.ai/wp-content/uploads/2019/10/technical-introduction.pdf" target=_blank>the Fetch.ai whitepaper</a>. 



## Constellation

!!!	Note
	This section is coming soon.


## Wallet API

!!!	Note
	This section is coming soon.



## P2P Service

!!!	Note
	This section is coming soon.



<br/>