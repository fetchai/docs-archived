The <a href="../scaffolding/">scaffolding tool</a> allows you create the folder structure required for a skill.

!!!	Note
	Before developing your first skill, please read the <a href="../skill/">skill guide</a>.


## Step 1: Setup

Ensure, you have followed the <a href="../quickstart/">preliminaries and installation</a>. We will first create an agent and add a scaffold skill, which we call `my_search`:

``` bash
aea create my_agent && cd my_agent
aea scaffold skill my_search
```

In the following steps, we will replace each one of the scaffolded `Behaviour`, `Handler` and `Task` in `my_agent/skills/my_search` with our implementation. We will build a simple skill which lets the agent send a search query to the [OEF](https://docs.fetch.ai/oef/) and process the resulting response.


## Step 2: Develop a Behaviour

A `Behaviour` class contains the business logic specific to initial actions initiated by the agent rather than reactions to other events.

In this example, we implement a simple search behaviour. Each time, `act()` gets called by the main agent loop, we will send a search request to the OEF.

``` python
import logging
import time

from aea.protocols.oef.message import OEFMessage
from aea.protocols.oef.models import Query, Constraint, ConstraintType
from aea.protocols.oef.serialization import DEFAULT_OEF, OEFSerializer
from aea.skills.base import Behaviour

logger = logging.getLogger("aea.my_search_skill")


class MySearchBehaviour(Behaviour):
    """This class provides a simple search behaviour."""

    def __init__(self, **kwargs):
        """Initialize the search behaviour."""
        super().__init__(**kwargs)
        self.sent_search_count = 0

    def setup(self) -> None:
        """
        Implement the setup.

        :return: None
        """
        logger.info("[{}]: setting up MySearchBehaviour".format(self.context.agent_name))

    def act(self) -> None:
        """
        Implement the act.

        :return: None
        """
        time.sleep(1)  # to slow down the agent
        self.sent_search_count += 1
        search_constraints = [Constraint("country",
        	                  ConstraintType("==", "UK"))]
        search_query_w_empty_model = Query(search_constraints, model=None)
        search_request = OEFMessage(oef_type=OEFMessage.Type.SEARCH_SERVICES,
                                    id=self.sent_search_count,
                                    query=search_query_w_empty_model)
        logger.info("[{}]: sending search request to OEF, search_count={}".format(self.context.agent_name, self.sent_search_count))
        self.context.outbox.put_message(to=DEFAULT_OEF,
                                        sender=self.context.agent_address,
                                        protocol_id=OEFMessage.protocol_id,
                                        message=OEFSerializer().encode(search_request))

    def teardown(self) -> None:
        """
        Implement the task teardown.

        :return: None
        """
        logger.info("[{}]: tearing down MySearchBehaviour".format(self.context.agent_name))
```

Searches are proactive and as such well placed in a `Behaviour`.

We place this code in `my_agent/skills/my_search/behaviours.py`.


## Step 3: Develop a Handler

So far, we have tasked the agent with sending search requests to the OEF. However, we have no way of handling the responses sent to the agent by the OEF at the moment. The agent would simply respond to the OEF via the default `error` skill which sends all unrecognised envelopes back to the sender.

Let us now implement a handler to deal with the incoming search responses.


``` python
import logging

from aea.protocols.oef.message import OEFMessage
from aea.protocols.oef.serialization import OEFSerializer
from aea.skills.base import Handler

logger = logging.getLogger("aea.my_search_skill")


class MySearchHandler(Handler):
    """This class provides a simple search handler."""

    SUPPORTED_PROTOCOL = OEFMessage.protocol_id

    def __init__(self, **kwargs):
        """Initialize the handler."""
        super().__init__(**kwargs)
        self.received_search_count = 0

    def setup(self) -> None:
        """Set up the handler."""
        logger.info("[{}]: setting up MySearchHandler".format(self.context.agent_name))

    def handle(self, message: OEFMessage, sender: str) -> None:
        """
        Handle the message.

        :param message: the message.
        :param sender: the sender.
        :return: None
        """
        msg_type = OEFMessage.Type(message.get("type"))

        if msg_type is OEFMessage.Type.SEARCH_RESULT:
            self.received_search_count += 1
            nb_agents_found = len(message.get("agents"))
            logger.info("[{}]: found number of agents={}, received search count={}".format(self.context.agent_name, nb_agents_found, self.received_search_count))

    def teardown(self) -> None:
        """
        Teardown the handler.

        :return: None
        """
        logger.info("[{}]: tearing down MySearchHandler".format(self.context.agent_name))
```

We create a handler which is registered for the `oef` protocol. Whenever it receives a search result, we log the number of agents returned in the search - the agents matching the search query - and update the counter of received searches.

Note, how the handler simply reacts to incoming events (i.e. messages). It could initiate further actions, however, they are still reactions to the upstream search event.

We place this code in `my_agent/skills/my_search/handlers.py`.


## Step 4: Develop a Task

We have implemented a behaviour and a handler. We conclude by implementing a task. Here we can implement background logic. We will implement a trivial check on the difference between the amount of search requests sent and responses received.


```python
import logging

from aea.skills.base import Task

logger = logging.getLogger("aea.my_search_skill")


class MySearchTask(Task):
    """This class scaffolds a task."""

    def setup(self) -> None:
        """
        Implement the setup.

        :return: None
        """
        logger.info("[{}]: setting up MySearchTask".format(self.context.agent_name))

    def execute(self) -> None:
        """
        Implement the task execution.

        :param envelope: the envelope
        :return: None
        """
        my_search_behaviour = self.context.behaviours[0]
        my_search_handler = self.context.handlers[0]
        logger.info("[{}]: number of search requests sent={} vs. number of search responses received={}".format(self.context.agent_name,
                                my_search_behaviour.sent_search_count,
                                my_search_handler.received_search_count)
        )

    def teardown(self) -> None:
        """
        Implement the task teardown.

        :return: None
        """
        logger.info("[{}]: tearing down MySearchTask".format(self.context.agent_name))
```

Note, how we have access to other objects in the skill via `self.context`.

We place this code in `my_agent/skills/my_search/tasks.py`.


## Step 5: Create the config file

Based on our skill components above, we create the following config file:

```yaml
name: my_search
authors: Fetch.ai Limited
version: 0.1.0
license: Apache 2.0
url: ""
description: 'A simple search skill utilising the OEF.'
behaviours:
  - behaviour:
      class_name: MySearchBehaviour
      args: {}
handlers:
  - handler:
      class_name: MySearchHandler
      args: {}
tasks:
  - task:
      class_name: MySearchTask
      args: {}
shared_classes: []
protocols: ["oef"]
dependencies: []
```

We place this code in `my_agent/skills/my_search/skill.yaml`.


## Step 6: Add the oef protocol

Our agent does not have the oef protocol yet. Hence, we add it like so:
```bash
aea add protocol oef
```

## Step 7: Run the agent

We first start an oef node (see the <a href="../connection/">connection section</a> for more details) in a separate terminal window:

```bash
python scripts/oef/launch.py -c ./scripts/oef/launch_config.json
```

We can then launch our agent:
```bash
aea run
```

Stop the agent with `CTRL + C`.


## Now it's your turn:

We hope this step by step introduction has helped you to develop your own skill. We are excited to see what you will build.

<br />
