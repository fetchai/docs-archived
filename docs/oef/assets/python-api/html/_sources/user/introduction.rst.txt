.. _introduction:

Introduction
============

What is Fetch?
--------------

**Fetch promotes a world** where digital entities can exist, interact, and collaborate/cooperate by exchanging
data services *autonomously* on behalf of their representatives.
These digital entities are software agents augmented by machine
learning and AI capabilities and known as  *Autonomous Economic Agents* (AEAs).
Fetch enables a *data marketplace* where AEAs can be attached
to data sources (such as IoT devices) to propose a data service as a *Data Service Provider*,
and AEAs looking for data can get it as a *Data Service Consumer*. AEAs will register,
query, and negotiate data services on behalf of their representatives.

.. image:: https://github.com/fetchai/oef-sdk-python/wiki/imgs/fetch-world.png
   :target: https://github.com/fetchai/oef-sdk-python/wiki/imgs/fetch-world.png
   :alt: Fetch World

The *Fetch network* achieves this by providing a 3-level layered software architecture:
*Smart Ledger*, *Open Economic Framework* (OEF), and *Autonomous Economic Agent* (AEA) layer.
The bottom layer is the Ledger. It implements scalable transactions between agents
allowing for data service contracts and basic trust mechanism. The OEF layer implements agent and data exploration.
Finally, the AEA layer implements data models and communication protocols for agents
to interact with the OEF and with each other.

What is OEF? (Open Economic Framework)
--------------------------------------

Overview
~~~~~~~~

**To access Fetch world**, AEAs (or just agents from now on) need to connect to a Fetch node that deploys the OEF.

The OEF-core is the part of the OEF that manages primitive operations:
agent connections, registrations, search, and queries.
It implements the core concepts and protocols needed to allow agents
to live, interact and advance in the Fetch world.
It is also the interface to the ledger.

The OEF-core keeps track of connected agents in an *AgentDirectory* and registered data services
in a *ServiceDirectory*.

For each connected and correctly identified agent, the AgentDirectory stores its ID,
description (as a property list), and session. If the agent registers a data service,
the data service along with the agent ID will be stored in the ServiceDirectory.

.. image:: https://github.com/fetchai/oef-sdk-python/wiki/imgs/oef-core.png
   :target: https://github.com/fetchai/oef-sdk-python/wiki/imgs/oef-core.png
   :alt: OEF-core

For simplicity, in the next, we use `OEF core` and `OEF node` interchangeably.

Agent life-cycle
~~~~~~~~~~~~~~~~

A typical agent life-cycle on the OEF consists of:

1. Connect to the OEF-core
2. Register a DataService, query for a DataService, or search for agents
3. Interact with other agents
4. Unregister DataServices, if any
5. Disconnect from the OEF-core

Agent-to-OEF core interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1.** To be part of the Fetch world, an agent first needs to connect to a Fetch node on the OEF-Core
 and identify itself using its public key.


.. image:: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-connect-2.png
   :target: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-connect-2.png
   :alt: Connect Operation

**2.** Once connected and correctly identified, a *session* is created on the OEF-Core side.
This *session* object will be used to directly communicate with the OEF-core as well as
with other agents.

Once a session is in place, an agent can:
- Register a DataService: propose a DataService by registering a data model (a description) and wait for interested agents to contact it. Note that the actual data is not sent

.. image:: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-register.png
   :target: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-register.png
   :alt: Register Operation

- Query for a DataService: query the OEF-core for a data model with a set of constraints

.. image:: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-query.png
   :target: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-query.png
   :alt: Query Operation

- Search for agents: conduct an agent property-based search (GPS position, market type, ...)

.. image:: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-search.png
   :target: https://github.com/fetchai/oef-sdk-python/wiki/imgs/operation-search.png
   :alt: Search Operation


Agent-to-agent interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An agent spends nearly its entire lifetime in the Fetch world
interacting with other agents. An interaction is initiated by either contacting
an agent (using the ID received from a query or a search) or receiving a message
from one (in response to a registered data service or based on registered property list).
The previous operations thus served as preliminary steps in agent-to-agent interactions
by providing a mechanism for discovery.

Agents interact with each other by exchanging messages via the OEF Nodes. There are different kind of messages
they can exchange:

* simple messages, used for general-purpose information exchange;
* `FIPA <http://www.fipa.org/>`_ interaction protocol messages, to support negotiation.

Every message contains a `dialogue identifier` that specify to both ends, the sender and the recipient, the dialogue
in which the message is defined.

In the current implementation of the OEF, dialogues objects really exist only on
the agent's side. On the OEF node side, they exist only conceptually.

What is OEF Python SDK?
-----------------------

A Python SDK to develop agents interacting with each other through the OEF-core.

In the next sections, you can find more details and some examples that let you start using the APIs.

Have fun!
