
## Intro 

Agent World 1 (AW-1) is our first incentivized testnet. It allows anyone with FET tokens to gain some more FET token rewards by following a few simple steps and launching an agent on Agent World 1.

## How to win tokens?

You have to complete a few steps as listed below:

1. Join our discord channel <a href="https://discord.gg/UDzpBFa" target="_blank">here</a>. This allows you to ask questions throughout AW-1 and engage with the Fetch.ai developers.

2. Download and install the AEA (Autonomous Economic Agent) Framework including its CLI on your own machine. There are two ways to do this:

	- Manual:
		- ensure you have Python (3.6, 3.7 or 3.8) installed on your machine
		- `pip install aea[all]`
		- ensure you have the latest version `0.7.0` installed by executing `aea --version`

	- Automated:
		- get [this script for Windows](https://github.com/fetchai/agents-aea/tree/master/scripts/install.ps1) or [this script for MacOs/Ubuntu](https://github.com/fetchai/agents-aea/tree/master/scripts/install.sh) and run it on your machine

3. Create a developer account on the [AEA Registry](https://aea-registry.fetch.ai), the package manager for AEA components.

	- Simply run `aea init` and follow the steps as prompted.

4. Fetch the registration agent from AEA Registry via CLI:

	- Run `aea fetch fetchai/registration_aea_aw1`
	- Enter it `cd registration_aea_aw1`
	- Install dependencies via `aea install`

5. Create a test-net address for the registration agent via CLI:

	- Run `aea generate-key fetchai` and `aea add-key fetchai`
	- Print your address `aea get-address fetchai`

6. Sign your test-net address you just generated with the private key which is tied to your FET account on Ethereum mainnet which you use for staking FET:

	- We recommend you use MetaMask or a similar Wallet to sign your Fetch.ai test-net address.
	- In your registration agent's `aea-config.yaml` file update the following lines:

	```
	ethereum_address: PUT_YOUR_ETHEREUM_ADDRESS_HERE
	signature_of_fetchai_address: PUT_YOUR_SIGNATURE_HERE
	whitelist: [PUT_WHITELIST_ADDRESSES_HERE]
	```

	- Currently, the whitelisted address is: `fetch19unnpas52q0us5lp7e2pmnkrmywjhnau224yel`

7.  Configure the registration agent further, to include your developer handle. Optionally, to earn more tokens, also provide a link to a tweet. To qualify, the tweet must reference your developer handle and link to incentivized [testnet landing page](../).

	- In your registration agent's `aea-config.yaml` file add the following lines:

	```
	developer_handle: PUT_YOUR_DEVELOPER_HANDLE_HERE
	tweet: PUT_THE_LINK_TO_YOUR_TWEET_HERE
	```

	- The developer handle needs to be updated in two places!

8. Now, you can run your registration agent which registers the agent and the provided data on the SOEF:

	- Execute `aea run`

9. After a while, when you see `received register_msg success`, you can stop the agent.

10. You can verify that you have received funds on the test-net in AEA's wallet:

	- Execute `aea get-wealth fetchai` to see your test-net wealth

11. Use the CLI to send some funds from your registration agent to the whitelist adddress: `fetch19unnpas52q0us5lp7e2pmnkrmywjhnau224yel`

We would really value your feedback. Please fill in [this]() survey to help us improve.

