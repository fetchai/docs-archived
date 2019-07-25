.. _quickstart:

Quickstart
==========

This is a quick start guide, for the eager users.

Install
-------

Try the following installation instructions. If you have some troubles,
we recommend following the full installation guide: :ref:`install`.

Depending on your platform, do one of the following:

* On Linux Ubuntu:

.. code-block:: bash

  sudo apt-get install protobuf-compiler
  git clone https://github.com/fetchai/oef-sdk-python.git --recursive
  cd oef-sdk-python/
  sudo python3 setup.py install


* On Mac OS X:

.. code-block:: bash

  brew install protobuf
  git clone https://github.com/fetchai/oef-sdk-python.git --recursive
  cd oef-sdk-python/
  sudo python3 setup.py install


* For other platforms and additional details,
  please follow the installation guide: :ref:`install`.


Run an OEF Node
---------------

For full details about how to run an OEF Node, please follow the instructions at this page: :ref:`oef-node`.

Using Docker
~~~~~~~~~~~~

In a separate terminal:

.. code-block:: bash

  # clone the repo for the OEF node
  git clone https://github.com/fetchai/oef-core.git --recursive && cd oef-core/

  # build the docker image
  ./oef-core-image/scripts/docker-build-img.sh

  # run the image
  ./oef-core-image/scripts/docker-run.sh -p 3333:3333 -d --

When finished, you can stop the image by running the following:

.. code-block:: bash

  docker stop $(docker ps | grep oef-core-image | awk '{ print $1 }')


Connect Agents
--------------

With the OEF Node running, we can start to connect agents.


Write Agents
~~~~~~~~~~~~

The ``GreetingsAgent`` behaviour is implemented in the following callbacks:

* :func:`~oef.agents.Agent.on_search_result`: Once the agent receives results from its search,
  the agent sends a ``"hello"`` message to each agent discovered.
* :func:`~oef.agents.Agent.on_message`: whenever the agent receives a ``"hello"`` message,
  it answers with ``"greetings"``.


.. code-block:: python

    from typing import List
    from oef.agents import OEFAgent

    class GreetingsAgent(OEFAgent):
        """A class that implements the greeting agent."""

        def on_message(self, msg_id: int, dialogue_id: int, origin: str, content: bytes):
            print("[{}]: Received message: msg_id={}, dialogue_id={}, origin={}, content={}"
                  .format(self.public_key, msg_id, dialogue_id, origin, content))
            if content == b"hello":
                print("[{}]: Sending greetings message to {}".format(self.public_key, origin))
                self.send_message(1, dialogue_id, origin, b"greetings")
                self.stop()
            if content == b"greetings":
                self.stop()

        def on_search_result(self, search_id: int, agents: List[str]):
            if len(agents) > 0:
                print("[{}]: Agents found: {}".format(self.public_key, agents))
                for a in agents:
                    self.send_message(0, 0, a, b"hello")
            else:
                print("[{}]: No agent found.".format(self.public_key))
                self.stop()


Start Communications
~~~~~~~~~~~~~~~~~~~~

* Instantiate agents:

.. code-block:: python

    client_agent = GreetingsAgent("greetings_client", oef_addr="127.0.0.1", oef_port=3333)
    server_agent = GreetingsAgent("greetings_server", oef_addr="127.0.0.1", oef_port=3333)

* Connect them to the OEF:

.. code-block:: python

    client_agent.connect()
    server_agent.connect()

* The server agent registers itself as a greetings service on the OEF:

.. code-block:: python

    from oef.schema import DataModel, Description, AttributeSchema
    say_hello = AttributeSchema("say_hello", bool, True, "The agent answers to 'hello' messages.")
    greetings_model = DataModel("greetings", [say_hello], "Greetings service.")
    greetings_description = Description({"say_hello": True}, greetings_model)
    server_agent.register_service(0, greetings_description)

* The client agent executes the search for greetings services:

.. code-block:: python

    from oef.query import Query, Constraint, Eq
    # the client executes the search for greetings services
    # we are looking for services that answers to "hello" messages
    query = Query([Constraint("say_hello", Eq(True))], greetings_model)

    print("[{}]: Search for 'greetings' services. search_id={}".format(client_agent.public_key, 0))
    client_agent.search_services(0, query)

When the ``client_agent`` receives a search result from the OEF, the ``on_search_result`` method is executed.

* Execute both agents concurrently

.. code-block:: python

    import asyncio
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(
            client_agent.async_run(),
            server_agent.async_run()))
    finally:
        client_agent.stop()
        server_agent.stop()

        client_agent.disconnect()
        server_agent.disconnect()

The output should be:

.. code-block:: none

    [greetings_client]: Search for 'greetings' services. search_id=0
    [greetings_client]: Agents found: ['greetings_server']
    [greetings_server]: Received message: msg_id=0, dialogue_id=0, origin=greetings_client, content=b'hello'
    [greetings_server]: Sending greetings message to greetings_client
    [greetings_client]: Received message: msg_id=1, dialogue_id=0, origin=greetings_server, content=b'greetings'


You can find the full script at
`this link <https://github.com/fetchai/oef-sdk-python/tree/master/examples/greetings/greeting_agents.py>`_.
and the `Jupyter notebook version
<https://github.com/fetchai/oef-sdk-python/tree/master/examples/greetings/greeting_agents.ipynb>`_.

You can also try another version that uses the local implementation of an OEF Node:
`link <https://github.com/fetchai/oef-sdk-python/tree/master/examples/greetings/local_greeting_agents.py>`_.

In :ref:`tutorial` you might find all the details and how to implement more complex behaviours.
