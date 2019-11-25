# Machine Learning

Fetch.ai has developed a machine learning library is a generalised toolkit for building and running this type of applications on distributed ledger nodes. This means neural networks can be trained and run on or off chain depending on what is needed for your application. Machine learning operations are implemented in the Etch language, used to write smart contracts native to the Fetch.ai platform.

Like PyTorch and TensorFlow, the library is focused on neural networks and deep learning. But in contrast with them, it is compatible with Etch `FixedPoint` data types and Tensors built with them. These data types implement integer mathematics, wich make possible to compute precise results of complex mathematical operations (in line with deep neural networks requirements) on different architectures with guaranteed identical results.

If you're new to the Etch language, used to write smart contracts native to the Fetch.ai platform,
<a href="/machine-learning/basic-etch-example" target=_blank>this etch example</a> demonstrates how to train and run a neural network.
This can be useful for trying out ideas, or simply using the Fetch.ai machine learning library for standalone applications.

To extending this further we need to understand how to train or run a neural net on-chain. 
<a href="/machine-learning/smart-contract-example" target=_blank>This smart contract example </a> demonstrates how to rework this neural network to train and run on chain.

Finally, <a href="/machine-learning/synergetic-contract-example" target=_blank>this synergetic contract example</a> covers synergetic contracts; this is useful for coordinating between on-chain and off-chain work.
This is great for executing expensive computations off-chain but coordinating/managing the work on-chain. 
