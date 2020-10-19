
## Intro 

Agent World 1 (AW-1) is our first incentivized testnet. It allows anyone with FET tokens to gain some more FET token rewards by following a few simple steps and launching an agent on Agent World 1.

## How to win tokens?

You have to complete a few steps as listed below:

1. Join our discord channel [here](https://discord.gg/TdRhuE). This allows you to ask questions throughout AW-1 and engage with the Fetch.ai developers.

2. Download and install the AEA (Autonomous Economic Agent) Framework including its CLI on your own machine. There are two ways to do this:

	- Manual:
		- ensure you have Python (3.6, 3.7 or 3.8) installed on your machine
		- `pip install aea[all]`
		- ensure you have the latest version `0.7.0` installed by executing `aea --version`

	- Automated:
		- get [this]() script and run it on your machine

3. Create a developer account on the [AEA Registry](https://aea-registry.fetch.ai), the package manager for AEA components.

	- Simply run `aea init` and follow the steps as prompted.

4. Fetch the registration agent from AEA Registry via CLI:

	- Run `aea fetch fetchai/my_registration_aea`
	- Enter it `cd my_registration_aea`

5. Create a test-net address for the registration agent via CLI:

	- Run `aea generate-key fetchai` and `aea add-key fetchai`

6. Register your ethereum address which is tied to your FET account against the test-net address you just generated:

	- In your registration agent's `aea-config.yaml` file add the following lines:

``` yaml
ethereum_address: PUT_YOUR_ETHEREUM_ADDRESS_HERE
signature_of_fetchai_address: PUT_YOUR_SIGNATURE_HERE
```

(We recommend you use MetaMask to sign your fetchai address)

7.  Configure the registration agent further, to include your developer handle. Optionally, to earn more tokens, also provide a link to a tweet. To qualify, the tweet must reference your developer handle and link to incentivized [testnet landing page](../i_nets/quickstart-aw1/).

	- In your registration agent's `aea-config.yaml` file add the following lines:

``` yaml
developer_handle: PUT_YOUR_DEVELOPER_HANDLE_HERE
tweet: PUT_THE_LINK_TO_YOUR_TWEET_HERE
```

8. Now, you can run your registration agent which registers the agent and the provided data on the SOEF:

	- Execute `aea run`

9. After a while, you can stop the agent.

10. You can verify that you have received funds on the test-net in AEA's wallet:

	- Execute `aea get-wealth fetchai` to see your test-net wealth

11. Use the CLI to send funds from your registration agent to this adddress: `SOME_ADDRESS`

We would really value your feedback. Please fill in [this]() survey to help us improve.

