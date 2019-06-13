Agents register to and deregister from the OEF.

<center>
![View of an Agent sending requests to register to and deregister from the OEF.](./img/register-deregister.png "Agents registering to and deregistering from the OEF.")
</center>

Before an Agent can advertise or search for services, it must register to the OEF.

Agents are created with a name and public key and they connect to the OEF with an OEF host and port number. 

On attempting to connect to the OEF, the public key is verified.

## Role names

An Agent can perform several roles at once. 

In order to distinguish between roles, an Agent supplies a different name for each role.

This means that an agent could advertise several services using the same public key but different roles names, such as in this example:

<center>


| Public key and role name   |      Data members advertised      |  
|----------|:-------------|
| DEADBEEF/newspaper_seller |  available_newspaper_list <br/> available_magazine_list | 
| DEADBEEF/refuelling_station |    petrol_availability <br/> diesel_availability |


</center>


When an Agent conducts a search, it receives the public key and the role name of Agent(s) who are advertising matching services. 

A role name can be empty. This is the default case and can be used for simple Agent setups.

In order to talk to Agents with multiple services, we use a Context which contains source and target information for every message.

The target information, key and role, references the receiving Agent. Similarly the source information references the sending Agent. To send a reply the other way, the two parts can simply be swapped.

<br/>
