## Introduction: Agent World 2 (AW-2) - part 2, "My first own agent"

Agent World 2 (AW-2) is the second part of our agent-themed incentivised testnet. During this part, It allows anyone with FET tokens to gain additional FET by building agents to represent **mobility** and **climate/weather** related agents in key cities around the world, such as Berlin, London, San Francisco and Shanghai. The world is full of web based APIs for collecting this data, and the <a href="../../aea">agent framework</a> supports HTTP connections to these.

## Rewards

The following table shows the incentive rewards on offer.

Action             | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
------------------ | -------------------------- | ------------------------- | ----------------------------
Steps 1 - 11 below | 100                        | 250                       | 150
Tweet              | 0                          | 50                        | 100

## How to qualify for incentive rewards?

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>You must complete <a href="../quickstart-aw2">AW-1</a> before continuing!</p>
</div>

You have to complete a few steps as listed below:

1. Make sure you use the latest AEA framework version <a href="https://img.shields.io/pypi/v/aea" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/aea" /></a>. To upgrade, follow the instructions <a href="../../aea/version" target="_blank">here</a>.

2. Fetch the `template_seller_aw2` AEA from the AEA-registry and give it a suitable name:

	- Run `aea fetch fetchai/template_seller_aw2 --alias YOUR_AEA_NAME`, where `YOUR_AEA_NAME` is replaced with a name of your choice.
	- After fetching it, enter the project: `cd YOUR_AEA_NAME`

3. Eject the `simple_seller` and `simple_data_request` skills to edit it:

	- Run `aea skill eject fetchai/template_seller` and `aea skill eject fetchai/simple_data_request`

4. Customize the `simple_seller` skill (in `YOUR_AGENT_NAME/skills/simple_seller`) and the `simple_data_request` skill (in `YOUR_AGENT_NAME/skills/simple_data_request`) to satisfy the following requirements (you may optionally customize other components of the AEA as well):

	- The AEA must sell data offered by a public API which provides data on mobility or weather in either one of Berlin (Germany), London (UK), San Francisco (USA) or Shanghai (China). You can customize the `simple_data_request` skill to satisfy this requirement.
	- The AEA must negotiate the terms using the fipa protocol (`fetchai/fipa`) and advertise it using oef search protocol (`fetchai/oef_search`) on the SOEF. You can customize the `simple_seller` skill to satisfy this requirment.
	- The advertisement must include the correct classification and a reference to AW-2. You can customize the `simple_seller` skill to satisfy this requirment.
	- Payment must be via a simple transfer on the incentivized testnet. You can customize the `simple_seller` skill to satisfy this requirment.

	let's make this easy: basically http request data from behaviour, handle the data and save in shared context, buyer skill simply takes data from shared context and sells it via fipa. So all they need to do: define end point to get data from, properly parse data, properly configure agent

5. Run the AEA for several hours and sell data at least twice successfully.

	- A buyer AEA is continuously checking the SOEF for data to purchase. The buyer AEA will purchase once immediately and then again after a few hours.
	- If the initial sale does not go through your AEA is incorrectly implemented. Stop it, fix it and try again.
	o you need to run your AEA long enough.
	- If the initial sale does go through let the AEA run until the second sale has concluded.
	- The buyer AEA only purchases from AEAs which implement all the requirements listed under 4.

6. Once your AEA has successfully sold data twice, stop it and upload it to the AEA-registry:

	- Change the author in the `aea-config.yaml` to your author handle (run `aea init` to see what it is).
	- Change the agent name in `aea-config.yaml` to a name of your choice.
	- Run `aea publish` from within the AEA project. You might first have to push the skills you have developed with `aea push skill PUBLIC_ID`.

7. Optionally, provide feedback on AW-2 to improve the AEA framework and the Agent World incentivized testnet programme.

8. Extra: Fetch the `simple_buyer_aw2` AEA (`aea fetch fetchai/simple_buyer_aw2`) from the AEA-registry and extend it to be a buyer for the above use-case. Then push it to the AEA-registry. (There is no need to run it at this point.)


More checks on pushing
