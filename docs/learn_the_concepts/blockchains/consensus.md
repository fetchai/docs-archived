# Consensus Mechanisms

Despite the absence of a central authority to confirm and authenticate the transactions, every Blockchain transaction is regarded as being totally safe and validated. Only the presence of the consensus protocol, a fundamental component of every Blockchain network, makes this feasible. 
 
!!! info 

    A consensus algorithm allows every peer in the Blockchain network to agree on the distributed ledger's current state. Consensus algorithms accomplish dependability in the Blockchain network and build confidence amongst unidentified peers in a distributed computing setting in this way.  

Hence, the consensus mechanism ensures that every new block added to the Blockchain is the sole version of the truth that has been accepted by every node.

When it comes to confirming the legitimacy of distributed blockchain systems, each consensus technique has a unique set of benefits and drawbacks. While PoW and PoS are the most common, new algorithms are always emerging. The following are the most utilized consensus mechanisms nowadays: 

## Proof-of-Work (PoW)

One of the most prominent blockchain technologies is the PoW consensus process, which was initially made popular by Bitcoin. Miners and the power they need to do the computations required to validate transactions are the key elements that distinguish PoW systems. Miners use computer hardware to power network nodes that use processing power to solve algorithmic mathematical computational puzzles, known as proofs of work. The miner who completes the puzzle first validates the blockchain's most recent block of transactions. The successful miner broadcasts the new block to all other nodes, which in turn authenticate its accuracy and add that block to their copies of the blockchain. This verification procedure establishes consensus. A new block cannot be added to the network until this data has been verified. When a miner validates a new block of data this latter one is then added to the PoW blockchain, with the first miner completing the validation process being rewarded with newly created cryptocurrency, known as the _block reward_.

??? note

      PoW networks are constrained in terms of their speed and scalability due to how the high energy-intensive process these imply. Massive quantities of processing hash power must be used to solve the computational challenge, which uses a lot of energy. The more intensive the validation process, the more computational power is adopted to solve the puzzle and this leads to a higher competition among validators, which equals harder proofs of work and more energy consuming operations. Technology advancement in the blockchain sector has put a lot of emphasis on addressing the negative environmental effects of crypto mining, and several alternatives have surfaced.

      PoW blockchains have typically offered stronger security while preserving significant decentralization, despite their speed and scalability restrictions. Due to the distributed nature of PoW systems, it would be very expensive for a bad actor to seize control of the majority of the network's computing power and take over the blockchain. Typically, it is unable to overcome the high expenses of the hardware, power, and computing.

## Proof-of-Stake (PoS)

PoS blockchains only have validators for transaction validation, not miners. Similar to PoW systems, validators operate network nodes and validate data, but there is no energy-intensive computing procedure required to earn the privilege to validate. 

!!! info

      This consensus mechanism addresses many of the problems of PoW blockchains, including slowness, lack of scalability, wasteful energy use, and high entry barriers. Polkadot, Avalanche, and Cardano are a few instances of contemporary market-dominating PoS blockchains.

Validators stake some native tokens of the blockchain to qualify for selection as a validator node rather than working to solve proofs of work. The potential validator will effectively stake blockchain-native crypto tokens to act as collateral. On a PoS blockchain, when it is time to validate the data contained in a transaction block, the system chooses a validator at random to do so. The quantity of tokens a validator has staked is one such factor that might increase the likelihood that they will be picked as a validator. 
 
The process starts with a new block after the block is confirmed, and the validator is typically compensated with network transaction fees. By asking validators to stake their tokens, PoS blockchains make the network safe and maintain validators' integrity.  The entrance barrier to PoS blockchains for validators is arguably lower, when compared to PoW blockchains, since they do not need to invest in expensive hardware or incur significant electricity costs. However, you still need to have enough cryptocurrency to stake if you want to become a validator. PoS blockchains have been accused of being plutocratic since validators' control over the network is frequently proportionally correlated with the quantity of their stake. Thus, even though the PoS validation process uses significantly less energy and is quicker and less expensive, it does have some drawbacks, such as the potential for power concentration in the hands of individuals on the network who have amassed a sizable amount of the platform's governance cryptocurrency.

??? note
   
      Through a procedure known as slashing, validators that engage in malevolent or incompetent behaviour lose their stake and network access. By using this incentive system, validators are certain to benefit more from following the law than from breaching it.

      There can be particular hardware requirements for various platforms adopting a PoS mechanism. While PoS is not nearly as resource-consuming as PoW, certain PoS blockchains' validator nodes may require strong hardware or software specifications because they may be the need of handling a lot of transactions at once.

## Delegated Proof-of-Stake (DPoS)

It is a well-liked development of the Proof of Stake idea in which network users choose delegates to validate the following block. Delegates may also be referred to as block producers or witnesses. By pooling your tokens into a staking pool and tying them to a specific delegate, you may cast a vote for delegates using DPoS. The argument for DPoS is that it is a more decentralized and equitable method of reaching consensus than just Proof-of-Stake.

## Proof of Burn (PoB)

With PoB, validators burn coins by sending them to an address from which they are irretrievably lost, as opposed to spending money on expensive hardware equipment. Validators obtain the right to mine on the network based on a random selection procedure by sending the coins to an unreachable address. Burning coins here entails a long-term commitment on the part of validators in return for a temporary loss. Miners may burn either the native money of the Blockchain application or the currency of an alternate chain, such as bitcoin, depending on how the PoB is implemented. The more coins they burn, the better are their chances of being selected to mine the next block.

## Proof of Capacity (PoC)

PoC, often referred to as Proof-of-Space (PoSpace) is a mining technique that is based on the amount of hard disk space that a miner has available. Here, miners generate a list of all the possible hashes beforehand in a process called plotting. Such plots are then stored on hard drives. The more storage capacity a miner has, the more possible solutions available. The more solutions, the higher the chances of possessing the correct combination of hashes and thus the higher the possibility of winning the reward. 
 
!!! info

      PoC makes it possible for the typical individual to take part in the network because it does not need expensive or specialized equipment. As a result, this is decentralized and less energy-intensive alternative to some of the more widely used consensus mechanisms. However and there are concerns about its susceptibility to malware attacks.

## Proof of Activity (PoA)

It is a consensus approach that combines PoW and PoS. Similar to PoW, the mining process starts here with miners vying to use the most powerful processing power to solve a complex mathematical problem. The system then turns to resemble PoS when the block has been mined, with the successfully created block header being sent to the PoA network. The new block is then randomly validated by a number of validators who sign off on the hash. The more crypto a validator possesses, similar to PoS, the better their chances are of being chosen. The block is introduced to the blockchain network and made available to record transactions once each selected validator has signed it. The miner and validators then split the block rewards.
 
## Proof of Authority (PoA) 

This mechanism chooses its validators based on their track record. Validators in PoA do not stake coins. Instead, in order to have the ability to validate blocks, they must risk their reputations. The majority of blockchain systems, in contrast to this, often do not need participants to disclose their identities. This approach is far less resource-intensive than some of its predecessors, especially PoW, as it requires essentially little computational power.
