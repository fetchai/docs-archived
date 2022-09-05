# What is a blockchain?

A  **blockchain** is a series of data records that functions as a distributed, replicated digital ledger of transactions across a network of computer systems. 

If we compare a blockchain to a conventional database, in the latter one records are written in tables which might be on one or more servers located in different locations, but they are all centrally administered by a database administrator. When it comes to blockchains, instead of the records being written in tables, the records of transactions are compiled into **blocks** which are linked together. A blockchain consists of a stable chain of blocks, and in the context of cryptocurrencies, each one of these blocks stores a list of previously confirmed transactions.
 
 Because blockchain transactions take place inside a P2P global network, these are considered borderless and immune to censorship. Hence, a blockchain network serves as a decentralized ledger since it is maintained by several computers located all over the world. This implies that each participant, namely a node, keeps a copy of the blockchain data and interacts with other participants to make sure that everyone is aware of the same information stored in the block.

Blockchains also differ from traditional databases in the impossibility for a malicious actor to come in and alter a blockchain record, whereas within traditional databases, this risk is a constant security challenge. In addition to this, blockchains do not need any sort of trust, because these systems are regarded as being trustless because of the absence of supervision by any central authority. On a blockchain system, management is carried out by its participants.

A further distinction can be made between databases and blockchains, when it comes to the editing and updating of records: in the context of a traditional database, the database administrator can update and delete records freely, whereas in a blockchain this is impossible. In fact, a blockchain record can only be created, but once written, it can not be altered or deleted in any way. Each block inside the blockchain contains a hash (i.e. a digital fingerprint or unique identifier), timestamped batches of recent valid transactions, and the hash of the previous block. The previous block hash links the blocks together and prevents any block from being altered or a block being inserted between two existing blocks. An additional feature of a blockchain is that all previous records are stored within the current records, and hence,  there is a full history of previous transactions. 

A central concept here is given by **mining operations**. Mining is the process by which cryptocurrency transactions between users are verified and added to the blockchain public ledger. The mining operations are also responsible for introducing new coins into the existing circulating supply. New blockchain transactions are submitted to a pool (i.e. memory pool) when these are created. A miner's responsibility is to arrange these pending transactions into blocks and confirm their authenticity. A block may be compared to a page of the blockchain ledger where many transactions are recorded, alongside with other data. More specifically, a mining node is in charge of building a candidate block from unconfirmed transactions in the memory pool. The miner will next attempt to turn this candidate block into a legitimate,confirmed block. But in order to achieve it, they must solve a challenging mathematical puzzle. This requires a lot of computational resources, but every successfully mined block will give the miner a block reward, consisting of newly created cryptocurrencies plus transaction fees. 

## Blockchains: use cases

Blockchain technology has progressively gained popularity since the invention of Bitcoin in 2008, and cryptocurrencies are now recognised on a bigger scale. This technology is mostly used to track cryptocurrency transactions, but it is suitable for a variety of different types of digital data and has other potential applications. Bitcoin, which was created using a thorough and balanced blend of cryptography and game theory, is the oldest, safest, and largest blockchain network. While blockchain is currently primarily used to record and store cryptocurrency transactions, its proponents are creating and testing alternative uses for blockchain, such as the following:

1. **Blockchain for payment processing and money transfers**: banking transfer fees might be decreased (or eliminated) for transactions handled through a blockchain and paid in a couple of seconds.

2. **Blockchain for monitoring of supply chains**: businesses may easily identify inefficiencies in their supply chains using blockchain, as well as find products in real time and monitor their quality as they move from producers to retailers.

3. **Blockchain for digital IDs**: Microsoft is experimenting with blockchain technology to help people control their digital identities, while also giving users control over who accesses that data.

4. **Blockchain for data sharing**: blockchain could act as an intermediary to securely store and move enterprise data among industries.
 
5. **Blockchain for copyright and royalties protection**: blockchain technology has the potential to be utilized to build a decentralized database that guarantees the preservation of music rights and rewards musicians with transparent and real-time royalties. Blockchain may potentially benefit open source programmers in a similar way.

6. **Blockchain for Internet of Things (IoT) network management**: blockchain has the potential to regulate IoT networks by identifying connected devices, tracking their behavior, assessing their dependability, and automatically determining the dependability of new devices that are linked to the network, such as smartphones and vehicles.

7. **Blockchain for healthcare**: the healthcare industry may benefit greatly from the use of blockchain. Blockchains are being used by healthcare payers and providers to handle clinical trial data and electronic medical records while upholding regulatory compliance.

## Who can participate in a blockchain network? 

Each blockchain network has various participants, each one playing a different role:

1. **Blockchain users**: participants (typically business users) with permissions to join the blockchain network and conduct transactions with other network participants.

2. **Regulators**: blockchain users with special permissions to oversee the transactions happening within the network.

3. **Blockchain network operators**: individuals who have special permissions and authority to define, create, manage, and monitor the blockchain network.

4. **Certificate authorities**: individuals who issue and manage the different types of certificates required to run a permissioned blockchain.

## Benefits 

Blockchains have the following key _positive features_:

1. **Security**: blockchains are very secure, as the data is cryptographically encrypted and it is very difficult and obvious if someone is trying to hack into a blockchain. To delete a record in the blockchain would require the whole chain to be hacked and this would be an immense, obvious, and impractical undertaking.

2. **Resiliency**: as the same information is stored in many different places on the blockchain then blockchains are very resilient as if any part or indeed even the majority of the network was to catastrophically fail then the information stored on the blockchain is still available in full.

3. **Trust**: blockchains are decentralized systems so they have the same benefit of lacking a central authority that behaves in its own interest. Therefore there is a high degree of trust between the participants; the system is run by the participants for the participants.

## Drawbacks 

There are some important _negative features_ of blockchains:

1. **Complexity of setup**: setting up a blockchain is not a simple task, there are networks of nodes to set-up, the participatory framework established, and numerous components to bring together before you can even begin to store any information on the blockchain. Compared to setting up a traditional database, blockchains are much more complex to set up.

2. **Speed**: it takes longer to add a record to a block and add a block to the chain than it does to simply add a record into a traditional database table. This is a challenge for blockchain based payment systems, as blockchains typically handle fewer transactions per second than conventional payment systems.

3. **Scaling issues**: blockchains often have scalability issues, because as they grow they get more complex leading to issues of network congestion.

4. **Participation is required**: blockchains are decentralized systems, so they do need the active participation of members, for example they need to vote on governance proposals affecting the chain and be engaged in order for the blockchain to successfully operate. This means a limited amount of extra work for participants.

## Types of Blockchain

The architecture of blockchain systems varies greatly, especially in terms of the _consensus_ techniques employed to carry out the crucial role of validating network data (i.e. _Proof-of-Work (PoW)_ and _Proof-of-Stake (PoS)_ mechanisms). The security, usability, and sustainability of the underlying blockchain are affected differently by their own design. Different blockchain networks operate quite differently from one another. The kind of consensus mechanism each blockchain employs is one fundamental distinction. A blockchain adopts a consensus method to decide on information on the network, such as whether transactions are valid and in what order they should happen. Additionally, the consensus method is essential for protecting the blockchain network from bad actors like hackers.

We can distinguish among: **public**, **private**, **consortium** and **hybrid** blockchains.  

1. **Public blockchains** are entirely decentralised, permissionless, and open to everybody. Public blockchains allow all nodes to have equal access to the blockchain, the ability to add new blocks of data, and the ability to validate existing blocks of data are largely utilised nowadays for bitcoin mining and trading. These blockchains include Bitcoin, Ethereum, and Litecoin as examples. The majority of public blockchain networks use processes known as _Proof-of-Work_ (_PoW_) or _Proof-of-Stake_ (_PoS_) to provide consensus. 

2. **Private blockchains** are blockchains with permissions that are managed by a single company. Who is permitted to be a node on a private blockchain is decided by the central authority. Additionally, the central authority may not always accord each node an equal right to execute certain responsibilities. Due to restrictions on public access, private blockchains are only partially decentralised. Permissioned blockchains can be structured in various ways to prioritize speed, security, and scalability.

3. **Consortium blockchains** are permissioned blockchains governed by a group of entities, rather than a single one as private blockchains. As a result, consortium blockchains are more decentralised than private blockchains, which increases their security. But creating consortiums may be a difficult process since it calls for collaboration between several groups, which poses logistical problems and a possible antitrust risk.

4. **Hybrid blockchains** are blockchains which are managed by a single entity but at the same time have some supervision provided by the public blockchain, which is necessary to carry out specific transaction validations. The IBM Food Trust blockchain is an illustration of a hybrid blockchain. It was created to increase efficiency along the whole food supply chain.

**Private** and **consortium blockchains** are typically used by enterprises that aim to employ blockchain architecture, but want to ensure specific information remains private, for either regulatory or competitive reasons. On the other hand, **public blockchains** are censorship-resistant and offer broad ecosystems for the development of apps and platforms. **Consortium blockchains**, however, may offer faster transaction processing times and are easier to modify, but are restrictive with limited usage outside of the private consortium.

Varying consensus techniques have different effects on accessibility, security, and sustainability, and not all blockchains are created equally. In fact, the most suitable type of blockchain design needs to be fitting the actual use case it wants to serve.
 