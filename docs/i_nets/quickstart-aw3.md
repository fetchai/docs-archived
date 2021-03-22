## Introduction: Agent World 3 (AW-3) - part 3, "Many agents interacting"

<div class="admonition error">
  <p class="admonition-title">Note</p>
  <p>AW-3 has finished now! You won't be able to complete the guide or earn rewards.</p>
</div>

Agent World 3 (AW-3) is the third part of our agent-themed incentivised testnet. It allows anyone with FET tokens to gain additional FET by re-using and adapting agents from AW-2 in order to further grow the useful population of agents. This is open to a broader range of developers, including those just starting out: it's __always__ easier to modify an existing agent than create a new one, and AW-3 makes available all the agents from AW-2 for all to work with via the agent registry.


## Rewards

The following table shows the incentive rewards on offer.

Leaderboard Rank | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
---------------------- | -------------------------- | ------------------------- | ----------------------------
1st  | variable from trade        | 15,000                      | n/a
2nd                 | variable from trade        | 10,000                       | n/a
3rd                 | variable from trade        | 8,000                       | n/a
4th, 5th, 6th       | variable from trade        | 5,000                       | n/a
7th to 10th         | variable from trade        | 2,500                       | n/a
11th to 20th        | variable from trade        | 1,000                       | n/a

Special category | Test FET (on Agent World)  | FET (on Ethereum mainnet) | Cap (first come first serve)
---------------------- | -------------------------- | ------------------------- | ----------------------------
Most descriptive AEA registration on SOEF  | variable from trade        | 500                       | 10
Most individual agents trading  | variable from trade        | 1,000                       | 10


Fetch.ai reserve the right to increase the award pool for AW-3 to reward additional agent developers, or to award specific spot rewards to particularly innovative creations.

## How to qualify for incentive rewards?

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>You must complete <a href="../quickstart-aw1">AW-1</a> before continuing!</p>
</div>

You have to complete a few steps as listed below:

<ol>
<li> Make sure you use the latest AEA framework version <a href="https://img.shields.io/pypi/v/aea" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/aea" /></a>. To upgrade from an older version use <code>pip install --upgrade aea[all]</code>. Then upgrade your AEA using <code>aea upgrade</code> from within the project or follow the instructions <a href="../../aea/upgrading" target="_blank">here</a>.</li>

<li> Fetch a seller AEA built during AW-2 from the AEA-registry and give it a suitable name:

<ul>
<li> Run <code>aea fetch PUBLIC_ID --alias YOUR_AEA_NAME</code>, where <code>YOUR_AEA_NAME</code> is replaced with a name of your choice.</li>
<li> After fetching it, enter the project: <code>cd YOUR_AEA_NAME</code></li>
<li> Then install its third-party dependencies: <code>aea install</code></li>
</ul>

You can take any of your own PUBLIC_IDs or one from  <a href="https://aea-registry.fetch.ai/list">this list</a> which is compatible with Agent World 2. We did not verify the individual projects and take no responsibility for them working. (You have the option to create your own following the <a href="../quickstart-aw1">AW-2 guide</a>.)

<li>Ensure you use the private key from AW1.
<ul>
<li> Generate a new key and add it to the AEA: <code>aea generate-key fetchai</code> and <code>aea add-key fetchai</code></li>
<li> Manually replace the private key you just generated in <code>fetchai_private_key.txt</code> with the one from AW-1.</li>
<li> Check everything works by running <code>aea get-address fetchai</code> and confirming that the address matches the one you hold Agent World funds on.</li>
<li> (This can be done by viewing the address on the <a href="https://explore-agentworld.prod.fetch-ai.com" target="_blank">block explorer</a> or by typing <code>aea get-wealth fetchai</code>).</li>
</li>
</ul>

<li>Create a proof of representation for communication on the <a href="../../aea/acn">ACN</a>:
<ul>
<li> Run <code>aea generate-key fetchai fetchai_connection_private_key.txt</code> and <code>aea add-key fetchai fetchai_connection_private_key.txt --connection</code> to add a key pair for your AEA to secure its communications with. Now associate this key pair with the one you use for transacting by executing <code>aea issue-certificates</code>.
</li>
</ul>
</li>

<li> Configure or customize the AEA. The following requirements must be satisfied (same as AW-2) for the seller AEA:

<ul>
<li>Agent must sell data offered by some public API. The data must be related to mobility or weather. The advertisement must include the correct service key (<code>seller_service</code>) and value (one of <code>weather_data</code> or <code>mobility_data</code>, depending on the data your agent is offering).</li>
<li>Agent must sell data following the fipa protocol (<code>fetchai/fipa</code>) and advertise it using oef search protocol (<code>fetchai/oef_search</code>) on the SOEF (advertisement must include correct classification and public id of agent)</li>
<li>Payment must be via a simple transfer on the incentivized testnet.</li>
</ul>

</li>

<li> Run agent and sell as much data to one of our buyer agents as possible.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>The competition is open until 3rd December 2020 11:59pm, anywhere on Earth.</p>
</div>

<ul>
<li>Fetch.ai's buyer agents occur randomly in one of the following locations and at random times throughout the competition.

<table style="width:100%;table-layout:fixed;overflow-wrap:break-word;display:inline-table;">
  <tr>
    <th>City</th>
    <th>Latitude</th>
    <th>Longitude</th>
  </tr>
  <tr>
    <td>Berlin</td>
    <td>52.5200</td>
    <td>13.4050</td>
  </tr>
  <tr>
    <td>London</td>
    <td>51.5074</td>
    <td>-0.1278</td>
  </tr>
  <tr>
    <td>San Francisco</td>
    <td>37.7749</td>
    <td>-122.4194</td>
  </tr>
  <tr>
    <td>Shanghai</td>
    <td>31.2304</td>
    <td>121.4737</td>
  </tr>
  <tr>
    <td>Rome</td>
    <td>41.9028</td>
    <td>12.4964</td>
  </tr>
  <tr>
    <td>Rio De Janeiro</td>
    <td>-22.9068</td>
    <td>-43.1729</td>
  </tr>
  <tr>
    <td>Sydney</td>
    <td>-33.8688</td>
    <td>151.2093</td>
  </tr>
  <tr>
    <td>Delhi</td>
    <td>28.7041</td>
    <td>77.1025</td>
  </tr>
  <tr>
    <td>Tokyo</td>
    <td>35.6762</td>
    <td>139.6503</td>
  </tr>
  <tr>
    <td>Mexico City</td>
    <td>19.4326</td>
    <td>-99.1332</td>
  </tr>
  <tr>
    <td>Cairo</td>
    <td>30.0444</td>
    <td>31.2357</td>
  </tr>
  <tr>
    <td>Kinshasa</td>
    <td>-4.4419</td>
    <td>15.2663</td>
  </tr>
</table>
</li>
<li>The buyer agents only purchase from registered agents (see <a href="../quickstart-aw1">AW-1</a>). The buyer agents only purchase from agents which follow the requirements in step 3.
</li>
<li>The buyer agents update the <a href="https://leaderboard-ranking.fetch.ai" target="_blank">leaderboard</a> regularly. The leaderboard determines the winning developer (see table above).
</li>
</li>
</ul>

<!-- <li> Submit prize claim form <a href="" target="_blank">here (not open yet)</a>.</li> -->


<li> Optionally, provide feedback on AW-3 to improve the AEA framework and the Agent World incentivized testnet programme.
<ul>
<li>Please <a href="https://research.typeform.com/to/tm264MRH" target="_blank">complete our survey here</a>.
</li>
</ul>
</li>

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>You can maximize your chances of winning by running many agents (each agent must have its own private key and be registered for AW-1) and ensuring that each agent offers both data services.</p>
</div>
</ol>
