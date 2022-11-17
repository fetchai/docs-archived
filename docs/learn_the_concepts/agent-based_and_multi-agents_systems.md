# Agent-based and multi-agents systems

An **agent** is a piece of software that _represents_ an entity (individual, organisation, or object) and acts _continuously_ and _autonomously_  (with limited or no interference) on their behalf. The most important defining characteristic of an agent is its autonomy, that is the ability to act on its own without external direction from its owner in response to situations it encounters..

???+ note 

    What differentiates agents to other software paradigms (e.g. smart contracts, web apps) is that as well as being _reactive_, meaning they respond to other agents and changes in their environments, they are also _proactive_, which means that they take the initiative and perform actions to achieve their goals.

Agents have _five key characteristics_: 

1. **Representation**: Agents are owned by and operate on behalf of an entity, for example an individual, family, company, government, or object, and look after their owner's interests.

2. **Autonomy**: Agents operate with limited or no interference and do not need to be constantly told what to do. They perform actions continuously according to their internal reasoning system.

3. **Self-interested**: Each agent primarily looks after its own interests (which is aligned with those of its owner) and not necessarily the interests of other agents.

4. **Proactive**:  Agents have goals to achieve allowing them to take the initiative and perform actions that get them closer to achieving their goals. This means an agent typically compares the outcome of different actions relative to its goals and selects the one that takes it closer to them.

5. **Reactive**: Agents respond to other agents, services, etc., and changes in their environments. A great example of this behaviour is a heating system with a thermostat that constantly monitors its environment and turns the heating on or off when the temperature changes.

???+ note

    Agent characteristics and behaviors may vary in their extent and sophistication. An agent may differ from other agents, for instance, in the amount of information in the agent’s decisions process, its internal models of the external world, its view of the possible reactions of other agents in response to its actions, and the size of the memory of past events the agent retains and uses in making its decisions. Further instances of differentiating factors are the amounts of resources used by agents or accumulated as a result of their interactions.

## Agent-Based Modelling

In agent-based modelling (ABM), a system is represented as a group of independent decision-making units known as agents. Each agent evaluates its own circumstances and decides based on a set of rules. Agents can act in a variety of ways that are suitable for the system they are representing (e.g. producing, consuming, or selling). An agent-based model, at its most basic, consists of a system of agents and the connections between them. Even a straightforward agent-based model has the potential to display intricate behavioural patterns and provide important details about the behaviour of the emulated real-world system. 

Agent-based modelling has been used in various kinds of applications spanning the physical, biological, social, and management sciences. Agent-based models have also been developed in the fields of economics, sociology, anthropology, and cognitive science. Various social phenomena have been investigated using agent-based models that are not easily modeled using other approaches. Here, agent-based models are being used to analyze existing and hypothetical markets.

!!! example

    Agent-based simulations are used to model possible futures for a market directed towards space tourism, to analyze how companies represented by agents would compete and offer products to customers in this hypothetical market.

As it is possible to think, there are a growing number of agent-based applications in a variety of fields and disciplines directed towards the study of a large number of real-world applications. Examples of agent-based systems, for which large-scale agent-based models have been developed, include: traffic, air traffic control, military command and control, physical infrastructures and markets, such as electric power and integrated energy markets. 

???+ note

    When it comes to consider the Fetch.ai ecosystem, despite some similarities between ABM and the Autonomous Economic Agent (AEA) Framework, the two have fundamentally different goals. ABM's goal is not the design of agents or solving specific practical or engineering problems, but to study the unknown and complex behaviour of systems comprised of agents with known behaviour. On the other hand, the Autonomous Economic Agent (AEA) Framework's goal is to provide the necessary tools to build AEAs which purpose is to create economic value for their owner in clearly defined domains of application and not the study of existing of hypothetical scenarios to gather data.

## Multi-Agents Systems

A **Multi-Agents System** (**MAS**) is a group of agents that interact with each other and the environment to achieve specific goals. In such systems, agents may not have full knowledge of both the environment and the internal state of other agents. 

???+ info 

    Interactions between agents is an important feature that enables them to use knowledge of other agents and learn more about the environment in a compressed time period. This type of interaction may be **cooperative** or **competitive**. In a cooperative interaction, agents work with each other towards a common goal. The aim of this interaction is to enable agents to distribute and share their knowledge and use the intelligence and capabilities of each other to solve problems. In a competitive interaction, agents may compete to obtain individual resources and achieve individual goals.

MAS systems have different **key characteristics**:

1. **Decentralization**: multi-agents systems are decentralized. The authority to make management decisions about the system is distributed among the participants. A multi-agents system is run for its participants by its participants.

2. **Heterogeneity**: the agents in multi-agents systems are not uniform throughout, they may be composed of agents composed of different hardware or software components, but all working in a self-interested way collaboratively.

3. **Scalability**: multi-agents systems are easy to scale, you simply add agents to the system to grow the system.

4. **Robustness**: multi-agents systems are intrinsically very robust as no single failure point takes down the system.

5. **Adaptability**: multi-agents systems adapt to changing circumstances very effectively as each agent autonomously adjusts to changing circumstances.

However, there are some negative features characterizing such systems:

1. **Complexity**: multi-agents systems are quite complex to set up, you have to use a pre-existing framework or build one, and getting all the agents to communicate effectively together can be an operational challenge. As these are decentralized systems (i.e. no central authority), managing the system is more complicated than in a centralized one, as participants need to be involved in management decisions.

2. **Predictability**: with every agent acting in a self-interested manner with clear goals, it is easy to predict what an individual agent is trying to achieve. However, it is harder to predict the direction of the whole system as that is the result of the interactions between all the agents and each agent is different. 

???+ note 

    The complexity of MASs can increase rapidly with the number of agents, the interactions among them, or the complexity of their behavior. System composition depends on the characteristics of individual agents and whether they are homogeneous or heterogeneous in physical and/or programming structure. Homogeneous agents are similar to each other or of the same type, whereas, heterogeneous agents are different and diverse in kind.

MAS have received tremendous attention from scholars in different disciplines, ranging from computer science to civil engineering, in order to solve complex problems by subdividing them into smaller tasks. The individual tasks are allocated to autonomous agents, and each one of them decides on a proper action to solve the task using multiple inputs (e.g. history of actions, interactions with its neighboring agents, and its goal).

!!! example

    A good example of a MAS is represented by _smart-grids_, in which different agents work together collaboratively, but independently and in a self-interested manner. Another important application of such systems is found in _computer gaming_ and _computer simulations_. Such fields increasingly adopted MASs. Here, each participant has its own agent and interacts in the environment populated also by other agents. _Self-driving vehicles_ are another great example of an agent based system. In this respect, each vehicle acts as an agent, directed by their user and acting independently from other agents within a set of rules, such as not exceeding the speed limits, and being responsive to the environment around them. 

MAS have found multiple applications including _modeling complex systems_, _smart grids_ and _computer networks_. The main application domains of MAS are _ambient intelligence_, _grid computing_, _electronic business_, _the semantic web_, _bioinformatics and computational biology_, _monitoring and control_, _resource management_, _education_, _space_, _military_ and _manufacturing applications_, and so on.

???+ note 

    Despite their wide applicability, there are still several challenges faced by MAS including coordination between agents, security, and task allocation.
