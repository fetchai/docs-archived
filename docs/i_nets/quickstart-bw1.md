## Introduction: Beacon World 1 (BW-1) - part 1, Getting started with Staking and Governance

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>BW-1 is live now!</p>
</div>

Beacon-world 1 (BW-1) is the second stage of our program for testing the Fetch.ai blockchain and for preparing our community for the launch of our v2.0 main-net. The goal of BW-1 is to reward users and potential validators for gaining experience with the software ecosystem around the main-network. These tasks don't require any technical knowledge or programming experience; all you need is an interest in Fetch.ai and a willingness to help shape its future direction.

## Rewards

The following table shows the incentive rewards on offer.

Action             | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first served)
------------------ | -------------------------- | ------------------------- | ----------------------------
Steps 1 - 4 below  | 100                        | 100                       | 300
Tweet              | 0                          | 50                        | 300


A key responsibility of validators, developers and users is that they take part in decisions on the future directions of the project. The way that these decisions are made is known as governance and is a key element of decentralised networks. The Fetch.ai ledger uses a simple governance mechanism that was first used by <a href="https://www.coindesk.com/bitcoin-coders-confront-an-old-quandary-how-to-upgrade-an-entire-network" target="_blank">Bitcoin</a>, where a majority of miners have to make a decision on whether to perform a specific software upgrade to the network.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p> To qualify for rewards, users must first <a href="https://fetch.ai/staking/" target="_blank">stake</a> FET ERC20 tokens on Ethereum.

  While not strictly necessary we also encourage people who have not already done so to try out at least the [AW-1](./quickstart-aw1/) challenge.</p>
</div>

## How To Earn Rewards

To earn rewards, users must complete the following tasks, which are designed to familiarise them with the tools used for sending transactions, delegating stake and voting on governance proposals. The general flow is as follows:

1. Create a test-net address and link this to their Ethereum staking address (anyone who has completed the <a href="../quickstart-aw1/" target="_blank">AW-1</a> task can skip this step).

2. Send a transaction on the test-net.

3. Delegate stake to one of the validators on the test-net.

4. Vote on at least one governance proposal.

We recommend that everyone joins our discord channel <a href="https://discord.gg/UDzpBFa" target="_blank">here</a>, as this is the quickest way to answer any questions and receive support from the team and the rest of the community.

There are technical and community tracks for interacting with the BW-1 test-net. We recommend that developers or anyone who is interested in running a validator node follow the technical track while non-technical users should follow the community track. Please note that a <a href="https://www.ledger.com" target="_blank">ledger</a> nano hardware wallet is required for the community track. It's possible to follow the steps in both tracks but only one reward is available for each Ethereum staking address that is registered.

## Community (Non-Technical) Track

Non-technical users should follow these steps:

1. Install the <a href="https://cosmos.network/" target="_blank">Cosmos</a> app on your Ledger nano by following these [instructions](/ledger_v2/cli-keys/#hardware-wallets)</a>.

2. Connect your Ledger nano to the <a href="https://explore-agentworld.prod.fetch-ai.com" target="_blank">block explorer</a> using the instructions [here](/ledger_v2/block-explorer/#logging-in-with-the-ledger-nano).

3. Request tokens to your Ledger nano address using the [token faucet](/ledger_v2/block-explorer/#getting-testnet-tokens-from-the-faucet).

4. Sign the test-net address where you requested tokens in step 3 with the private key tied to your FET account on the Ethereum mainnet (this is the account you use for FET staking):

	- We recommend you use our <a href=https://fetchai.github.io/web-ethereum-signer/ target="_blank">signing app</a> with your <a href="https://docs.metamask.io/guide/signing-data.html#a-brief-history" target="_blank">MetaMask</a> wallet, alternatively use <a href="https://www.myetherwallet.com/interface/sign-message" target="_blank">MEW</a> or a similar wallet to sign your Fetch.ai test-net address.

5. To complete registration, send a transaction of 0.01 FET to this address: `fetch1a3ecdm538yt4xlz6kc39xf0h3syge0mlrr0jgf` but make sure that you add the Ethereum address you used for staking tokens in the "memo" field.

6. Send a second transaction of 0.01 FET to the same address but this time add the signature in the "memo" field that you generated in step 4.

7. Delegate Stake to any of the validators using the instructions [here](/ledger_v2/block-explorer/#delegating-stake-to-a-validator).

8. Vote on at least one governance proposal.

## Technical Track

Anyone interested in developing agents or operating a validator node should follow these steps:

1. Obtain a working copy of the ledger v0.2.x software by [checking out and building](/ledger_v2/building/) it from source.

2. Import a private key from [AW-1](./quickstart-aw1.md) into the `fetchcli` following these [instructions](/ledger_v2/cli-keys/#importing-a-private-key-generated-from-the-agent-framework).

    - You can check the balance of your account by typing `fetchcli query account <YOUR_ACCOUNT_ADDRESS>` where `<YOUR_ACCOUNT_ADDRESS>` is in bech32 format and contains a `fetch1...` prefix. Check out the [documentation](/ledger_v2/cli-keys/) for extra information

3. Delegate some of your stake to the one of the existing validators that are running following these [instructions](/ledger_v2/governance/#stake-delegation). The full list of validators can be found [on the block explorer](https://explore-agentworld.prod.fetch-ai.com/validators) but the table at the bottom of this page shows these for convenience.

4. Vote on at least one governance proposal following these [instructions](/ledger_v2/governance/#voting-on-a-proposal).


| Validator | Operator Address |
| --------- | --------------------------------------------------- |
| Bond      | fetchvaloper1cct4fhhksplu9m9wjljuthjqhjj93z0s97p3g7 |
| Bourne    | fetchvaloper12xd8rgp2u0cwp8lnj2ndulpzad3y9m9f2r8lsx |
| Hunt      | fetchvaloper1vf5wsxjkmjk4uv3nm2zjplw0y2f96rsjw8k7gv |
| Powers    | fetchvaloper108hhutnylgz09acca2ljde8dp6huhsu67hn8v7 |
