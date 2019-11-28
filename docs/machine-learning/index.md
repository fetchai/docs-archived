# Machine Learning

Fetch.ai has developed a machine learning library that is a generalised toolkit for building and running these type of applications on distributed ledger nodes. This means neural networks can be trained and run on or off chain depending on what is needed for your application. Machine learning operations may be invoked with the Etch language, used to write smart contracts native to the Fetch.ai platform.

Like PyTorch and TensorFlow the library focuses on building, training, and running computational graphs, in order to implement neural networks for deep learning. In contrast with these frameworks, the Fetch.ai machine learning library is fully compatible with integer mathematics, implemented with Etch `FixedPoint` data types (and Tensors containing them). As a result, every neural network and complex mathematical operation in the library will produce numerically identical results across any hardware and software architecture. This means that every machine learning operation taking place on the ledger will be verifiable by every other node in the network.

If you are new to Etch, the language used to write smart contracts native to the Fetch.ai platform, [the quickstart section](/getting-started/quickstart#training-a-neural-network) demonstrates how to train and run a neural network. This can be useful for trying out ideas, or simply using the Fetch.ai machine learning library for standalone applications.

To extend this further we need to understand how to train or run a neural net on-chain. [This smart contract example](/machine-learning/smart-contract-example) demonstrates how to rework this neural network to train and run on chain.

Finally, [this synergetic contract example](/machine-learning/synergetic-contract-example) covers synergetic contracts; this is useful for coordinating between on-chain and off-chain work. This is great for executing expensive computations off-chain but coordinating/managing the work on-chain.
