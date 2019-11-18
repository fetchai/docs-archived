<h1>Introduction to synergetic contracts</h1>

Synergetic contracts are a new type of smart contract which allow miners to use their computational power to solve useful problems and earn a reward.

Anyone can register a problem on the ledger by creating a synergetic contract and inviting miners to solve it.

All attempts at solving the problem form a Directed Acyclic Graph (DAG).

The type of problems that synergetic contracts can solve are complex optimisation problems such as <a href="https://www.ijstr.org/final-print/aug2018/The-Optimized-Algorithm-For-Prioritizing-And-Scheduling-Of-Patient-Appointment-At-A-Health-Center-According-To-The-Highest-Rating-In-Waiting-Queue.pdf" target=_blank>scheduling patient appointments</a> and <a href="https://en.wikipedia.org/wiki/Protein_folding" target=_blank>protein folding</a>.

<center>![Synergetic contract flow](img/synergetic_contracts.png)</center>

A miner registers as a participant of the synergetic contract and starts calculating towards the problem solution from a random seed generated from a public key. It is a trial and error approach like proof of work.

Registered miners begin to solve the problem **at the same time** and the miner who solves the problem first wins the bounty associated with the problem.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>The winning miner is not necessarily the miner who verifies the block.</p>
</div>

<br/>
