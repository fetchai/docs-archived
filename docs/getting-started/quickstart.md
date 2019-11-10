<h1>Quick, start!</h1>
Fetch.ai is a platform for decentralised autonomous agents to work, it's a platform that enables machine learning from the consensus design through to applications in Etch. 

This quickstart quide is to get you moving as quickly as possible. Let's get started, anything we miss will be highlighted for you to deep dive on later.

Running a node locally:

This is a great way to test Etch code locally and view what a node is doing; you can connect to the testnet or just run as a single node. 

Let's do that. You're going to need to clone the fetch.ai ledger repo:
``` bash
cd [working_directory]
git clone https://github.com/fetchai/ledger.git
git checkout release/v0.9.x
```

Update and initialise submodules from the repository root directory:

``` bash
cd ledger
git pull
git submodule update --init --recursive
```

For more detailed instructions, including helpful tips if you're running into errors head here. 

<h3>Install the Python Ledger API</h3>


If you want to develop Smart Contracts and deploy them, or create apps to connect directly to the ledger, the Python Ledger API is your best friend. 


<br/>