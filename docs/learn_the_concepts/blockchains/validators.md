# Validators 

The **block validation** procedure is one of the essential elements that makes blockchain functioning possible. 
The block validation procedure used by the two primary blockchain architectures, **Proof-of-Work** (**PoW**) and 
**Proof-of-Stake** (**PoS**), differ noticeably from one another. A network node known as a **blockchain validator** 
assists in processing and validating transaction blocks on the platform so that they may be added to the blockchain's 
permanent ledger. _Validator nodes take on the responsibility of validating, voting on, and keeping a record of 
transactions by taking part in the consensus process_.

## How are blocks validated on the blockchain?

### Validation on Proof-of-Work (PoW) Blockchains 

One of the most prominent blockchain technologies is the **Proof-of-Work** (**PoW**) consensus process, which was 
initially made popular by Bitcoin. **Miners** and the power they need to do the computations required to validate 
transactions are the key elements that distinguish PoW systems. Miners use computer hardware to power network nodes that
use processing power to solve algorithmic mathematical computational puzzles, known as proofs of work. The miner who 
completes the puzzle first validates the blockchain's most recent block of transactions. 

In order to create a reliable record of data for the whole network, the successful miner broadcasts the new block to all 
other nodes, which in turn authenticate its accuracy and add that block to their copies of the blockchain. This 
verification procedure establishes consensus. A new block cannot be added to the network until this data has been 
verified. When a miner validates a new block of data this latter one is then added to the PoW blockchain, with 
**the first miner completing the validation process being rewarded with newly created cryptocurrency**, known as the 
**block reward** (e.g. in the case of Bitcoin, block rewards are in terms of BTC).

Proof-of-Work Blockchains seek to generate blocks at regular intervals. PoW networks are constrained in terms of their 
_speed_ and _scalability_ due to how the high energy-intensive process these imply. Massive quantities of processing 
hash power must be used to solve the computational challenge, which uses a lot of energy. Some have called the PoW model
an environmental catastrophe because of the enormous number of blocks verified on large PoW blockchains per day. **In 
fact, the more intensive the validation process, the more computational power is adopted to solve the puzzle and this 
leads to a higher competition among validators, which equals harder proofs of work and more energy consuming 
operations**. 

For instance, the Bitcoin network consumed as much power as Chile and had a carbon footprint that was equal to that of 
New Zealand in 2021. Technology advancement in the blockchain sector has put a lot of emphasis on addressing the 
negative environmental effects of crypto mining, and several alternatives have surfaced.

PoW blockchains have typically offered stronger security while preserving significant decentralization, despite their
speed and scalability restrictions. Due to the distributed nature of PoW systems, it would be very expensive for a bad 
actor to seize control of the majority of the network's computer power and take over the blockchain.

### Validation on Proof-of-Stake (PoS) Blockchains

The second-most popular consensus method, **Proof-of-Stake** (**PoS**), addresses many of the problems of Proof-of-Work 
blockchains, including their slowness, lack of scalability, wasteful energy use, and high entry barriers. Polkadot, 
Avalanche, and Cardano are a few instances of contemporary market-dominating PoS blockchains.

_PoS blockchains only have validators for transaction validation, not miners_. Similar to PoW systems, validators 
operate network nodes and validate data, but _there is no energy-intensive computing procedure required to earn the 
privilege to validate_. Validators stake some of the native tokens of the blockchain to qualify for selection as a 
validator node rather than working to solve proofs of work. The potential validator will effectively stake 
blockchain-native crypto tokens to act as collateral. 

On a PoS blockchain, when it is time to validate the data contained in a transaction block, the system chooses a 
validator at random to do so. The quantity of tokens a validator has staked is one such factor that, while somewhat 
random, might increase the likelihood that they will be picked as a validator. 

The process starts with a new block after the block is confirmed, and the validator is typically compensated with 
network transaction fees. **By asking validators to stake their tokens, Proof-of-Stake blockchains make the network safe 
and maintain validators' integrity**. Through a procedure known as **slashing**, validators that engage in malevolent or 
incompetent behaviour lose their stake and network access. By using this incentive system, validators are certain to 
benefit more from following the law than from breaching it.

**Every PoS blockchain has its own unique validation standards**, however on the majority of platforms, you must also 
meet certain criteria in order to be chosen as a validator node. The entrance barrier to PoS blockchains for validators 
is arguably lower, when compared to PoW blockchains, since they do not need to invest in expensive hardware or incur 
significant electricity costs. However, you still need to have enough cryptocurrency to stake if you want to become a 
validator. However, there can be particular hardware requirements for various platforms adopting a PoS mechanism. 

**While PoS is not nearly as resource-consuming as PoW, certain PoS blockchains' validator nodes may require strong 
hardware or software specifications because they may be the need of handling a lot of transactions at once**. 

Additionally, PoS blockchains have been accused of being plutocratic since validators' control over the network is 
frequently proportionally correlated with the quantity of their stake. Thus, even though the PoS validation process uses 
significantly less energy and is quicker and less expensive, it does have some drawbacks, such as the potential for 
power concentration in the hands of individuals on the network who have amassed a sizable amount of the platform's 
governance cryptocurrency.

**Delegated Proof-of-Stake** (i.e. **DPoS**), is a well-liked development of the Proof-of-Stake idea in which network 
users chose delegates to validate the following block. **Delegates** may also be referred to as block producers or 
witnesses. By pooling your tokens into a staking pool and tying them to a specific delegate, you may cast a vote for 
delegates using DPoS. **DPoS represent a more decentralized and equitable method of reaching consensus than just 
Proof-of-Stake mechanism**.
