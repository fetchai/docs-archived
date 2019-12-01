# Fetch.ai ledger

The ledger serves as the foundations for the rest of the Fetch.ai platform. There are several reasons that lead us to develop a new ledger, some of which are listed below.

## Increased rate of transactions per second

The origin of the limited throughput of Bitcoin and other conventional distributed ledger technologies is the sequential organization of blocks in a chain. All full processing nodes must keep a copy of the ledger, and blocks must be distributed across the peer-to-peer network in their entirety.

Although the serial nature of blockchains limits their throughput, it is also crucial for security purposes. To succeed in inserting a conflicting event into the global consensus, the attacker must potentially re-write the entire history of the ledger, which becomes more difficult as time progresses.

In order to increase throughput, while still preserving the consistency that prevents double-spending attacks, the Fetch.ai ledger relaxes the requirement on sequential execution by partitioning resources into mutually disjoint subsets called _resource groups_. Transactions that affect resources from different groups are then handled by separate _resource lanes_.

Resource lanes are a novel componentof the Fetch.ai ledger architecture and you can read more about them [here](architecture.md).


## Custom consensus algorithm

The blockchain trilemma states that scalable blockchains cannot achieve both security and decentralisation, but our protocol aims to overcome said trilemma by forcing block producers to behave in a very restricted way and have limited flexibility. Critically, individual nodes have little control over which transactions go into the blockchain. These features give the ledger security and performance characteristics to match centralised systems.

The protocol uses a Proof-of-Stake mechanism to construct a blockchain, a Decentralised Random Beacon to elect a
group of nodes that collaboratively build and decide upon the next block that will be entered into the ledger, and a Directed Acyclic Graph for coordination and notarization.

For better understanding of our consensus protocol, please read [this blog post](https://medium.com/fetch-ai/a-minimal-agency-consensus-scheme-2a9a2fae7d26) and [the whitepaper](https://www.fetch.ai/uploads/Fetch.AI-A-Minimum-Agency-Consensus-Paper.pdf).

## Support for on-chain ML and AI operations

Coming soon.
