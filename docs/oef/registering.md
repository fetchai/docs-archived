Agents register to and deregister from the OEF.

<center>
![View of an Agent sending requests to register to and deregister from the OEF.](./img/register-deregister.png "Agents registering to and deregistering from the OEF.")
</center>

Before an Agent can advertise or search for services, it must register onto the OEF.

## `AsyncioCore` thread management

The `AsyncioCore` class is a thread manager for `Agent` objects.

Instantiate an `AsyncioCore` class and call the `run_threaded()` function to start the networking.

Call `stop()` when you're done.

```c++
core = AsyncioCore(logger=logger)
core.run_threaded()

// do stuff

core.stop()
```

## `Agent` creation

Create an `Agent` with a name and public key.

The `Agent` connects to the OEF with the given OEF host and port number.

Finally, include the `AsyncioCore` class in the `Agent` constructor.

The following example builds a weather station agent that is managed by the `AsyncioCore` class.

```c++
agent = WeatherStation("weatherStationSecure", prv_key_file="examples/resources/agent_1.pem", oef_addr="127.0.0.1", oef_port=10005, core=core)
agent.connect()
```

On attempting to connect to the OEF, the public key is verified.

Include a single `AsyncioCore` class in many `Agent` objects.

## `Agent` state

Query the `state` parameter of an `Agent` with `get_state()`.

The `Agent` returns one of the following self-explanatory strings:

-   `offline`.
-   `connecting`.
-   `connected`.
-   `failed`.
-   `timedout`.
-   `terminated`.

## Single `Agent` reacting to arriving messages

Call `run()` on a single `Agent` after connecting if the `Agent` is only going to react to arriving messages. This puts the `Agent` into a loop.

The loop sleeps then checks for the `Agent` state.

When the `Agent` is in a disconnected state, the loop calls `stop()` on the `Agent`.

```python
if __name__ == "__main__":
    core = AsyncioCore(logger=logger)
    core.run_threaded()

    # create and connect the agent
    agent = WeatherClient("weatherCLient", oef_addr="127.0.0.1", oef_port=10000, core=core)
    agent.connect()

    # add queries to the agent

    try:
        agent.run()
        time.sleep(3)

    except Exception as ex:
        print("EXCEPTION:", ex)

    finally:
        agent.stop()
        agent.disconnect()
        core.stop()
```

## Single `Agent` doing intermittent work

If you have an `Agent` which not only reacts to messages but also has to do some intermittent activity, do not call `run()`.

Instead, after connecting, build a loop that checks the `Agent` state for some form of disconnection, at which point the loop calls `stop()`.

While the `Agent` state is not disconnected, perform the required tasks.

```python
def doSearch():
	# doing search here

if __name__ == "__main__":
    core = AsyncioCore(logger=logger)
    core.run_threaded()

    # create and connect the agent
    agent = WeatherClient("weatherCLient", oef_addr="127.0.0.1", oef_port=10000, core=core)
    agent.connect()

    # do stuff with the agent

    try:
		while agent.get_state() not in ["connected", "connecting"]:
	      	agent.doSearch()
	       	time.sleep(5)

    except Exception as ex:
        print("EXCEPTION:", ex)

    finally:
        agent.stop()
        agent.disconnect()
        core.stop()
```

## Multiple `Agent` scenarios

Do not call `run()` in scenarios in which you have more than one `Agent` in play.

For example, when connecting to multiple OEF cores, set up each `Agent` and call `connect()`. Then perform the specific tasks.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Logger can also be a print function.</p>
</div>

```python
def doSpecificTasks(agent):
	# do stuff here

if __name__ == "__main__":
    core = AsyncioCore(logger=print)
    core.run_threaded()

    # create and connect the agent
    agent1 = WeatherClient("weatherClient1", oef_addr="127.0.0.1", oef_port=10000, core=core)
    agent1.connect()
   	agent2 = WeatherClient("weatherClient2", oef_addr="127.0.0.1", oef_port=10001, core=core)
    agent2.connect()

    # add queries to the agent

	try
		while agent1.get_state() in ["connected", "connecting"] and agent2.get_state() in ["connected", "connecting"]:
	      	doSpecificTasks(agent1)
            doSpecificTasks(agent2)
	       	time.sleep(5)

    except Exception as ex:
        print("EXCEPTION:", ex)

    finally:
        agent1.stop()
        agent1.disconnect()
        agent2.stop()
        agent2.disconnect()
        core.stop()
```

## Role names

An Agent can perform several roles at once.

In order to distinguish between roles, an Agent supplies a different name for each role.

This means that an agent could advertise several services using the same public key but different roles names, such as in this example:

<center>

| Public key and role name    | Data members advertised                                |
| --------------------------- | :----------------------------------------------------- |
| DEADBEEF/newspaper_seller   | available_newspaper_list <br/> available_magazine_list |
| DEADBEEF/refuelling_station | petrol_availability <br/> diesel_availability          |

</center>

When an Agent conducts a search, it receives the public key and the role name of Agent(s) who are advertising matching services.

A role name can be empty. This is the default case and can be used for simple Agent setups.

In order to talk to Agents with multiple services, we use a Context which contains source and target information for every message.

The target information, key and role, references the receiving Agent. Similarly the source information references the sending Agent. To send a reply the other way, the two parts can simply be swapped.

<br/>
