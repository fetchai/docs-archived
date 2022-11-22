## What is a Peer-to-Peer system?

A **Peer-to-Peer** (i.e. **P2P**)  system is a network of users who communicate with each other without having to go through a middleman. Peer-to-Peer networks consist of a group of devices that collectively store and share files. Every participant (i.e. _node_) functions as a distinct _peer_. Normally, all nodes are equally powerful and carry out the same functions. We can outline three key characteristics featuring a P2P system:

1. **No middlemen needed**: One of the key characteristics of peer-to-peer systems is that middlemen are not always required, though they are allowed. For instance, when booking a hotel room with a travel agent, the users will be going through a middleman but if the user books a hotel room directly with the hotel itself, then this depicts a direct communication, and hence, they are communicating on a peer-to-peer basis.

2. **Direct links**: direct communication between both parties can be established only in the presence of direct links between them.

3. **Direct interaction**: It is not enough just for parties to be able to communicate directly, they have to be able to actually interact. Peer-to-peer systems are characterized by direct interaction. In the hotel room booking example, making a booking with the hotel sending back a booking confirmation actually consists of a direct interaction between the two parties.

??? note

    P2P networks enable the sharing of files stored on linked devices' hard drives. A user can serve as the source of a file after they have downloaded it. In other words, when a node performs the role of a client, it downloads data from other network nodes. However, while they are acting as a server, they serve as the location for file downloads by other nodes. However, both operations can be carried out concurrently. Therefore, each node has a copy of the data and serves as both a client and a server to other nodes. This removes the need of a central administrator or server. 

    P2P networks differ from more conventional client-server systems in this way, where client devices receive files from a centralized server.  Since every node sends, receives, and saves data, P2P networks often get quicker and more effective as their user bases expand. P2P networks are also particularly resilient to cyberattacks thanks to their distributed architecture, and P2P networks do not have a single point of failure, in contrast to conventional models.

P2P systems can be grouped based on their architecture into the following _three primary subtypes_:

### Unstructured P2P networks

P2P networks that are unstructured lack a defined node organization. Participants communicate with one another in a random fashion. These systems are thought to be resistant to high churn activity (i.e. several nodes frequently joining and leaving the network). 

??? note

    Unstructured P2P networks are simpler to set up, but because search requests are sent to as many peers as possible, they may utilize more CPU and memory. This frequently causes the network to get overrun with requests, especially when only a few nodes are providing the needed material.

### Structured P2P networks

The structured P2P network is organized into an arrangement based on a distributed hash table (i.e. DHT). 

!!! info 

    DHT is an advanced form of lookup or search system that allows nodes to access data, such as files, through the use of a key instead of having to make a copy of the data on every node. 

This contrasts with the idea behind unstructured P2P networks in which whole files may be stored on more than one node. 

??? note

    Searching for material in a structured network is simpler and uses less power and memory than an unstructured network. The routing of requests and information rely on each peer knowing what is available for download and other criteria of the neighboring node, which must be relearned as peers leave or join the network as the neighbors change.

### Hybrid P2P networks

In hybrid P2P networks, some elements of the P2P architecture are combined with the traditional client-server approach. For instance, it might provide a central server that streamlines peer communication. Hybrid models typically display better overall performance when compared to the other two categories. They typically incorporate some key benefits of each strategy, attaining notable levels of efficiency and decentralization at the same time.

## Benefits and drawbacks of a P2P system

### Benefits

* **No need for a specific operating system or software**: Individual peers can be on any OS and in most cases do not need specialized software to share files. This is especially useful in remote P2P networks where users might not have the same hardware.

* **Cost**: P2P networks do not need a costly server and can be joined together simply through USB or over the internet. Even more permanent connections (using copper wires in smaller offices, for example) is not as costly as creating a server or buying server software.

* **Egalitarian**: Each peer has control over what can be accessed by others on the network by changing the sharing settings. This makes it easier to protect the integrity of the network as an issue with one node will not destroy the rest of the peers.

* **Easy to set up**: Configuration is straightforward, with no need for the oversight of an administrator. Each node manages access and sharing themselves.

* **Scalable**: P2P networks are easy to scale, with more nodes adding performance and giving more power. Adding more peers makes more storage and processing power available to the network and can improve download and upload speeds.

* **Easy searching**: The idea of a peer-to-peer network is that finding the right resources should, in theory, be easy. Even in an unstructured network, if the content you are searching for is not rare, it should be held by several peers and be available to download from multiple sources.

* **Aligns with decentralized systems**: Peer-to-peer systems align closely with decentralized systems, as both require trust between parties in order to work effectively, and both do not require central authorities to manage the system. Peer-to-peer communication is the basis of how parties in decentralized systems communicate with each other.

* **More freedom**: By not having to go through a middleman, it gives users more freedom. They are not limited by the information for example provided by the hotel booking site but can find out far more by being in direct contact with the hotel and likewise the hotel can ask questions directly to their guests.

### Drawbacks

* **Decentralized**: this makes it harder to arrange backups and file archiving. The safety and integrity of the content can be at risk if it is not managed, backed up regularly and deleted once it is obsolete. Due to the decentralized nature of such networks, participants may find it hard to provide themselves those useful services normally provided by the middlemen, such as marketing and promoting services, or market balancing services.

* **No oversight**: in most of P2P networks, the decentralized nature makes it hard for a single administrator to monitor contents, and these can be at risk from malware and viruses. Sharing files with an infected node can transmit malware through the network and could cause problems over several affected peers.

* **Slow transmission**: simultaneous uploading and downloading of files can lead to a slower rate of transmission. The double function of uploading content while downloading other resources might actually make it slower.

* **Poor internet performance**: file sharing through P2P networks uses a lot of bandwidth and CPU, which can slow the computer performance for the individual user, especially when it comes to the internet. If multiple files are being shared, there is a risk that productivity in other areas could be reduced.

* **Illegal content**: peer-to-peer networks can be used for downloading pirated music, movies, software and other copyrighted material, even if the sharer is unaware.

## Examples of Peer-to-Peer Systems 

One of the most popular uses of P2P systems is represented by file sharing networks which allow members to directly share files with each other.

!!! example

    [Napster](https://www.napster.com/it) and [LimeWire](https://limewire.com/) were P2P music sharing networks backed by the idea that peers connected through the internet could find and download any song they wanted, from several other users.

    There exist also online gaming platforms which adopt a P2P structure for downloading games between users, such as [Blizzard Entertainment](https://www.blizzard.com/en-gb/) which distributed Diablo III, StarCraft II, and World of Warcraft using P2P.

A more successful use for P2P systems was developed in the crypto world thanks to **blockchains** and how these relate to P2P networks. Bitcoin, Ether and many other cryptocurrencies were developed following the P2P mechanism. 

An additional example of P2P architecture is represented by **P2P crypto exchanges**, on which users can immediately buy or sell cryptos from/to other users directly. The majority of P2P exchanges let you send and receive cryptocurrencies without requesting identity verification, in contrast to centralized exchanges where you must complete KYC in order to fulfill an order. Also, unlike centralized exchanges, P2P-based exchanges do not have a single point of failure. In most cases, a user may sign up for the exchange without having to undergo identification verification. A password and an email address are all that are needed for registration. 

!!! example

    P2P-based crypto exchanges include [Paxful](https://paxful.com/) and [Binance P2P](https://p2p.binance.com/en/trade/all-payments/USDT?fiat=CNY).
