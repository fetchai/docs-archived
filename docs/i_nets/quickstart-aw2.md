## Introduction: Agent World 2 (AW-2) - part 2, "My first own agent"

<div class="admonition error">
  <p class="admonition-title">Note</p>
  <p>AW-2 has finished now! You won't be able to complete the guide or earn rewards.</p>
</div>

Agent World 2 (AW-2) is the second part of our agent-themed incentivised testnet. During this part, it allows anyone with FET tokens to gain additional FET by building agents to represent **mobility** and **climate/weather** related agents in key cities around the world, such as Berlin, London, San Francisco and Shanghai. The world is full of web based APIs for collecting this data, and the <a href="../../aea">agent framework</a> supports HTTP connections to these.

## Rewards

The following table shows the incentive rewards on offer.

Action                 | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
---------------------- | -------------------------- | ------------------------- | ----------------------------
Steps 1 - 7, 10 below  | variable from trade        | 1500                      | 60
Step 9                 | variable from trade        | 500                       | 60

Fetch.ai reserve the right to increase the award pool for AW-2 to reward additional agent developers, or to award specific spot rewards to particularly innovative creations.

## How to qualify for incentive rewards?

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>You must complete <a href="../quickstart-aw1">AW-1</a> before continuing!</p>
</div>

You have to complete a few steps as listed below:

1. Make sure you use the latest AEA framework version <a href="https://img.shields.io/pypi/v/aea" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/aea" /></a>. To upgrade from an older version use `pip install --upgrade aea[all]`. Then upgrade your AEA using `aea upgrade` from within the project or follow the instructions <a href="../../aea/upgrading" target="_blank">here</a>.

2. Fetch the `simple_seller_aw2` AEA from the AEA-registry and give it a suitable name:

	- Run `aea fetch fetchai/simple_seller_aw2 --alias YOUR_AEA_NAME`, where `YOUR_AEA_NAME` is replaced with a name of your choice.
	- After fetching it, enter the project: `cd YOUR_AEA_NAME`
	- Then install its third-party dependencies: `aea install`

3. Eject the `simple_seller` and `simple_data_request` skills so you can edit them:

	- Run `aea eject skill fetchai/simple_seller`, which will eject the skill from the `vendor` folder to the `skills` folder where you can edit it.
	- Then, run `aea eject skill fetchai/simple_data_request`, which will eject this skill too.

4. Ensure you use the private key from AW1.

	- Generate a new key and add it to the AEA: `aea generate-key fetchai` and `aea add-key fetchai`
	- Manually replace the private key you just generated in `fetchai_private_key.txt` with the one from AW-1.
	- Check everything works by running `aea get-address fetchai` and confirming that the address matches the one you hold Agent World funds on.
	- (This can be done by viewing the address on the <a href="https://explore-agentworld.prod.fetch-ai.com" target="_blank">block explorer</a> or by typing `aea get-wealth fetchai`).

5. Create a proof of representation for communication on the <a href="../../aea/acn">ACN</a>:

	- Run `aea generate-key fetchai fetchai_connection_private_key.txt` and `aea add-key fetchai fetchai_connection_private_key.txt --connection` to add a key pair for your AEA to secure its communications with. Now associate this key pair with the one you use for transacting by executing `aea issue-certificates`.

6. Customize the `simple_seller` skill (in `YOUR_AGENT_NAME/skills/simple_seller`) and the `simple_data_request` skill (in `YOUR_AGENT_NAME/skills/simple_data_request`) to satisfy the following requirements (you may optionally customize other components of the AEA as well):

	- The AEA must sell data offered by a public API which provides data on mobility or weather in the vicinity of either one of Berlin (Germany) [`latitude: 52.5200, longitude: 13.4050`], London (UK) [`latitude: 51.5074, longitude: -0.1278`], San Francisco (USA) [`latitude: 37.7749, longitude: -122.4194`] or Shanghai (China) [`latitude: 31.2304, longitude: 121.4737`]. Your AEA must be located in a radius no further than `50 km` from the geo locations specified. You can customize the `simple_data_request` and `simple_seller` skills to satisfy this requirement.
	- The AEA must request data from a public API. You can customize the `simple_data_request` skill to satisfy this requirement. You must configure the fields `method`, `url` and potentially `body` in the behaviours section and the field `shared_state_key` in the handlers section of the `fetchai/simple_data_request` skill on `aea-config.yaml`.
	- The AEA must negotiate the terms using the fipa protocol (`fetchai/fipa`) and advertise it using oef search protocol (`fetchai/oef_search`) on the SOEF. You can customize the `simple_seller` skill to satisfy this requirment (by default it is already satisfied).
	- The advertisement must include the correct service key (`seller_service`) and value (one of `weather_data` or `mobility_data`, depending on the data your agent is offering). You can customize the `simple_seller` skill to satisfy this requirement.
	- Payment must be via a simple transfer on the incentivized testnet. You can customize the `simple_seller` skill to satisfy this requirment (by default this is already the case).
	- The `shared_state_key` specified for the `fetchai/simple_seller` skill in `aea-config.yaml` must match the one specified for the `fetchai/simple_data_request` and not be `null`.

	<div class="admonition note">
	  <p class="admonition-title">Note</p>
	  <p>To succeed, please consult the documentation on the <a href="../../aea">agent framework</a> and discuss in Discord.</p>
	</div>

<!-- 	<div class="admonition note">
	  <p class="admonition-title">Note</p>
	  <p>If you have connectivity issues with the agent communication network, try changing the entry peer in the `aea-config.yaml` to `entry_peers:
  - /dns4/agents-p2p-dht.prod.fetch-ai.com/tcp/9001/p2p/16Uiu2HAmVWnopQAqq4pniYLw44VRvYxBUoRHqjz1Hh2SoCyjbyRW`.</p>
	</div> -->

7. Run the AEA for several hours and sell data at least twice successfully.

	- A set of buyer AEAs is continuously checking the SOEF for data to purchase. The buyer AEAs will purchase once immediately and then again after several hours.
	- If the initial sale does not go through, your AEA is incorrectly implemented. Stop it, fix it and try again.
	- If the initial sale does go through let the AEA run until the second sale has concluded.
	- The buyer AEA only purchases from AEAs which implement all the requirements listed under 5.

8. Once your AEA has successfully sold data twice, stop it and upload it to the AEA-registry:

	- Change the author in the `aea-config.yaml` to your author handle (run `aea init` to see what it is).
	- Run `aea publish --remote` from within the AEA project. You might first have to push the skills you have developed with `aea push skill PUBLIC_ID`.

9. Optionally, provide feedback on AW-2 to improve the AEA framework and the Agent World incentivized testnet programme.

	- Please <a href="https://research.typeform.com/to/vPqWIzcw" target="_blank">complete our survey here</a>.

10. Extra: create a buyer AEA yourself!

	- Fetch the `simple_buyer_aw2` AEA (`aea fetch fetchai/simple_buyer_aw2`) from the AEA-registry and extend it to be a buyer for the above use-case. Then push it to the AEA-registry. (There is no need to run it at this point.)

11. Fill in the following form, providing your developer handle and uploaded AEAs:

	- Complete <a href="https://forms.gle/NDWECUsBRvr8zuL27" target="_blank">this form</a>.
