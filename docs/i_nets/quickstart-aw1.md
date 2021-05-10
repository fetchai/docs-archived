
## Introduction: Agent World 1 (AW-1) - part 1, getting started

<div class="admonition error">
  <p class="admonition-title">Note</p>
  <p>AW-1 has finished now! You won't be able to complete the guide or earn rewards.</p>
</div>

Agent World 1 (AW-1) is the first part of our agent-themed incentivised testnet. It allows anyone with <a href="https://fetch.ai/staking/" target="_blank">a non-zero amount of staked FET</a> tokens to gain some more FET token rewards by following a few simple steps and launching an agent on Agent World. In this first two week part, we get everyone up and running with the a <a href="../../aea" target="_blank">agent framework</a>.


## Rewards

The following table shows the incentive rewards on offer.

Action             | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
------------------ | -------------------------- | ------------------------- | ----------------------------
Steps 1 - 11 below | 100                        | 250                       | 150
Tweet              | 0                          | 50                        | 100


## How to qualify for incentive rewards?

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>You must stake ERC20 FET tokens in order to take part and qualify. Go to <a href="https://fetch.ai/staking/" target="_blank">staking</a>, the process is simple and quick!</p>
</div>

You have to complete a few steps as listed below:

1. Join our discord channel <a href="https://discord.gg/UDzpBFa" target="_blank">here</a>. This allows you to ask questions throughout AW-1 and engage with the Fetch.ai developers.

2. Download and install the AEA (Autonomous Economic Agent) Framework including its CLI on your own machine. There are three ways to do this:

	- Direct:

		- Ensure you have <a href="https://www.python.org/downloads/" target="_blank">Python (3.6, 3.7 or 3.8)</a>  and <a href="https://golang.org/dl/" target="_blank">Go (>= 1.14.2)</a> installed on your machine.
		- Run `pip install aea[all]` to install the framework.
		- Ensure you have the latest version <a href="https://img.shields.io/pypi/v/aea" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/aea" /></a> installed by executing `aea --version`. To upgrade from an older version use `pip install --upgrade aea[all]`.
		- For more guidance (in particular Windows and Ubuntu related issues) check out the <a href="../../aea/quickstart/#known-issues">AEA quickstart's known issues section</a>

	- Docker:

		- We provide a Docker image with all the needed dependencies. To use the image you will first have to pull it and than run it with your current local directory mounted as a Docker volume. This allows you to keep your agents local while working on them from within the Docker container.
		- To pull `docker pull fetchai/aea-user:latest`
		- To run the image:
			- Linux and MacOs: `docker run -it -v $(pwd):/agents --workdir=/agents fetchai/aea-user:latest`
			- Windows: `docker run -it -v %cd%:/agents --workdir=/agents fetchai/aea-user:latest`
		- Once successfully logged into the Docker container, you can follow the rest of the guide the same way as if not using Docker and step Direct above.

	- Automated:

		- Get <a href="https://github.com/fetchai/agents-aea/tree/master/scripts/install.ps1" target="_blank">this script for Windows</a> or <a href="https://github.com/fetchai/agents-aea/tree/master/scripts/install.sh" target="_blank">this script for MacOs/Ubuntu</a> and run it on your machine. The script will install the required dependencies and the framework.

3. Create a developer account using the command below. This will enable you to download and contribute to the <a href="https://aea-registry.fetch.ai" target="_blank">AEA Registry</a>; the package manager for AEA components.

	- Simply run `aea init` and follow the steps as prompted. In the process you will set an author name; this is your **developer handle**.
	- Typing `aea` at the command prompt will give you a list of commands that are available.

4. Fetch the registration agent from AEA Registry via CLI:

	- Run `aea fetch fetchai/registration_aea_aw1`
	- Enter it `cd registration_aea_aw1`
	- Install dependencies via `aea install`
	- Build its components via `aea build`

5. Create a test-net address for the registration agent via CLI:

	- Run `aea generate-key fetchai` and `aea add-key fetchai` to generate and add a key pair for your AEA to transact with. Then run `aea generate-key fetchai fetchai_connection_private_key.txt` and `aea add-key fetchai fetchai_connection_private_key.txt --connection` to add a key pair for your AEA to secure its communications with. Now associate both with `aea issue-certificates`.
	- Print your address for transacting `aea get-address fetchai`

6. Sign the test-net address you just generated with the private key tied to your FET account on Ethereum mainnet. This is the account you use for FET staking:

	- We recommend you use our <a href=https://fetchai.github.io/web-ethereum-signer/ target="_blank">signing app</a> with your <a href="https://docs.metamask.io/guide/signing-data.html#a-brief-history" target="_blank">MetaMask</a> wallet, alternatively use <a href="https://www.myetherwallet.com/interface/sign-message" target="_blank">MEW</a> or a similar wallet to sign your Fetch.ai test-net address.
	- In your registration agent's `aea-config.yaml` file update the following lines:

		- `ethereum_address: PUT_YOUR_ETHEREUM_ADDRESS_HERE`
		- `signature_of_fetchai_address: PUT_YOUR_SIGNATURE_HERE`
		- `whitelist: [PUT_WHITELIST_ADDRESSES_HERE]` (In this challenge, this variable should be set to: `fetch1a3ecdm538yt4xlz6kc39xf0h3syge0mlrr0jgf`.)

	<div class="admonition note">
	  <p class="admonition-title">Note</p>
	  <p>Make sure you put strings (addresses and signatures) in quotes `''`.</p>
	</div>

7.  Configure the registration agent further, to include your developer handle. Optionally, to earn more tokens, also provide a link to a tweet. To qualify, the tweet must reference your developer handle and link to incentivized [testnet landing page](../).

	- In your registration agent's `aea-config.yaml` file add the following lines:

		- `developer_handle: PUT_YOUR_DEVELOPER_HANDLE_HERE`
		- `tweet: PUT_THE_LINK_TO_YOUR_TWEET_HERE`

	- The developer handle needs to be updated in two places!  (You can search the file for the `PUT_YOUR_DEVELOPER_HANDLE_HERE` placeholder).

8. Now, you can run your registration agent which registers the agent and the provided data on the <a href="../../aea/oef-ledger">SOEF</a> and with the confirmation agent:

	- Execute `aea run`

9. After a while, when you see `received register message success`, you can stop (by pressing `Ctrl-C`) the agent.

	- You can look for your transfer on the <a href="https://explore-agentworld.prod.fetch-ai.com" target="_blank">block explorer</a>.

	<div class="admonition note">
	  <p class="admonition-title">Note</p>
	  <p>If after some time (>1 min) you get no response or the response is an error, then please make sure you have followed steps 6. and 7. correctly and that you have funds staked!</p>
	</div>

10. You can verify that you have received funds on the test-net in AEA's wallet:

	- Execute `aea get-wealth fetchai` to see your test-net wealth

11. Use the CLI to send some funds from your registration agent to the whitelist adddress:

    - `aea transfer fetchai fetch1a3ecdm538yt4xlz6kc39xf0h3syge0mlrr0jgf 10`

At this point you are done!

We would really value your feedback. Please <a href="https://research.typeform.com/to/gFWEY0Sk" target="_blank">complete our survey here</a>.
