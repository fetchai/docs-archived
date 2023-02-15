# Agent-Based and Multi-Agents Systems

An **agent** is a piece of software that _represents_ an entity (individual, organisation, or object) and acts _continuously_ and _autonomously_  (with limited or no interference) on their behalf. 

The most important defining characteristic of an agent is its autonomy, that is the ability to act on its own without external direction from its owner in response to situations it encounters.

???+ note 

    What differentiates agents with other software paradigms (e.g. smart contracts, web apps) is that as well as being _reactive_, meaning they respond to other agents and changes in their environments, they are also _proactive_, which means that they take the initiative and perform actions to achieve their goals.

## Key features of agents

1. **Representation**: Agents are owned by and operate on behalf of an entity, for example an individual, family, company, government, or object, and look after their owner's interests.

2. **Autonomy**: Agents operate with limited or no interference and do not need to be constantly told what to do. They perform actions continuously according to their internal reasoning system.

3. **Self-Interested**: Each agent primarily looks after its own interests (which is aligned with those of its owner) and not necessarily the interests of other agents.

4. **Proactive**:  Agents have goals to achieve allowing them to take the initiative and perform actions that get them closer to achieving their goals. This means an agent typically compares the outcome of different actions relative to its goals and selects the one that takes it closer to them.

5. **Reactive**: Agents respond to other agents, services, etc., and changes in their environments. A great example of this behaviour is a heating system with a thermostat that constantly monitors its environment and turns the heating on or off when the temperature changes.

???+ note

    Agent characteristics and behaviors may vary in their extent and sophistication. An agent may differ from other agents, in the amount of information in its decisions process, its internal models of the external world, its view of the possible reactions of other agents in response to its actions, and the size of the memory of past events the agent retains and uses in making its decisions. Further instances of differentiating factors are the amounts of resources used by agents or accumulated as a result of their interactions.

## Agent-Based Modelling

In agent-based modelling (ABM), a system is represented as a group of independent decision-making units, i.e. agents. Each agent evaluates its own circumstances and makes decisions based on a set of rules. Agents can act in a variety of ways that are suitable for the system they are representing (e.g. producing, consuming, or selling). An agent-based model, at its most basic form, consists of a system of agents and the connections between them. Even a straightforward agent-based model has the potential to display intricate behavioural patterns and provide important details about the behaviour of the emulated real-world system.

Agent-based modelling is used in various application areas, spanning the physical, biological, social, and management sciences. Agent-based models have also been developed in the fields of economics, sociology, anthropology, and cognitive science. Various social phenomena have been investigated using agent-based models that are not easily modeled using other approaches.

!!! example

    Agent-based models can be used to analyze existing and hypothetical markets, for instance, modelling possible futures for a market directed towards space tourism, to analyze how companies represented by agents would compete and offer products to customers in this hypothetical market.

## Multi-Agents Systems

A **Multi-Agents System** (**MAS**) is a group of agents that interact with each other and the environment to achieve specific goals. In such systems, agents may not have full knowledge of both the environment and the internal state of other agents. 

??? note 

    Interactions between agents is an important feature that enables them to use knowledge of other agents and learn more about the environment in a compressed time period. This type of interaction may be _cooperative_ or _competitive_. In a cooperative interaction, agents work with each other towards a common goal. The aim of this interaction is to enable agents to distribute and share their knowledge and use the intelligence and capabilities of each other to solve problems. In a competitive interaction, agents may compete to obtain individual resources and achieve individual goals.

### Benefits

1. **Decentralization**: multi-agents systems are decentralized. The authority to make management decisions about the system is distributed among the participants. A multi-agents system is run for its participants by its participants.

2. **Heterogeneity**: agents in multi-agent systems are owned and operated by different entities and so are typically not uniformly designed. For instance, the agents may be composed of different hardware or software components.

3. **Scalability**: multi-agents systems are easy to scale. You simply add agents to the system to grow the system.

4. **Robustness**: multi-agents systems are intrinsically very robust as no single failure point takes down the system.

5. **Adaptability**: multi-agents systems adapt to changing circumstances effectively as each agent autonomously adjusts to changing circumstances.

### Drawbacks

1. **Complexity**: multi-agents systems are quite complex to set up, maintain and troubleshoot. You have to use a pre-existing framework or build one, and getting all the agents to communicate effectively together can be a challenge. As these are decentralized systems (i.e. no central authority), managing the system is more complicated than a centralized one, as participants need to be involved in management decisions. The complexity of MASs can increase rapidly with the number of agents, the interactions among them, and the complexity of their behavior. 

2. **Unpredictability**: with every agent acting in their own interest, it might be easy to predict what an individual agent is trying to achieve. However, it is much more difficult to predict the direction the whole system moves towards, as this is the result of the many interactions between every individual agent in the system.

Multi-agent systems have received tremendous attention from scholars in different disciplines, ranging from computer science to civil engineering, in order to solve complex problems by subdividing them into smaller tasks. The individual tasks are allocated to autonomous agents, and each one of them decides on a proper action to solve the task using multiple inputs.
