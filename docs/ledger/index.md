# Fetch.ai ledger

TODO Reasons why a new ledger needed to be developed

## Custom consensus algorithm



## Increased rate of transactions per second

The origin of the limited throughput of Bitcoin and other conventional distributed ledger technologies is the sequential organization of blocks in a chain. All full processing nodes must keep a copy of the ledger, and blocks must be distributed across the peer-to-peer network in their entirety.

Although the serial nature of blockchains limits their throughput, it is also crucial for security purposes. To succeed in inserting a conflicting event into the global consensus, the attacker must potentially re-write the entire history of the ledger, which becomes more difficult as time progresses.

In order to increase throughput, while still preserving the consistency that prevents double-spending attacks, the Fetch.ai ledger relaxes the requirement on sequential execution by partitioning resources into mutually disjoint _resource groups_. Transactions that affect resources from different groups are then handled by separate _resource lanes_.

Resource lanes are a novel componentof the Fetch.ai ledger architecture and you can read more about them [here](architecture.md).


## Support for on-chain ML and AI operations

Coming soon.
