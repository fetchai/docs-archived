# Peer-to-Peer Systems

A **Peer-to-Peer** (i.e. **P2P**)  system is a network of users who communicate with each other without having to go through a middleman. Peer-to-Peer networks consist of a group of devices that collectively store and share files. Every participant (i.e. _node_) functions as a distinct _peer_. Normally, all nodes are equally powerful and carry out the same functions. We can outline three key characteristics featuring a P2P system:

1. **No middlemen needed**: One of the key characteristics of peer-to-peer systems is that middlemen are not always required, though they are allowed. For instance, when booking a hotel room with a travel agent, the users will be going through a middleman but if the user books a hotel room directly with the hotel itself, then this depicts a direct communication, and hence, they are communicating on a peer-to-peer basis.

2. **Direct links**: direct communication between both parties can be established only in the presence of direct links between them.

3. **Direct interaction**: It is not enough just for parties to be able to communicate directly, they have to be able to actually interact. Peer-to-peer systems are characterized by direct interaction. In the hotel room booking example, making a booking with the hotel with the hotel sending back a booking confirmation actually consists of a direct interaction between the two parties.
 
P2P networks enable the sharing of files stored on linked devices' hard drives. Using software tools designed to mediate data sharing, users may look for and download files from other networked devices. A user can serve as the source of a file after they have downloaded it. In other words, when a node performs the role of a client, it downloads data from other network nodes. However, while they are acting as a server, they serve as the location for file downloads by other nodes. However, in actuality, both operations can be carried out concurrently (e.g., downloading file A, and uploading file B).

In essence, a distributed network of users maintains a P2P system. Because each node has a copy of the data and serves as both a client and a server to other nodes, they often do not have a central administrator or server. Therefore, each node has the ability to download files from and upload files to other nodes. P2P networks differ from more conventional client-server systems in this way, where client devices receive files from a centralized server.  Since every node sends, receives, and saves data, P2P networks often get quicker and more effective as their user bases expand. P2P networks are also particularly resilient to cyberattacks thanks to their distributed architecture, and P2P networks do not have a single point of failure, in contrast to conventional models. 

P2P systems can be grouped based on their architecture into the following _three primary subtypes_: 

#### **Unstructured P2P networks**

P2P networks that are unstructured lack a defined node organization. Participants communicate with one another in a random fashion. These systems are thought to be resistant to high churn activity (i.e. several nodes frequently joining and leaving the network). Unstructured P2P networks are simpler to set up, but because search requests are sent to as many peers as possible, they may utilize more CPU and memory. This frequently causes the network to get overrun with requests, especially when only a few nodes are providing the needed material.

#### **Structured P2P networks**

Unlike the unstructured network, the structured P2P network is organized into an arrangement based on a distributed hash table (i.e. DHT). DHT is an advanced form of lookup or search system that allows nodes to access data, such as files, through the use of a key instead of having to make a copy of the data on every node. These keys are formed through hashing, whereby data of varying sizes are assigned generated values of the same size (e.g. a mix of 10 digits and letters). This contrasts with the idea behind unstructured P2P networks in which whole files may be stored on more than one node.
Consistent hashing, a kind of hashing, is the method used by DHT to assign ownership of a certain file to a particular peer. In a P2P network, conventional hashing demands that all keys be produced whenever a new peer joins. Consistent hashing uses less electricity since just a small portion of the keys must be generated. In general, searching for material in a structured network is simpler and uses less power and memory than searching in an unstructured network. The routing of requests and information rely on each peer knowing what is available for download and other criteria of the neighboring node, which must be relearned as peers leave or join the network as the neighbors change. High churn rates make this sort of network more difficult.

#### **Hybrid P2P networks**

In hybrid P2P networks, some elements of the peer-to-peer architecture are combined with the traditional client-server approach. For instance, it might provide a central server that streamlines peer communication. Hybrid models typically display better overall performance when compared to the other two categories. They typically incorporate some of the key benefits of each strategy, attaining notable levels of efficiency and decentralization at the same time.

## Benefits and drawbacks of a P2P system

### Benefits

- **No need for a specific operating system or software**: Individual peers can be on any OS and in most cases do not need specialized software to share files. This is especially useful in remote P2P networks where users might not have the same hardware.

- **Cost**: P2P networks do not need a costly server and can be joined together simply through USB or over the internet. Even more permanent connections (using copper wires in smaller offices, for example) is not as costly as creating a server or buying server software.

- **Egalitarian**: Each peer has control over what can be accessed by others on the network by changing the sharing settings. This makes it easier to protect the integrity of the network as an issue with one node will not destroy the rest of the peers.

- **Easy to set up**: Configuration is straightforward, with no need for the oversight of an administrator. Each node manages access and sharing themselves.

- **Scalable**: P2P networks are easy to scale, with more nodes adding performance and giving more power. Adding more peers makes more storage and processing power available to the network and can improve download and upload speeds.

- **Easy searching**: The idea of a peer-to-peer network is that finding the right resources should, in theory, be easy. Even in an unstructured network, if the content you are searching for is not rare, it should be held by several peers and be available to download from multiple sources.

- **Aligns with decentralized systems**: Peer-to-peer systems align closely with decentralized systems, as both require trust between parties in order to work effectively, and both do not require central authorities to manage the system. Peer-to-peer communication is the basis of how parties in decentralized systems communicate with each other.

- **More freedom**: By not having to go through a middleman, it gives users more freedom. They are not limited by the information for example provided by the hotel booking site but can find out far more by being in direct contact with the hotel and likewise the hotel can ask questions directly to their guests.

### Drawbacks

- **Decentralized**: this makes it harder to arrange backups and file archiving. The safety and integrity of the content can be at risk if it is not managed, backed up regularly and deleted once it is obsolete. Due to the decentralized nature of such networks, participants may find it hard to provide themselves those useful services normally provided by the middlemen, such as marketing and promoting services, or market balancing services.

- **No oversight**: in most of P2P networks, the decentralized nature makes it hard for a single administrator to monitor contents, and these can be at risk from malware and viruses. Sharing files with an infected node can transmit malware through the network and could cause problems over several affected peers.

- **Slow transmission**: simultaneous uploading and downloading of files can lead to a slower rate of transmission. While the idea is that it is more reliable and usually faster to utilize the processing power of multiple peers, the double function of uploading content while downloading other resources might actually make it slower.

- **Poor internet performance**: file sharing through P2P networks uses a lot of bandwidth and CPU, which can slow the computer performance for the individual user, especially when it comes to the internet. If multiple files are being shared, there is a risk that productivity in other areas could be reduced.

- **Illegal content**: peer-to-peer networks can be used for downloading pirated music, movies, software and other copyrighted material, even if the sharer is unaware.

## Examples of Peer-to-Peer Systems 
One of the most popular uses of P2P systems is represented by file sharing networks which allow members to directly share files with each other. [Napster](https://www.napster.com/it) and [LimeWire](https://limewire.com/), are great examples of a P2P system. These were P2P music sharing networks backed by the idea that peers connected through the internet could find and download any song they wanted, from several other users. Peers could also upload songs to Napster themselves, then share their files with others. These have come under a great deal of scrutiny with numerous lawsuits as the lack of a central authority has resulted in the inability to enforce copyright legislation, and numerous copyright infringements have been alleged. In fact, both Napster and LimeWire soon came under fire as the songs placed in the depository for download infringed on the copyright of the record labels and musicians.

Another example of P2P networking is given by some online gaming platforms which adopt  a P2P structure for downloading games between users. The company [Blizzard Entertainment](https://www.blizzard.com/en-gb/) distributed Diablo III, StarCraft II, and World of Warcraft using P2P. Another large publisher, Wargaming, does the same with their World of Tanks, World of Warships, and World of Warplanes games.

A perhaps more successful use for P2P systems was developed in the crypto world thanks to the concept of blockchains and how these relate to P2P networks. Bitcoin, Ether and many other cryptocurrencies were developed following the P2P mechanism. Indeed, when Bitcoin was created, Satoshi Nakamoto defined it as a “peer-to-peer electronic cash system” built with the aim to create a P2P digital form of money without banks. In the context of P2P blockchains, these rely on a shared and reliable record of transactions provided by the underlying blockchain technology, which makes use of the strength of P2P networks. A blockchain is a distributed ledger system that stores transactions as immutable, time-stamped digital blocks including sender and recipient information. The blockchain networks are run by decentralized organizations, and only the members may approve transactions amongst themselves. People and institutions may now accept the results without having faith in the participants thanks to technology. This brand-new approach to distributed data management and storage serves as a public digital ledger for all transactions and operations. In contrast to databases, which organize their data into tables, blockchains organize their data into blocks. Each transaction that occurs on the network can be added to these blocks, which have a set amount of storage. A new block is added to an existing block after it has been filled with transactions to add additional transactions, producing a chain of blocks known as the blockchain. Blockchains are not kept in a single location since they are decentralized. As an alternative, they are kept on network nodes or PCs. Every node possesses a copy of the network's transactions (i.e. In essence, each node keeps a copy of the blockchain and verifies the data with other nodes to verify accuracy). The distribution of blockchains over large numbers of nodes renders them virtually immune to the Denial-of-Service (i.e. DoS) attacks that plague numerous systems. Because a majority of nodes must establish consensus before data is added to a blockchain, it is almost impossible for an attacker to alter the data recorded onto it. When considering smaller blockchains, these are more susceptible to attacks because one person or group could eventually achieve control over a majority of nodes (i.e. 51% attack). Beyond security purposes, the P2P design adopted in cryptocurrencies blockchains makes them immune to government censorship. This means that the governments can not freeze or drain cryptocurrency wallets, in contrast to traditional bank accounts. This opposition also covers private money processing and content platform control initiatives. In order to avoid having their payments banned by other parties, some content producers and online retailers started accepting cryptocurrency payments.

An additional example of P2P architecture is represented by **P2P crypto exchanges**, on which users can immediately buy or sell cryptos from/to other users directly. The majority of P2P exchanges let you send and receive cryptocurrencies without requesting identity verification, in contrast to centralized exchanges where you must complete KYC in order to fulfill an order. Also, unlike centralized exchanges, P2P-based exchanges do not have a single point of failure. In most cases, a user may sign up for the exchange without having to undergo identification verification. A password and an email address are all that are needed for registration. A user may browse various purchases and sell offers made by users on the platform after logging in. Each offer varies in terms of rate, payment choices, and often the minimum or maximum purchase amount. A buyer might choose an offer and get in touch with the seller to arrange a deal. You can provide the accepted payment method and any associated fees if you're a vendor. To protect the security of the platform, P2P crypto exchanges typically employ an escrow account to deposit cryptocurrency or other forms of user collateral. Examples of P2P-based crypto exchanges include:  

- [Paxful](https://paxful.com/) 
- [Binance P2P](https://p2p.binance.com/en/trade/all-payments/USDT?fiat=CNY)
- [HODL HODL](https://hodlhodl.com/)
- [Bisq](https://bisq.network/)
