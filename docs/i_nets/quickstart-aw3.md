## Introduction: Agent World 3 (AW-3) - part 3, "Many agents interacting"

Agent World 3 (AW-3) is the third part of our agent-themed incentivised testnet. During this part, It allows anyone with FET tokens to gain additional FET by re-using and adapting agents from AW-2 in order to further grow the useful population of agents. This is open to a broader range of developers, including those just starting out: it's __always__ easier to modify an existing agent than create a new one, and AW-3 makes available all the agents from AW-2 for all to work with via the agent registry.


## Rewards

The following table shows the incentive rewards on offer.

Leaderboard Rank | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
---------------------- | -------------------------- | ------------------------- | ----------------------------
1  | variable from trade        | 1500                      | n/a
2                 | variable from trade        | 500                       | n/a
3                 | variable from trade        | 500                       | n/a
4.-10.            | variable from trade        | 500                       | n/a


Special category | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
---------------------- | -------------------------- | ------------------------- | ----------------------------
Most descriptive AEA registration on SOEF  | variable from trade        | 500                       | 10
Most individual agents trading  | variable from trade        | 500                       | 10


Fetch.ai reserve the right to increase the award pool for AW-3 to reward additional agent developers, or to award specific spot rewards to particularly innovative creations.

## How to qualify for incentive rewards?

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>You must complete <a href="../quickstart-aw1">AW-1</a> before continuing!</p>
</div>

You have to complete a few steps as listed below:

1. Make sure you use the latest AEA framework version <a href="https://img.shields.io/pypi/v/aea" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/aea" /></a>. To upgrade from an older version use `pip install --upgrade aea[all]`. Then upgrade your AEA using `aea upgrade` from within the project or follow the instructions <a href="../../aea/upgrading" target="_blank">here</a>.

2. Fetch a seller AEA built during AW-2 from the AEA-registry and give it a suitable name:

	- Run `aea fetch PUBLIC_ID --alias YOUR_AEA_NAME`, where `YOUR_AEA_NAME` is replaced with a name of your choice.
	- After fetching it, enter the project: `cd YOUR_AEA_NAME`
	- Then install its third-party dependencies: `aea install`

	You can take any PUBLIC_ID from the following list. We did not verify the individual projects and take no responsibility for them working. (You have the option to complete your own following the <a href="../quickstart-aw1">AW-2 guide</a>.)

	Public ID             |
	----------------------|
	TBD on Monday 23rd Nov|


3. Configure or customize the AEA. The following requirements must be satisfied (same as AW-2) for the seller AEA:

	- Agent must sell data offered by some public API. The data must be related to mobility or weather.
	- Agent must sell data following the fipa protocol (`fetchai/fipa`) and advertise it using oef search protocol (`fetchai/oef_search`) on the SOEF (advertisement must include correct classification and public id of agent)
	- Payment must be via a simple transfer on the incentivized testnet

4. Run agent and sell as much data to one of our buyer agents as possible.

	- Fetch.ai's buyer agents occur randomly in one of the following locations and at random times throughout the competition.

	City                 | Latitude  | Longitude
	---------------------- | -------------------------- | -------------------------
	Berlin  | 52.5200     | 13.4050
	London  | 51.5074     | -0.1278
	San Francisco  | 37.7749     | -122.4194
	Shanghai  | 31.2304     | 121.4737
	Rome | 41.9028 | 12.4964
	Rio De Janeiro | -22.9068 | -43.1729
	Sydney | -33.8688 | 151.2093
	Delhi | 28.7041 | 77.1025
	Tokyo | 35.6762 | 139.6503
	Mexico City | 19.4326 | -99.1332
	Cairo | 30.0444 | 31.2357
	Kinshasa | - 4.4419 | 15.2663

	- The buyer agents only purchase from registered agents (see <a href="../quickstart-aw1">AW-1</a>). The buyer agents only purchase from agents which follow the requirements in step 3.

	- The buyer agents update the <a href="" target="_blank">leaderboard (not open yet)</a> regularly. The leaderboard determines the winning developer (see table above).


5. Submit prize claim form <a href="" target="_blank">here (not open yet)</a>.


6. Optionally, provide feedback on AW-2 to improve the AEA framework and the Agent World incentivized testnet programme.

	- Please <a href="" target="_blank">complete our survey here (not open yet)</a>.

