# Agent-based and multi-agents systems

# Agent-Based Systems

An **agent** is a computer program that performs various actions _continuously_ and _autonomously_  (with limited or no interference) on behalf of an individual or an organization. Agents have behaviors, often described by simple rules, and interactions with other agents, which in turn influence their behaviors. The most important defining characteristic of an agent is its capability to act autonomously, that is, to act on its own without external direction in response to situations it encounters. Agents are endowed with behaviors that allow them to make independent decisions. Typically, agents are active, initiating their actions to achieve their internal goals, rather than merely passive, reactively responding to other agents and the environment. 

Agents have **five key characteristics**:

1. **Representation**: The first key characteristic of agents is that they operate on behalf of an individual or organization. Agents are always operating for an entity. 

2. **Autonomy**: Agents operate with limited or no interference, they do not need to be told what to do constantly but perform actions continuously according to the rules they have been given.

3. **Self-interested**: They operate in their own interests and not necessarily in the interests of other agents.

4. **Goal-oriented**:  agents have goals to achieve with respect to their behaviors. This allows an agent to compare the outcome of its behaviors relative to its goals and adjust its responses and behaviors in future interactions.

5. **Reactive**: Agents are reactive. This is because they react to the circumstances around them and act consequently. A great example of this is an automatic thermostat, that turns the heating on or off when the temperature changes.

_Agent characteristics and behaviors may vary in their extent and sophistication_. An agent may differ from other agents, for instance, in the amount of information considered in the agent’s decisions process, the agent’s internal models of the external world, the agent’s view of the possible reactions of other agents in response to its actions, and the extent of memory of past events the agent retains and uses in making its decisions. Agents may also be endowed with different amounts of resources or accumulate different levels of resources as a result of agent interactions, further differentiating agents.

Agent-based modelling has been used in an enormous variety of applications spanning the physical, biological, social, and management sciences. In the biological sciences, agent-based modelling is used to model cell behavior and interaction, the workings of the immune system, tissue growth, and disease processes. Archaeology and anthropology make use of largescale agent-based modelling by providing a virtual environment for long-vanished civilizations. In ecology, agent-based modeling is used to model diverse populations of individuals and their interactions (e.g. Agent-based epidemic and pandemic models). Agent-based models have also been developed in the fields of economics, sociology, anthropology, and cognitive science. Various social phenomena have been investigated using agent-based models that are not easily modelled using other approaches. Here, agent-based models are being used to analyse existing and hypothetical markets (e.g. agent-based simulation to model possible futures for a market directed towards space tourism, to analyse how companies represented by agents would compete and offer products to customers in this hypothetical market).

As it is possible to think, there are a growing number of agent-based applications in a variety of fields and disciplines directed towards the study of a large number of real-world applications. Examples of agent-based systems, for which large-scale agent-based models have been developed, include traffic, air traffic control, military command and control, physical infrastructures and markets, such as electric power and integrated energy markets.

# Multi-Agents Systems

A **Multi-Agent System** (**MAS**) is a group of agents that interact with each other and the environment to achieve specific goals. In such systems, agents may not have full knowledge of both the environment and the internal state of other agents. _Interactions between agents is an important feature that enables them to use knowledge of other agents and learn more about the environment in a compressed time period_. This type of interaction may be _cooperative_ or _competitive_. In a cooperative interaction, agents work with each other towards a common goal. The aim of this interaction is to enable agents to distribute and share their knowledge and use the intelligence and capabilities of each other to solve problems. In a competitive interaction, agents may compete to obtain individual resources and achieve individual goals. 

MAS systems have different **key characteristics**:

1. **Decentralization**: multi-agent systems are decentralized. The authority to make management decisions about the system is distributed among the participants. A multi-agent system is run for its participants by its participants.

2. **Heterogeneity**: the agents in multi-agent systems are not uniform throughout, they may be composed of agents composed of different hardware or software components, but all working in a self-interested way collaboratively.

3. **Scalability**: multi-agent systems are easy to scale; you simply add agents to the system to grow the system.

4. **Robustness**: multi-agent systems are intrinsically very robust as no single failure point takes down the system. 

5. **Adaptability**: multi-agent systems adapt to changing circumstances very effectively as each agent autonomously adjusts to changing circumstances.

However, there are some negative features_ characterizing such systems:

1. **Complexity**: multi-agent systems are quite complex to set up, you have to use a pre-existing framework or build one and getting all the agents to communicate effectively together can be an operational challenge. As these are decentralized systems (i.e. no central authority), managing the system is more complicated than in a centralized one, as participants need to be involved in management decisions.

2. **Predictability**: with every agent acting in a self-interested manner with clear goals, it is easy to predict what an individual agent is trying to achieve. However, it is harder to predict the direction of the whole system as that is the result of the interactions between all the agents and each agent is different. 

The _complexity of MASs_ can increase rapidly with the number of agents, the interactions among them, or the complexity of their behaviour. System composition depends on the characteristics of individual agents and whether they are _homogeneous_ or _heterogeneous_ in physical and/or programming structure. Homogeneous agents are similar to each other or they are of the same type, whereas, heterogeneous agents are different and diverse in kind. 

MAS have received tremendous attention from scholars in different disciplines, ranging from computer science to civil engineering, in order to solve complex problems by subdividing them into smaller tasks. The individual tasks are allocated to autonomous agents, and each one of them decides on a proper action to solve the task using multiple inputs (e.g. history of actions, interactions with its neighbouring agents, and its goal). 

A good example of a MAS is represented by _smart-grids_, in which different agents work together collaboratively, but independently and in a self-interested manner. Another important application of such systems is found in _computer gaming_ and _computer simulations_. Such fields increasingly adopted MASs. Here, each participant has its own agent and interacts in the environment populated also by other agents. _Self-driving vehicles_ are another great example of an agent based system. In this respect, each vehicle acts as an agent, directed by their user and acting independently from other agents within a set of rules, such as not exceeding the speed limits, and being responsive to the environment around them. 

As we can see, MAS have found mu**ltiple applications including _modelling complex systems_, _smart grids_ and _computer networks_. The main application domains of MAS are _ambient intelligence_, _grid computing_, _electronic business_, _the semantic web_, _bioinformatics and computational biology_, _monitoring and control_, _resource management_, _education_, _space_, _military_ and _manufacturing applications_, and so on.
 
**Despite their wide applicability, there are still several challenges faced by MAS including coordination between agents, security, and task allocation.**
