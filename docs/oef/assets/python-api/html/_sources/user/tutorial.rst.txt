.. _tutorial:

First OEF Agents
================

In this guide, we show you some examples of how to develop and run OEF agents.


Initialization
--------------


Setup an OEF Node
~~~~~~~~~~~~~~~~~

To be able to follow the following examples, we need to set up an OEF Node.
This node will manage the discovery of agents
and the communications between agents.

Please follow the instruction in this page about how to run an OEF Node: :ref:`oef-node`.


Optional: set up the logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It might be useful to see logging messages to better understand what happens behind the scenes.

To do so, run the following instructions at the beginning of your scripts:

.. code-block:: python

    import logging
    from oef.logger import set_logger
    set_logger("oef.agents", logging.DEBUG)


First example: Echo agent
---------------------------

In this section, we will develop an `echo agent`. That is, whenever it receives a message from another agent, it replies
with the same message.

First, we define the service agent that implements the echo service.
Then, we implement other client agents to interact with the echo service.

The code for the example can be found at this
`link <https://github.com/fetchai/oef-sdk-python/tree/master/examples/echo>`_.

Echo Agent service
~~~~~~~~~~~~~~~~~~

Let's start to implement the echo service agent.
To do so, we define a new class, ``EchoServiceAgent``, which extends
the ``OEFAgent`` class and redefines the behaviour of the :func:`~oef.agents.Agent.on_message` method.

The :func:`~oef.agents.Agent.on_message` method of an agent is called whenever
the agent is one of the intended recipients of the message.
In this case, we just send the message back
to the sender through the OEF.

In later examples, we will see a more complex protocol and
how to implement the associated callbacks.

.. code-block:: python

    from oef.agents import OEFAgent

    class EchoServiceAgent(OEFAgent):
        """
        The class that defines the behaviour of the echo service agent.
        """

        def on_message(self, msg_id: int, dialogue_id: int, origin: str, content: bytes):
            print("[{}]: Received message: msg_id={}, dialogue_id={}, origin={}, content={}"
                  .format(self.public_key, msg_id, dialogue_id, origin, content))
            print("[{}]: Sending {} back to {}".format(self.public_key, content, origin))
            self.send_message(1, dialogue_id, origin, content)

Connect to the OEF
``````````````````

In order to connect a (service) agent to the OEF, we need to specify:

* A unique identifier for the agent;
* The IP address and port of the OEF Node on which we want to register;

We will use ``echo_server`` as the identifier.
Choose the IP address and port pair provided by the OEFNode instance.
In this example, the IP address and the port pair will be
``127.0.0.1`` and ``3333``, respectively.

.. code-block:: python

    # create agent and connect it to OEF
    server_agent = EchoServiceAgent("echo_server", oef_addr="127.0.0.1", oef_port=3333)
    server_agent.connect()

Define a Data Model and a Description
``````````````````````````````````````

In order to make our agent discoverable to other agents, we need to define a `description` (an instance of a schema),
which refers to a `data model` (abstract definition of the schema).
In this way, other agents can find our service by making `queries` (defined over the same data model) to the OEF.

.. code-block:: python

    from oef.schema import DataModel, Description, AttributeSchema
    echo_feature = AttributeSchema("does_echo", bool, True, "Whether the service agent can do echo or not.")
    echo_model = DataModel("echo", [echo_feature], "echo data service.")
    echo_description = Description({"does_echo": True}, echo_model)


Our data model ``echo_model`` is very straightforward. It has only one boolean attribute, `"does_echo"`,
that specify if a service can answer to an echo request.

The ``echo_description`` is the instantiation of our abstract
data model ``echo`` and defined accordingly. Since our service provides the echo service, we set the ``"does_echo"``
field to ``True`` such that it will be discoverable by other agents.

For further details, please look at the documentation of :class:`~oef.schema.AttributeSchema`,
:class:`~oef.schema.DataModel` and :class:`~oef.schema.Description`.

Register the service
````````````````````

Now that we have a description of our service, let's register our service agent to the OEF, by using
:func:`~oef.agents.Agent.register_service`:

.. code-block:: python

    msg_id = 0
    server_agent.register_service(msg_id, echo_description)


This instruction will notify the OEF Node that there is a new service available. The message id ``msg_id``
parameter will be used by the OEF Node to reference that request if something goes badly.

When another agent makes a query on the ``echo_model``, if the ``echo_description``
satisfies the constraint of the query's constraints, then our agent will be one of the results.


Run the agent
`````````````
To run the agent waiting for messages:

.. code-block:: python

    try:
        print("[{}]: Waiting for messages...".format(server_agent.public_key))
        server_agent.run()
    finally:
        print("[{}]: Disconnecting...".format(server_agent.public_key))
        server_agent.stop()
        server_agent.disconnect()


The :func:`~oef.agents.Agent.run` method is blocking, so you have to switch to another terminal/console to launch the client.

For some particular use cases,
you may want to use :func:`~oef.agents.Agent.async_run`, which is the associated ``async`` method.


In the ``finally`` clause, we call the :func:`~oef.agents.Agent.stop` method to be sure that our agent has no
pending work to do.

Then, we disconnect the agent from the OEF Node.
It is a good practice to explicitly disconnect the agent after the work is done.
The :func:`~oef.agents.Agent.disconnect` method explicitly closes the connection with the OEF Node.


Echo Agent client
~~~~~~~~~~~~~~~~~

The `EchoClientAgent` implements our `echo client`, which is
the consumer of the service we implemented in the previous section.

.. code-block:: python

    from typing import List

    from oef.agents import OEFAgent

    class EchoClientAgent(OEFAgent):
        """
        The class that defines the behaviour of the echo client agent.
        """

        def on_message(self, msg_id: int, dialogue_id: int, origin: str, content: bytes):
            print("[{}]: Received message: msg_id={}, dialogue_id={}, origin={}, content={}"
                  .format(self.public_key, msg_id, dialogue_id, origin, content))
            print("[{}]: Stopping...".format(self.public_key))
            self.stop()

        def on_search_result(self, search_id: int, agents: List[str]):
            if len(agents) > 0:
                print("[{}]: search_id={}. Agents found: {}".format(self.public_key, search_id, agents))
                msg = b"hello"
                for agent in agents:
                    print("[{}]: Sending {} to {}".format(self.public_key, msg, agent))
                    self.send_message(0, 0, agent, msg)
            else:
                print("[{}]: No agent found. Stopping...".format(self.public_key))
                self.stop()


The :func:`~oef.agents.Agent.on_message` method has the same semantics as the one implemented
in the ``EchoServiceAgent`` class. In this case,
we don't implement any complex behaviour (we just print the received message).

The :func:`~oef.agents.Agent.on_search_result` callback is called whenever the agent receives
a search result of a search query with
:func:`~oef.agents.Agent.search_agents` or :func:`~oef.agents.Agent.search_services` methods.

In our case, the agent just sends a ``"hello"`` message (in bytes) to every discovered service,
by using the :func:`~oef.agents.Agent.send_message`  method.

Connect to the OEF
``````````````````

Analogously to the previous section, we connect our client to the OEF.

.. code-block:: python

    client_agent = EchoClientAgent("echo_client", oef_addr="127.0.0.1", oef_port=3333)
    client_agent.connect()


Make a query
````````````

Now we need to search for agents who provide the ``echo`` service.

To do so, we create a :class:`~oef.query.Query` referring to the ``echo`` data model. The first parameter is a list
of *constraints* over the attributes of the data model. However, since our data model is trivial,
our query just returns all the agents that are registered with the ``echo`` data model.

.. code-block:: python

    # create a query for the echo data model
    from oef.schema import DataModel, AttributeSchema
    from oef.query import Query, Constraint, Eq
    echo_feature = AttributeSchema("does_echo", bool, True, "Whether the service agent can do echo.")
    echo_model = DataModel("echo", [echo_feature], "echo service.")
    echo_query = Query([Constraint("does_echo", Eq(True))], echo_model)


Search for services
```````````````````

Once we have a query, we can ask the OEF to return
all service agents that satisfy the given constraints.

.. code-block:: python

    print("[{}]: Make search to the OEF".format(client_agent.public_key))
    client_agent.search_services(0, echo_query)

Wait for search results
```````````````````````

The client agent needs to wait for search results from the OEF Node:

.. code-block:: python

    # wait for events
    try:
        client_agent.run()
    finally:
        print("[{}]: Disconnecting...".format(client_agent.public_key))
        client_agent.stop()
        client_agent.disconnect()

The clean up of the allocated resources is analogous to the one shown before for the ``EchoServiceAgent``.

Once the OEF Node computes the results, the :func:`~oef.agents.Agent.on_search_result` callback is called.


Message Exchange
~~~~~~~~~~~~~~~~


If you run the agents in different consoles, you can check the log messages that they produced.

The output from the client agent should be:

::

   [echo_client]: Make search to the OEF
   [echo_client]: search_id=0. Agents found: ['echo_server']
   [echo_client]: Sending b'hello' to echo_server
   [echo_client]: Received message: msg_id=1, dialogue_id=0, origin=echo_server, content=b'hello'
   [echo_client]: Stopping...
   [echo_client]: Disconnecting...

Whereas, the one from the server agent is:

::

   [echo_server]: Waiting for messages...
   [echo_server]: Received message: msg_id=0, dialogue_id=0, origin=echo_client, content=b'hello'
   [echo_server]: Sending b'hello' back to echo_client


The order of the exchanged message is the following:

1. The service agent ``echo_server`` registers itself to the OEF Node and waits for messages.
2. The ``echo_client`` queries to the OEF Node
3. The OEF Node sends back the list of agents who satisfy
   the query constraints. In this trivial example,
   the only agent returned is the ``echo_server``.
4. The client sends a ``"hello"`` message to the OEF Node,
   which targets the ``echo_server``
5. The OEF Node dispatches the message from ``echo_client`` to ``echo_server``
6. The ``echo_server`` receives the message and sends a new message (with the same content)
   to the OEF Node, which targets the ``echo_client``
7. The OEF Node dispatch the message from ``echo_server`` to ``echo_client``
8. The ``echo_client`` receives the echo message.

Follows the sequence diagram with the message exchange.

.. mermaid:: ../diagrams/echo_example.mmd
    :alt: Sequence diagram for the Echo example.
    :align: center
    :caption: The exchange of messages in the Echo example.



Second example: Weather Station
-------------------------------

In this second example, consider the following scenario:

* A `weather station` provides measurements of
  some physical quantity (e.g. wind speed, temperature, air pressure)
* A `weather client` is interested in these measurements.

The owner of the weather station wants to sell the data it measures.
In the following sections, we describe a
protocol that allows the agents to:

* request resources (physical assets, services, information etc.)
* make price proposals on the negotiated resources
* accept/decline proposals.


You can check the full code `here <https://github.com/fetchai/oef-sdk-python/tree/master/examples/weather>`_.


Weather Station Agent
~~~~~~~~~~~~~~~~~~~~~

Define a DataModel
``````````````````

For this example, we need a specific data model that can effectively describe the features of services.


Let's start with an attribute to represent whether a weather station provides a measure for physical quantities, e.g.
wind speed:

.. code-block:: python

    from oef.schema import AttributeSchema

    WIND_SPEED_ATTR = AttributeSchema(
        "wind_speed",
        bool,
        is_attribute_required=True,
        attribute_description="Provides wind speed measurements."
    )


The :class:`~oef.schema.AttributeSchema` class constructor requires:

- The name of the attribute;
- The type of the attribute: it can be one of ``int``, ``float``, ``bool`` and ``str``;
- A flag to determine whether the instances of the data model (that is :class:`~oef.schema.Description`) need to specify a value;
- A description of the meaning of the attribute.

In this case, our ``wind_speed`` attribute is of type ``bool``. If the description of a weather station has the value
``wind_speed`` set to ``True``, then it means that it can provide measurements for the wind speed.

We can define other types of measurements as well:

.. code-block:: python

    TEMPERATURE_ATTR = AttributeSchema(
        "temperature",
        bool,
        is_attribute_required=True,
        attribute_description="Provides temperature measurements."
    )

    AIR_PRESSURE_ATTR = AttributeSchema(
        "air_pressure",
        bool,
        is_attribute_required=True,
        attribute_description="Provides air pressure measurements."
    )

    HUMIDITY_ATTR = AttributeSchema(
        "humidity",
        bool,
        is_attribute_required=True,
        attribute_description="Provides humidity measurements."
    )


Now we can define our data model:

.. code-block:: python

    from oef.schema import DataModel

    WEATHER_DATA_MODEL = DataModel(
        "weather_data",
        [WIND_SPEED_ATTR,
        TEMPERATURE_ATTR,
        AIR_PRESSURE_ATTR,
        HUMIDITY_ATTR],
        "All possible weather data."
    )


To define our data model ``WEATHER_DATA_MODEL`` we need a name and a list of attributes. We use the
same we defined previously, that is ``WIND_SPEED_ATTR``, ``AIR_PRESSURE_ATTR``, ``HUMIDITY_ATTR`` and ``PRICE_ATTR``.


Define a Description
````````````````````

Once we have the data model, we can provide an `instance` of that model. To do so, we can use the
:class:`~oef.schema.Description` class:

.. code-block:: python

    from oef.schema import Description

    weather_service_description = Description(
        {
            "wind_speed": False,
            "temperature": True,
            "air_pressure": True,
            "humidity": True,
        },
        WEATHER_DATA_MODEL
    )

The first argument is a dictionary where:

- the keys are the names of the attributes;
- the values are the instantiation of the attribute schema specification.

The second argument is the data model the description is referring to.

We will use this description to register our service to the OEF. In this way, other agents can make queries defined over
the data model ``WEATHER_DATA_MODEL`` and discover the service.

Define the WeatherStation agent
```````````````````````````````

This is the code for our weather station:

.. code-block:: python

   from oef.agents import OEFAgent
   from oef.schema import Description
   from oef.messages import CFP_TYPES
   import json


    class WeatherStation(OEFAgent):
        """Class that implements the behaviour of the weather station."""

        weather_service_description = Description(
            {
                "wind_speed": False,
                "temperature": True,
                "air_pressure": True,
                "humidity": True,
            },
            WEATHER_DATA_MODEL
        )

        def on_cfp(self, msg_id: int, dialogue_id: int, origin: str, target: int, query: CFP_TYPES):
            """Send a simple Propose to the sender of the CFP."""
            print("[{0}]: Received CFP from {1}".format(self.public_key, origin))

            # prepare the proposal with a given price.
            price = 50
            proposal = Description({"price": price})
            print("[{}]: Sending propose at price: {}".format(self.public_key, price))
            self.send_propose(msg_id + 1, dialogue_id, origin, target + 1, [proposal])

        def on_accept(self, msg_id: int, dialogue_id: int, origin: str, target: int):
            """Once we received an Accept, send the requested data."""
            print("[{0}]: Received accept from {1}."
                  .format(self.public_key, origin))

            # send the measurements to the client. for the sake of simplicity, they are hard-coded.
            data = {"temperature": 15.0, "humidity": 0.7, "air_pressure": 1019.0}
            encoded_data = json.dumps(data).encode("utf-8")
            print("[{0}]: Sending data to {1}: {2}".format(self.public_key, origin, pprint.pformat(data)))
            self.send_message(0, dialogue_id, origin, encoded_data)



* when the agent receives a CFP, it answers with a list of relevant resources, that constitutes his proposal.
  In this simplified example, he answers with only one Description object, that specifies the price of the negotiation.
* on Accept messages, he answers with the available measurements. For the sake of simplicity, they are hard-coded.

And here is the code to run the agent:

.. code-block:: python


    agent = WeatherStation("weather_station", oef_addr="127.0.0.1", oef_port=3333)
    agent.connect()
    agent.register_service(0, agent.weather_service_description)

    print("Waiting for clients...")
    try:
        agent.run()
    finally:
        agent.stop()
        agent.disconnect()


Weather Client Agent
~~~~~~~~~~~~~~~~~~~~~

This is the code for the client of the weather service:

.. code-block:: python

    from typing import List
    import pprint
    from oef.agents import OEFAgent
    from oef.messages import PROPOSE_TYPES
    import json

    class WeatherClient(OEFAgent):
        """Class that implements the behavior of the weather client."""

        def on_search_result(self, search_id: int, agents: List[str]):
            """For every agent returned in the service search, send a CFP to obtain resources from them."""
            if len(agents) == 0:
                print("[{}]: No agent found. Stopping...".format(self.public_key))
                self.stop()
                return

            print("[{0}]: Agent found: {1}".format(self.public_key, agents))
            for agent in agents:
                print("[{0}]: Sending to agent {1}".format(self.public_key, agent))
                # we send a 'None' query, meaning "give me all the resources you can propose."
                query = None
                self.send_cfp(1, 0, agent, 0, query)

        def on_propose(self, msg_id: int, dialogue_id: int, origin: str, target: int, proposals: PROPOSE_TYPES):
            """When we receive a Propose message, answer with an Accept."""
            print("[{0}]: Received propose from agent {1}".format(self.public_key, origin))
            for i, p in enumerate(proposals):
                print("[{0}]: Proposal {1}: {2}".format(self.public_key, i, p.values))
            print("[{0}]: Accepting Propose.".format(self.public_key))
            self.send_accept(msg_id, dialogue_id, origin, msg_id + 1)

        def on_message(self, msg_id: int, dialogue_id: int, origin: str, content: bytes):
            """Extract and print data from incoming (simple) messages."""
            data = json.loads(content.decode("utf-8"))
            print("[{0}]: Received measurement from {1}: {2}".format(self.public_key, origin, pprint.pformat(data)))
            self.stop()


His behaviour can be summarized with the following lines:

* When the agent receives a search result from the OEF (see :class:`~oef.agents.Agent.on_search_result`),
  it sends a CFP to every weather station found. This message starts a negotiation with every agent.
  For simplicity, the CFP contains a query with an empty list of constraints, meaning that we do not specify constraints
  on the set of proposals we can receive.
* When the agent receives a Propose message, he will automatically accept the proposal, sending an Accept message.
  Here it is possible to implement multiple strategies, e.g. find the proposal with the minimum
  across different services.
* Then he waits to receive the measurements from the weather station.

And here's the code to run it:

.. code-block:: python

    from oef.query import Query, Constraint, Eq

    agent = WeatherClient("weather_client", oef_addr="127.0.0.1", oef_port=3333)
    agent.connect()

    query = Query([Constraint(TEMPERATURE_ATTR.name, Eq(True)),
                   Constraint(AIR_PRESSURE_ATTR.name, Eq(True)),
                   Constraint(HUMIDITY_ATTR.name, Eq(True))],
                   WEATHER_DATA_MODEL)

    agent.search_services(0, query)

    try:
        agent.run()
    finally:
        agent.stop()
        agent.disconnect()


Notice how we built the :class:`~oef.query.Query` object, used to search weather services. The query requires:

* a data model over which the query is defined
* a list of :class:`~oef.query.Constraint` object. Each constraint is defined over attributes of the data
  model and imposes a restriction on the possible values that the associated attributes can assume.

In this example, we require that the :class:`~oef.schema.Description` of the services registered in the OEF
is compliant with the following conditions:

* The description is defined over the ``WEATHER_DATA_MODEL`` (defined before)
* The fields `temperature`, `humidity` and `air pressure` must be set to ``True`` (that is, the service provides the
  associated measurements.
  To specify this kind of constraint, we use the class :class:`~oef.schema.Eq` that express the constraint of equality
  to a specific value.

To give a better idea, you can think about this query as an equivalent of the following SQL-like query:

.. code-block:: sql
   :linenos:

   SELECT * FROM weather_data WHERE
     temperature = true and
     air_pressure = true and
     humidity = true;


In other sections of the documentation, you can find more details about the query language and other types of constraint.

Message Exchange
~~~~~~~~~~~~~~~~


The output from the client agent should be:

.. code-block:: none

   [weather_station]: Waiting for clients...
   [weather_station]: Received CFP from weather_client
   [weather_station]: Sending propose at price: 50
   [weather_station]: Received accept from weather_client.
   [weather_station]: sending data to weather_client: {'air_pressure': 1019.0, 'humidity': 0.7, 'temperature': 15.0}


Whereas, the one from the server agent is:

.. code-block:: none

   [weather_station]: Waiting for clients...
   [weather_station]: Received CFP from weather_client
   [weather_station]: Sending propose at price: 50
   [weather_station]: Received accept from weather_client.
   [weather_station]: sending data to weather_client: {'air_pressure': 1019.0, 'humidity': 0.7, 'temperature': 15.0}


Follows the summary of the communication between the weather client and the weather station:

1. The weather station agent registers to the OEF and waits for messages.
2. The client sends a search result with a query, looking for weather stations
   that provide measurements for temperature, humidity and air pressure.
   Then, he waits for messages.
3. The OEF answers with the services that satisfy the query.
4. The client sends a CFP to the service via the OEF Node. The node forwards it to the recipient.
5. The weather station answers with a proposal.
6. The client accepts the proposal and notifies the weather station.
7. The station sends messages to the client with the desired measurements.


Follows the sequence diagram with the message exchange.

.. mermaid:: ../diagrams/weather_example.mmd
    :alt: Sequence diagram for the Weather example.
    :align: center
    :caption: The exchange of messages in the Weather example.

Notice: in step (6), instead of the `Accept` action, we might have had a counter-Propose, or a `Decline`.
`Decline` means that the sender is not interested anymore in continuing the negotiation with the recipient.
