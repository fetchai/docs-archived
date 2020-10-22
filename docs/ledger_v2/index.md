# Getting Ready for Mainnet V2

We are hard at work preparing for Fetch mainnet version 2, which is currently due for release in the next few months. But you can get prepared __now__. This documentation covers some of the things you need to know in order to prepare for and develop for this new network:

## Test Networks

The starting point for most developers will be our Agent Land test network, since this is primarily used for agent development and testing. Agent Land is **fully supported** by our Agent Framework from version 0.6 and above. If you are developing autonomous economic agents using our latest framework, then moving to Agent Land is relatively straightforward, unless smart contracts are involved.

Agentland and other testnets on the journey have a new address format. Here is a typical example:

```text
fetch1almpjpf769p23k0v4m5eglvzr4jupsjs66vxf4
```

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>These new addresses are not compatible with mainnet v1 or testnet v1. It is expected that users will create new address for agents on the network</p>
</div>

## Key links and information

Block explorer and token tap: [https://explore-agent-land.fetch.ai/](https://explore-agent-land.fetch.ai/)

Understanding building block relationships: [https://docs.fetch.ai/aea/oef-ledger/](https://docs.fetch.ai/aea/oef-ledger/)

For more detailed information, have a look at our [network](./networks/) information page.

### Other testnets

There are currently three key sequential testnets planned, but more may arise and operate in parallel in order to target the testing and development of specific additional new technologies. The three main incentivised testnet phases are:

1. [**Agents**](../i_nets/quickstart-aw1.md): a stable testnet for autonomous economic agents, featuring the core new mainnet v2 technologies that agent developers need in order to prepare.
2. [**Random Beacon**](../i_nets/quickstart-aw2.md): a stable testnet showcasing the decentralised random beacon, vital for DeFi, gaming and a key part of our on-going unique approach to consensus.
3. [**Oracles**](../i_nets/quickstart-aw3.md): a stable testnet for demonstrating connecting the outside world to the inside world; enabling agents to communicate reliable, trustworthy information from the environment at large.

## Roadmap for Smart Contracts

Mainnet V2 and the current testnet do not support the same smart contract language as mainnet version 1. When mainnet V2 is released, smart contracts will be developed using Cosmwasm, which will include the ability to develop your contracts in a number of languages depending on your preferences, such as Rust, Go or Javascript. For more information on Cosmwasm, and Rust, the primary language in which contract development is currently done, you can go to https://www.cosmwasm.com/ and https://github.com/CosmWasm/cosmwasm-template

