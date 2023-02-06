Blockchains get their most significant positive features by being purposefully segregated from external systems. However, off-chain data cannot be accessed by blockchains or smart contracts directly, and these need such data to perform any contractual agreement between any party on the blockchain itself. This is known as the core of **the Oracle dilemma**. 

This issue comes from the following limitation: _blockchains are unable to draw data from or push data out to any external systems as part of their built-in functionality_. A blockchain's isolation is precisely what makes it so safe and dependable since the network just needs to come to consensus on a very simple set of questions using information that has already been written in the ledger (e.g. did the owner of the public key sign the transaction with their matching private key? Is the public address sufficiently funded to support the transaction?)

A blockchain needs an additional piece of infrastructure, an **Oracle**, to connect the blockchain to the off-chain services in a secure manner. _A blockchain Oracle is a safe piece of middleware that makes it easier for blockchains to communicate with any off-chain system, such as data providers, online APIs, business backends, cloud providers, IoT devices, e-signatures, payment systems, other blockchains, and more_. This is, a blockchain Oracle is the element that links the blockchain to the external system, making it possible for smart contracts to operate on the basis of inputs and outputs from the real world. 

The Oracle system must work concurrently on and off the blockchain in order to perform these tasks. The **on-chain component** is used to connect to the blockchain to listen for requests, broadcast messages, submit proofs, extract blockchain data, and perhaps even carry out computation on the blockchain. The **off-chain component** is used to execute requests, retrieve and prepare external data, transport blockchain data to other systems, and carry out off-chain computation for improved smart contract scalability, privacy, security, and other features.

Blockchain Oracles can help to increase the range of possibilities for smart contracts to work, thus, Oracles are essential components of the blockchain ecosystem. Smart contracts would not even be particularly useful without blockchain Oracles as they would only have access to data from their own networks since the vast majority of smart contract use cases, including DeFi, depend on knowledge of real world data and off-chain occurrences. Oracles provide a global gateway to off-chain resources, therefore expanding the sorts of digital agreements that blockchains may support while maintaining the crucial security features of blockchains. Oracles and smart contracts are beneficial for many major businesses, including asset pricing in banking, weather data in insurance, randomness in gaming, IoT sensors in supply chains, identity verification in government, and many more. Because the results of smart contracts are directly determined by the data that oracles supply to blockchains, it is crucial that the Oracle mechanism works accurately for the agreement to operate exactly as intended.

## Types of Blockchain Oracles

Blockchain Oracles may be categorized based on the following characteristics:

* Data source: does the data come from hardware or software as its source?
* Information direction: is the flow of data going inward or outward?
* Trust: are these oracles decentralized or centralized?

Given this, we can identify the following types of oracles:

1. **Software Oracles**: these communicate with internet data sources and provide the data to the blockchain. Any internet data source is a possible source for this information (e.g. online databases, servers, websites, ...). Exchange rates, pricing of digital assets, and real-time flight information are just a few of the types of data that software oracles frequently give.

2. **Hardware Oracle**: these Oracles are made to gather data from the real world and provide it to smart contracts. Electronic sensors, barcode scanners, and other information gathering tools may transmit this data. In essence, a hardware oracle converts actual occurrences into digital values that smart contracts can comprehend.

3. **Inbound and Outbound Oracles**: outbound Oracles transfer information from smart contracts to the outside world, whereas inbound Oracles give information from external sources to smart contracts.

4. **Centralized and Decentralized Oracles**: A centralized Oracle is the only source of data for the smart contract and is managed by a single organization. It can be dangerous to rely just on one source of information because the Oracle's owner determines whether the contract will work. Also, the smart contract will be directly impacted by any harmful intervention from a bad actor. The primary issue with centralized oracles is that they have a single point of failure, which reduces the contracts' resistance to weaknesses and intrusions.
 
    On the other hand, avoiding counterparty risk is one of the goals shared by public blockchains and decentralized Oracles. By not depending on a single source of truth, decentralized Oracles improve the accuracy of the data supplied to smart contracts. Decentralized Oracles can also be referred to as consensus Oracles since the smart contract consults several Oracles to assess the validity and correctness of the data. Decentralized Oracle services are offered by several blockchain projects to other blockchains. In prediction markets, where the legitimacy of a particular conclusion may be confirmed by social consensus, decentralized oracles can also be helpful. While decentralized Oracles strive for trustlessness, it is crucial to remember that, like trustless blockchain networks, they do not entirely get rid of trust but rather spread it across many users.

5. **Specialized Oracles**: these Oracles are created so that a single smart contract can use them. This means that a proportionately large number of contract-specific Oracles must be created if one plans to implement numerous smart contracts.

    These Oracles are said to be exceedingly time and money consuming. This strategy can prove to be quite unworkable for businesses that need to pull data from a number of sources. On the other hand, developers have a lot of freedom to customize contract-specific Oracles to meet unique needs because they may be created from the ground up to service a particular use case.

6. **Human Oracles**: Oracles can occasionally be people who have specific expertise in a certain area. They are able to gather information from numerous sources, investigate its veracity, and convert it into smart contracts. Since human Oracles may use cryptography to confirm their identity, it is unlikely that a fraudster will pretend to be them while supplying tainted information.

7. **Cross-Chain Oracles**: these are another kind of Oracle that can read and write data between several blockchains. Using data from one blockchain to start an activity on another or connecting assets across chains so they may be utilized outside of the native blockchain they were issued on, cross-chain Oracles provide interoperability for moving both data and assets between blockchains.

Given the variety of Oracle services, selecting between Oracle service providers often comes down to **reputation**. Users and developers may monitor and discriminate amongst Oracles based on criteria they think are significant thanks to reputation in blockchain Oracle systems. _The fact that Oracles sign and distribute their data onto an immutable public blockchain ledger, allowing for the analysis and presentation of their previous performance history to users through interactive dashboards, contributes to Oracle reputation_. Reputation frameworks offer transparency into each Oracle network's and each Oracle node operator's precision and dependability. Then, users may decide for themselves which Oracles they wish to use to support their smart contracts. Oracle service providers may also exploit their reputation in the off-chain business world to provide customers extra assurances about their dependability.

## Blockchain Oracles: Use Cases

* **Decentralized Finance (DeFi)**

    Oracles are necessary for a significant section of the decentralized finance (i.e. DeFi) ecosystem to access financial information regarding assets and markets. Decentralized money markets, for instance, employ price oracles to assess users' borrowing capacity and evaluate if their holdings are undercollateralized and at risk of liquidation. Similarly, Automated Market Makers (AMMs) employ price Oracles to assist concentrate liquidity at the current market price to increase capital efficiency. Synthetic asset platforms use price oracles to link the value of tokens to real-world assets.

* **Dynamic NFTs and Gaming**

    Oracles also make it possible for smart contracts to be used in non-financial use cases, such as NFTs and dynamic NFTs. Non-fungible Tokens (i.e. NFTs) that can alter in appearance, value, or distribution based on external factors like the time of day or the weather are examples of dynamic NFTs. Oracles may also produce verified randomness, which projects can utilize to give NFTs randomized characteristics or to choose random winners in high-demand NFT drops. Verifiable randomness is also used in on-chain gaming applications to produce more captivating and surprising gameplay elements, such as the emergence of random treasure boxes or random matchmaking during a tournament.

* **Businesses**

    Businesses may link their backend systems to any blockchain network using the safe blockchain middleware provided by business cross-chain Oracles. Enterprise systems may read from and write to any blockchain in this way, and they can also use complicated logic to decide how to deploy assets and data among chains and with counterparties that are connected to the same oracle network. As a consequence, institutions no longer need to invest time and development resources in integrating with each individual blockchain. Instead, they can immediately join blockchains that are highly desired by their counterparties and quickly provide support for smart contract services that their customers require.

* **Insurance**

    Insurance smart contracts provide access to physical sensors, online APIs, satellite images, and legal data by using input Oracles to confirm the presence of insurable events throughout claims processing. Using other blockchains or conventional payment networks, output Oracles can give insurance smart contracts a mechanism to pay out on claims.
