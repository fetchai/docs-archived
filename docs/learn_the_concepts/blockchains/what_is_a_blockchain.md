# What is a Blockchain?

A  **blockchain** is a series of data records that functions as a distributed, replicated digital ledger of transactions across a network of computer systems.

!!! info 

      On blockchains, the records of transactions are compiled into **blocks** which are linked together to form a **chain**. A blockchain consists of a stable chain of blocks, and in the context of cryptocurrencies, each one of these blocks stores a list of previously confirmed transactions.

Transactions take place inside a P2P global network, thus, blockchains are considered borderless and immune to censorship. A blockchain network serves as a decentralized ledger since it is maintained by several computers located all over the world. This implies that each participant, namely **node**, keeps a copy of the blockchain data and interacts with other participants to make sure that everyone is aware of the same information stored in the block.

!!! note 

    Each block inside the blockchain contains a **hash** (i.e. a digital fingerprint or unique identifier), **timestamped batches of recent valid transactions**, and the **hash of the previous block**. The previous block hash links the blocks together, preventing existing blocks from being altered or new blocks inserted between existing ones. An additional feature of a blockchain is that all previous records are stored within any current record, so, there is always full history of previous transactions.

## Blockchains: Use Cases

Currently, the blockchain technology is mostly used to track cryptocurrency transactions. Examples of other uses are:

1. **Monitoring of Supply Chains**: businesses may easily identify inefficiencies in their supply chains using blockchain, as well as find products in real time and monitor their quality as they move from producers to retailers.

2. **Data sharing**: blockchain could act as an intermediary to securely store and move enterprise data among industries.
 
3. **Copyright and royalties protection**: blockchain technology has the potential to be utilized to build a decentralized database that guarantees the preservation of music rights and rewards musicians with transparent and real-time royalties.

4. **Internet of Things (IoT) network management**: blockchain has the potential to regulate IoT networks by identifying connected devices, tracking their behavior, assessing their dependability, and automatically determining the dependability of new devices that are linked to the network, such as smartphones and vehicles.

5. **Healthcare**: the healthcare industry may benefit greatly from the use of blockchain. Blockchains are being used by healthcare payers and providers to handle clinical trial data and electronic medical records while upholding regulatory compliance.

## Who can participate in a blockchain network?


1. **Blockchain users**: participants joining the blockchain network and conducting transactions with other network participants.

2. **Regulators**: users with special permissions to oversee the transactions happening within the network.

3. **Blockchain Network Operators**: individuals who have special permissions and authority to define, create, manage, and monitor the blockchain network.

4. **Certificate Authorities**: individuals who issue and manage the different types of certificates required to run a permissioned blockchain.

## Benefits

1. **Security**: blockchains are secure, in the sense that the data is cryptographically encrypted, and their structure makes it difficult and immediately noticeable if someone tries to change the data in a blockchain.

2. **Resiliency**: the same information is stored in many places on the blockchain. This implies high resiliency as, if any part of the network was to fail then the information stored on the blockchain is still available in full.

3. **Trust**: blockchains are decentralized systems and thus benefit from having no central authority controlling them. Due to their structure, and depending on the mechanism the blockchain's participants use to arrive at a consensus on what the state of the chain is, there is no need for the blockchain's users to trust the other parties. Guarantees are provided by the system itself.

## Drawbacks

1. **Complexity**: Setting up a blockchain is not a simple task, there are networks of nodes to set up, the participatory framework established, and numerous components to bring together before you can even begin to store any information on the blockchain.

2. **Speed**: It takes longer to add a record to a block and add a block to the chain than it does to simply add a record into a traditional database table. This is a challenge for blockchain-based payment systems, as blockchains typically handle fewer transactions per second than conventional payment systems.

3. **Scaling issues**: As blockchains grow, they get more complex leading to issues, such as network congestion.

4. **Participation is required**: Blockchains are decentralized systems, so they do need the active participation of members, for example they need to vote on governance proposals affecting the chain and be engaged in order for the blockchain to successfully operate.

## Types of Blockchain

The architecture of blockchain systems varies greatly, especially in terms of the [consensus protocol](https://docs.fetch.ai/learn_the_concepts/blockchains/consensus/) employed to validate network data. The security, usability, and sustainability of the underlying blockchain are affected differently by their own design. Different blockchain networks operate quite differently from one another. We can identify the following:

* **Public blockchains** are entirely decentralised, permissionless, and open to everybody. All nodes are meant to have equal access and abilities within the blockchain. These are censorship-resistant and offer broad ecosystems for the development of apps and platforms. 

    !!! example

            Examples of public blockchains include Bitcoin and Ethereum. The majority of public blockchain networks use processes known as _Proof-of-Work_ (_PoW_) or _Proof-of-Stake_ (_PoS_) to provide consensus.

* **Private blockchains** are blockchains within which permissions are managed by a single company. It is the central authority which decides who can be a node. The central authority may not always accord each node an equal right to execute certain responsibilities. This makes private blockchains partially decentralised. Private (or permissioned) blockchains can be structured in various ways to prioritize speed, security, and scalability.

+ **Consortium blockchains** are permissioned blockchains governed by a group of entities, rather than a single one as private blockchains. These blockchains are more decentralised than private blockchains, which increases their security. But creating consortiums may be a difficult process since it calls for collaboration between several groups, which poses logistical problems and a possible antitrust risk. However, these may offer faster transaction processing times and are easier to modify, but are restrictive with limited usage outside the private consortium.

* **Hybrid blockchains** are blockchains which are managed by a single entity but at the same time have some supervision provided by the public blockchain, which is necessary to carry out specific transaction validations.

!!! note 

    Varying consensus techniques have different effects on accessibility, security, and sustainability, and not all blockchains are created equally. In fact, the most suitable type of blockchain design needs to be fitting the actual use case it wants to serve.
