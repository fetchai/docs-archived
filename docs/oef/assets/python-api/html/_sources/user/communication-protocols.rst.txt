.. _communication-protocols:

Communication Protocols
========================

OEF agents can communicate with two categories of entities:

* an OEF Node.
* another OEF agent, via an OEF Node.

In this section, we will explain all the possible interaction with one of the cited categories of recipients.

You can check the `.proto` files that define the exchanged messages in the
`oef-core-protocol <https://github.com/fetchai/oef-core-protocol.git>`_ repository.

Interaction with the OEF Node
------------------------------

An agent can interact with the OEF for the following purposes:

* Establish a connection: `Handshake`
* Register/Unregister as an Agent (in the `Agent Directory`, see :ref:`introduction`)
* Register/Unregister as a Service (in the `Service Directory`, see :ref:`introduction`)
* Search other agents/services

The main difference between the `Agent Directory` and the `Service Directory` is that:

* the former is more general-purpose, whereas the latter is thought to be used by sellers of resources/data.
* in the former one, an agent can register himself with only one description at a time, whereas in the latter
  a service agent can register himself multiple time with a different description (and hence discoverable
  in multiple ways).

Every message has a `message id` field, that is used from the OEF Node to refer to a specific
message, e.g. for error handling (see `Error Handling`_).

It is important to notice that most of the above-mentioned methods are `asynchronous`, which means that the agent does not
waits explicitly for the result of the operations.

Establish a connection: `Handshake`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step is the `condition sine qua non` to interact with the OEF Node, and hence with other OEF agents.
It is implemented in the :func:`~oef.agents.Agent.connect` method.

.. code-block:: python

    from oef.agents import OEFAgent

    # assuming that an OEF Node is running at localhost on port 3333:
    agent = OEFAgent("agent_identifier", "127.0.0.1", 3333)

    # do the handshake
    agent.connect()

This method is synchronous; that is, the execution of the main thread waits until the connection is done.
The other

In the next sections, we assume that you already have connected the agent to an OEF Node.

Register agent
~~~~~~~~~~~~~~

In order to become discoverable from other agents, an agent can register itself in the `Agent Directory`.

To do so, we use the :func:`~oef.agents.Agent.register_agent` method:

.. code-block:: python

    from oef.schema import DataModel, AttributeSchema, Description

    # define a data model about "cars"
    car_data_model = DataModel("car", [
        AttributeSchema("manufacturer", str,   True, "The name of the car manufacturer."),
        AttributeSchema("year",         int,   True, "The year of registration."),
        AttributeSchema("luxury",       bool,  True, "Whether the car is a luxury car."),
        AttributeSchema("price",        float, True, "The price of the car."),
    ])

    # define the description of our
    agent_description = Description({
        "manufacturer": "Ferrari",
        "year":         2015,
        "luxury":       True,
        "price":        150000.0
        }, car_data_model)

    # register the agent in the Agent Directory
    msg_id = 0
    agent.register_agent(msg_id, agent_description)


Unregister agent
~~~~~~~~~~~~~~~~

We can unregister an agent by using the method :func:`~oef.agents.Agent.unregister_agent`:

Using the previous example:

.. code-block:: python

    msg_id = 1
    agent.unregister_agent(msg_id)


Notice that we don't need to use a description since our agent in the `Agent Directory` is uniquely identified
by the `public key` of the agent.

Register service
~~~~~~~~~~~~~~~~

We can register an agent as a service in the `Service Directory`
by using the method :func:`~oef.agents.Agent.register_service`:


.. code-block:: python

    from oef.schema import DataModel, AttributeSchema, Description

    # define a data model about "bookshops"
    bookshop_data_model = DataModel("bookshop", [
        AttributeSchema("name",        str,   True,  "The name of the bookshop."),
        AttributeSchema("city",        str,   True,  "The city where the bookshop is located."),
        AttributeSchema("address",     str,   True,  "The address where the bookshop is located."),
        AttributeSchema("online",      bool,  False, "Whether it provides online catalog and purchases."),
        AttributeSchema("second_hand", bool,  False, "Whether it is a second hand bookshop."),
    ])

    # define a description, that is an instance of the data model
    service_description = Description({
        "name":         "John Smith's Bookshop",
        "city":         "Cambridge",
        "address":      "Helmore Building, Anglia Ruskin University, Cambridge Campus",
        "second_hand":  False

    }, bookshop_data_model)

    msg_id = 0
    agent.register_service(msg_id, service_description)

Notice: nothing prevents us to register `the same agent` (with the same public key) in the Agent Directory,
or as another type of service in the `Service Directory`.

Unregister service
~~~~~~~~~~~~~~~~~~

We can unregister a service with a given description from the `Service Directory`
by using the method :func:`~oef.agents.Agent.unregister_service`:

Continuing with the bookshop example:

.. code-block:: python

    msg_id = 1
    agent.unregister_service(msg_id, service_description)


Notice that, differently from the :func:`~oef.agents.Agent.unregister_agent` described before, we need to
provide the description that we used when registered because we might have registered our service
with multiple descriptions.


Search agents
~~~~~~~~~~~~~

In order to find other agents, we have to query the OEF Node about the kind of agents we are interested in.

To do so, we can use the API provided by the :mod:`~oef.query` module and building :class:`~oef.query.Query` object
as explained in :ref:`query-language`

Once our query is ready, we can use the :func:`~oef.agents.Agent.search_agents` method.

Suppose we want to search cars whose manufacturer is ``Ferrari``. Continuing with the definition of the data model
`in this section <#register-agent>`__.

.. code-block:: python

    from oef.query import Query, Constraint, Eq

    # specify a query to be evaluated by the OEF Node
    # on the Agent Directory descriptions.
    ferrari_query = Query([
        Constraint("manufacturer", Eq("Ferrari"))
    ], car_data_model)

    # specify a search id. This id will be used by the
    # OEF Node to refer to the right search request when
    # it will send back the result.
    search_id = 0
    agent.search_agents(search_id, ferrari_query)

    # NOTICE: you have to implement `on_search_result` to handle the search result from the OEF Node.
    agent.run()


The :func:`~oef.agents.Agent.search_agents` function will send the search message to the OEF Node, which eventually will answer with a
*list of the public keys* of agents satisfying the query.

In this specific case, the OEF Node will return a list of the public keys of all the OEF agents that:

- are successfully registered in the `Agent Directory`;
- are registered with the ``car_data_model``;
- their manufacturer is ``Ferrari``.

The :func:`~oef.agents.Agent.run` is mandatory to receive the search result. Indeed, the main loop of the agent
will automatically call the :func:`~oef.agents.Agent.on_search_result` method implemented by the class, as soon as the
search result message has been received.

Hence, to specify a behaviour when a search result is called, you need to:

- extend the class :class:`~oef.agents.OEFAgent`
- override the :func:`~oef.agents.Agent.on_search_result` method.

.. code-block:: python

    class MyAgent(OEFAgent):

        def on_search_result(self, search_id: int, agents: List[str]):
            ...

The following sequence diagram depicts the sequence of messages exchanged between the OEF Node and the agent that
sent the search request.

.. mermaid:: ../diagrams/search_agents.mmd


Search services
~~~~~~~~~~~~~~~

The :func:`~oef.agents.Agent.search_services` method is the analogous counterpart of the
:func:`~oef.agents.Agent.search_agents`, but used to discover services in the `Service Directory`.

Suppose we want to search bookshop located in ``Cambridge``. Continuing with the definition of the data model
`in this section <#register-service>`__.

.. code-block:: python

    from oef.query import Query, Constraint, Eq

    # specify a query to be evaluated by the OEF Node
    # on the Service Directory descriptions.
    cambridge_query = Query([
        Constraint("city", Eq("Cambridge"))
    ], bookshop_data_model)

    # specify a search id. This id will be used by the
    # OEF Node to refer to the right search request when
    # it will send back the result.
    search_id = 0
    agent.search_services(0, cambridge_query)

    # wait for events
    agent.run()


The :func:`~oef.agents.Agent.search_services` function will send the search message to the OEF Node,
which eventually will answer with a *list of the public keys* of services satisfying the query.

In this specific case, the OEF Node will return a list of the public keys of all the OEF service agents that:

- are successfully registered in the `Service Directory`;
- are registered with the ``bookshop_data_model``;
- their "city" field has value ``Cambridge``.

The :func:`~oef.agents.Agent.run` is mandatory to receive the search result. Indeed, the main loop of the agent
will automatically call the :func:`~oef.agents.Agent.on_search_result` method implemented by the class,
as soon as the search result message has been received.

Hence, to specify a behaviour when a search result is called, you need to:

- extend the class :class:`~oef.agents.Agent`
- override the :func:`~oef.core.Agent.on_search_result` method.

.. code-block:: python

    class MyAgent(OEFAgent):

        def on_search_result(self, search_id: int, agents: List[str]):
            ...


The following sequence diagram depicts the sequence of messages exchanged between the OEF Node and the agent that
sent the search request.

.. mermaid:: ../diagrams/search_services.mmd


Disconnect
~~~~~~~~~~

To explicitly disconnect the agent from the OEF Node:

.. code-block:: python

    agent.disconnect()

It's not a mandatory step, but it is a good practice to clean up the allocated resources.


Interaction with other OEF Agents
---------------------------------

In this section we explain the main two methods to communicate with other OEF agents, namely:

* using general-purpose messages
* using FIPA protocol, designed for negotiation


Using general-purpose messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OEF Node provides a way to exchange information via the method :func:`~oef.agents.Agent.send_message`.

Let's call `Sender` the sender agent and `Recipient` the recipient agent.

The `Sender` can send the message by using the :func:`~oef.agents.Agent.send_message`.
Then, the OEF Node will forward it to the `Recipient`. When the `Recipient` agent call the function
:func:`~oef.agents.Agent.run`, then it will start to read from the connection with the OEF Node, and the
:func:`~oef.agents.Agent.on_message` handler is called.


Here's the code snippet that shows how the `Sender` can send a simple message.

.. code-block:: python

    # the identifier of the message
    msg_id = 0

    # the identifier of the dialogue
    dialogue_id = 0

    # the public key of the recipient agent
    destination = "recipient"

    # the content (in bytes) of the message
    content = b"hello"

    # send the message
    sender_agent.send_message(msg_id, dialogue_id, destination, content)


On the other side, the `Recipient` must implement the :func:`~oef.agents.Agent.on_message` to specify the
behaviour when a message arrives.

The parameters ``msg_id``, ``dialogue_id`` and ``content`` below will be the same of ``msg_id``,
``dialogue_id`` and ``content`` above.
The parameter ``origin`` will be the public key of the sender, ``"sender"``.


.. code-block:: python


    class RecipientAgent(OEFAgent):

        def on_message(msg_id: int, origin: str, dialogue_id: int, content: bytes):
            ...

Here follows the sequence diagram that depicts the message exchange:

.. mermaid:: ../diagrams/simple_messages.mmd


Using FIPA for negotiation
~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section, we explain a more complex protocol designed to facilitate negotiation.

It follows FIPA specifications. Citing
`Wikipedia <https://en.wikipedia.org/wiki/Foundation_for_Intelligent_Physical_Agents>`_:

    The Foundation for Intelligent Physical Agents (FIPA) is a body for developing and setting computer software
    standards for heterogeneous and interacting agents and agent-based systems.

The most simple use case one can think of is an agent (let's call him `buyer`) that wants to buy
some resources from another agent (the `seller`).

The protocol consists of four types of messages:

- `Call for Proposals` (or `CFP`), used by the buyer for asking resources and their price to the seller.
- `Propose`, the actual proposal in a negotiation.
- `Accept`, meaning that the sender accepts a previous `Propose` of his opponent.
- `Decline`, meaning that the sender is not interested anymore in continuing the negotiation.

Every message contains the following information:

* `dialogue id`: the identifier of the dialogue in which the message is sent.
* `destination`: the agent identifier to whom the message is sent.
* `message id`: the message identifier for the dialogue.
* `target`: the identifier of the message to whom this message is answering.

plus some other parameters, depending on the message.


We assume that the communication is alternating between the `Buyer` and the `Seller`. That is,
first is the `Buyer` that has the right to speak, then the `Seller`, then the `Buyer` again etc.

In the following sections, we will briefly describe how to send and receive these messages with the SDK.


CFP
```

The `CFP` (`Call For Proposals`) message is used to start the negotiation.

You can use the method :func:`~oef.agents.Agent.send_cfp` to send a `CFP` message.

Besides the fields described above, you need to define the query associated with the Call For Proposals.
It can be one of:

    * :class:`~oef.query.Query`: the `Seller` will answer with the resources matching the query.
    * ``bytes``: a generic information that should make sense to the ``Seller``
    * ``None``: a `CFP` that do not specify any constraint.


.. code-block:: python

    # the identifier of the dialogue
    dialogue_id = 0

    # the public key of the seller agent
    destination = "seller"

    # the message id and the target of the message.
    # since the CFP is the first message in the dialogue, target doesn't point to any message
    msg_id = 1
    target = 0

    # the query associated with the Call For Proposals
    # in this case, the query is empty.
    from oef.query import Query
    query = Query([])

    # send the CFP
    agent.send_cfp(dialogue_id, msg_id, destination, target, query)


On the other side, the `Seller` should implement the :func:`~oef.agents.Agent.on_cfp` to specify the
behaviour when a message arrives.

The parameters ``dialogue_id``, ``msg_id``, ``target`` and ``query`` below will be the same of above.
The parameter ``origin`` will be the public key of the sender (in this case ``"buyer"``).


.. code-block:: python


    class Seller(OEFAgent):

        def on_cfp(self, msg_id: int,
                   dialogue_id: int,
                   origin: str,
                   target: int,
                   query: CFP_TYPES) -> None:
            ...

Here follows the sequence diagram that depicts the message exchange:

.. mermaid:: ../diagrams/cfp.mmd


Propose
```````

The `Propose` message is used to make a proposal to the opponent of the negotiation.
It can answer to a `CFP` or another `Propose` (in that case it would be a counter-`Propose`).

You can use the method :func:`~oef.agents.Agent.send_propose` to send a `Propose` message.

Besides the fields described above, you need to define the actual proposal.
It can be one of:

    * a list of :class:`~oef.schema.Description`: the `Seller` will answer with the resources matching the query.
    * ``bytes``: a generic information that should make sense to the opponent.

Assume, for example, that the following code is executed inside the :func:`~oef.agents.Agent.on_cfp` of
the `Seller`.

.. code-block:: python

    class Seller(OEFAgent):

        def on_cfp(self, msg_id: int,
                   dialogue_id: int,
                   origin: str,
                   target: int,
                   query: CFP_TYPES) -> None:

            # do some stuff with the query
            ...

            # the target becomes the message we just received
            new_target = msg_id

            # we increment the message id
            new_msg_id = msg_id + 1

            # make the proposal - either a list of Description or `bytes`
            proposal = [description_1, description_2, ...]

            # send the Propose
            agent.send_propose(dialogue_id, destination, proposal, new_msg_id, new_target)


On the other side, the opponent should implement the :func:`~oef.agents.Agent.on_propose` to specify the
behaviour when a message arrives.

The parameters ``dialogue_id``, ``msg_id``, ``target`` and ``proposal`` below will be the same of above.
The parameter ``origin`` will be the public key of the sender (in this case ``"seller"``).


.. code-block:: python


    class Buyer(OEFAgent):

        def on_propose(self, msg_id: int,
                       dialogue_id: int,
                       origin: str,
                       target: int,
                       proposals: PROPOSE_TYPES) -> None:
            ...

Here follows the sequence diagram that depicts the message exchange:

.. mermaid:: ../diagrams/propose.mmd


Accept
```````


The `Accept` message is used to accept one of the previous `Propose`, and it ends the negotiation.
Obviously, both the `Buyer` and the `Seller` can accept one of the previous opponent's proposals.

You can use the method :func:`~oef.agents.Agent.send_accept` to send a `Accept` message.

Assume, for example, that the following code is executed inside the :func:`~oef.agents.Agent.on_propose` of
the `Buyer`.

.. code-block:: python

    class Buyer(OEFAgent):

        def on_propose(self, msg_id: int,
                       dialogue_id: int,
                       origin: str,
                       target: int,
                       proposals: PROPOSE_TYPES) -> None:

            # do some stuff with the proposal
            ...

            # the target is the id of the Propose we want to accept.
            new_target = msg_id

            # we increment the message id
            new_msg_id = msg_id + 1

            # send the Accept
            agent.send_accept(dialogue_id, destination, new_msg_id, new_target)


On the other side, the `Seller` should implement the :func:`~oef.agents.Agent.on_accept` to specify the
behaviour when a message arrives.

The parameters ``dialogue_id``, ``msg_id``, ``target`` below will be the same of above.
The parameter ``origin`` will be the public key of the sender (in this case ``"buyer"``).


.. code-block:: python


    class Seller(OEFAgent):

        def on_accept(self, msg_id: int,
                      dialogue_id: int,
                      origin: str,
                      target: int) -> None:
            ...

Here follows the sequence diagram that depicts the message exchange:

.. mermaid:: ../diagrams/accept.mmd

Notice that:

* There might have been other counter- `Propose` s between both parties
* Both the `Buyer` and the `Seller` can send an `Accept`, but only when is its turn.



Decline
```````

The `Decline` message is used to decline any propose, and it ends the negotiation.
Obviously, both the `Buyer` and the `Seller` can send a `Decline`.

The `Decline`'s target must be the `CFP` that initiated the negotiation. It can be even sent by the `Seller` on the
`Buyer` 's `CFP`.

You can use the method :func:`~oef.agents.Agent.send_decline` to send a `Decline` message.

Assume, for example, that the following code is executed inside the :func:`~oef.agents.Agent.on_propose` of
the `Buyer`.

.. code-block:: python

    class Buyer(OEFAgent):

        def on_propose(self, msg_id: int,
                       dialogue_id: int,
                       origin: str,
                       target: int,
                       proposal: PROPOSE_TYPES) -> None:

            # do some stuff with the query
            ...

            # the target is the id of the CFP.
            new_target = 0

            # we increment the message id
            new_msg_id = msg_id + 1

            # send the Decline
            agent.send_decline(dialogue_id, destination, new_msg_id, new_target)


On the other side, the `Seller` should implement the :func:`~oef.agents.Agent.on_decline` to specify the
behaviour when a message arrives.

The parameters ``dialogue_id``, ``msg_id``, ``target`` below will be the same of above.
The parameter ``origin`` will be the public key of the sender (in this case ``"buyer"``).


.. code-block:: python


    class Seller(OEFAgent):

        def on_decline(self, msg_id: int,
                       dialogue_id: int,
                       origin: str,
                       target: int) -> None:
            ...

Here follows the sequence diagram that depicts the message exchange:

.. mermaid:: ../diagrams/decline.mmd

Notice that:

* There might have been other counter- `Propose` s between both parties
* Both the `Buyer` and the `Seller` can send a `Decline`, but only when is its turn.


FIPA Examples
~~~~~~~~~~~~~

In this section, you can see some examples of how the negotiation protocol should work.

Notice that the SDK does not impose any restriction on the messages. Eventually, there will be
more API support that moves the burden of taking care of some protocol-related details, from the developer to the SDK.

You can use this `script <https://github.com/fetchai/oef-sdk-python/tree/master/examples/random_fipa/random_fipa.py>`_
to generate other simulations.

CFP - Decline
``````````````

.. mermaid:: ../diagrams/fipa_examples/cfp-decline.mmd
    :align: center
    :caption: The Seller sends a `Decline` just after a `CFP`.

CFP - Propose - Decline
````````````````````````

.. mermaid:: ../diagrams/fipa_examples/cfp-propose-decline.mmd
    :align: center
    :caption: The Buyer sends a `Decline` after the first `Seller`'s `Propose`.

CFP - Propose - Accept
``````````````````````

.. mermaid:: ../diagrams/fipa_examples/cfp-propose-decline.mmd
    :align: center
    :caption: The Buyer accepts the first `Seller`'s `Propose`.

CFP - Propose - Propose - Decline
``````````````````````````````````

.. mermaid:: ../diagrams/fipa_examples/cfp-propose-propose-decline.mmd
    :align: center
    :caption: The Seller sends a `Decline` after the `Buyers`'s counter-`Propose`.


CFP - Propose - Propose - Accept
````````````````````````````````

.. mermaid:: ../diagrams/fipa_examples/cfp-propose-propose-accept.mmd
    :align: center
    :caption: The Seller accepts the `Buyers`'s counter-`Propose`.


.. _error-handling:

Error Handling
--------------

The OEF supports two ways to report errors:

- One related to the interactions with the OEF: `OEF Errors`
- One related to the interactions with other agents: `Dialogue Errors`.

OEF Error
~~~~~~~~~

The OEF Error is sent back to an OEF Agent when a particular operation he submitted fail for some
reason.

More specifically, if an agent receives an OEF Error, one of the following problems might have happened:

- following a :func:`~oef.agents.Agent.register_agent` request, if the description received by the OEF Node is invalid.
- following a :func:`~oef.agents.Agent.register_service` request, if something fails when the OEF Node try to store the
  service description in the Service Directory.
- following a :func:`~oef.agents.Agent.unregister_service` request, when we tries to unregister a non-existent
  service.

In order to correctly handle an OEF Error message, you have to specify the behaviour
of the :func:`~oef.agents.Agent.on_oef_error` method.

.. code-block:: python

    class MyAgent(OEFAgent):

        def on_oef_error(self, answer_id: int, operation: OEFErrorOperation):
            ...


The ``answer_id`` parameter will be the same of the ``msg_id`` used to submit the request.
The ``operation`` parameter specify which kind of error has been received.
See :class:`~oef.messages.OEFErrorOperation` for further details.

Dialogue Error
~~~~~~~~~~~~~~

The Dialogue Error is sent back to an OEF Agent when a particular operation he submitted fail for some
reason.

More specifically, if an agent receives a Dialogue Error, one of the following problems might have happened:

- following a :func:`~oef.agents.Agent.send_message` (or any ``send_*`` method), if the destination is not currently connected.


In order to correctly handle a Dialogue Error message, you have to specify the behaviour
of the :func:`~oef.agents.Agent.on_dialogue_error` method.


.. code-block:: python

    class MyAgent(OEFAgent):

        def on_dialogue_error(self, answer_id: int, dialogue_id: int, origin: str):
            ...

The ``answer_id``, ``dialogue_id`` and ``origin`` parameters will be the same of, respectively,
the ``msg_id``, ``dialogue_id`` and ``destination`` parameter used to send the agent message.

