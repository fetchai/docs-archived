<!--
## Pull

Clone the repo:

```python
git clone https://github.com/fetchai/oef-search-pluto && cd oef-search-pluto
```

!!! Warning
	At 13/6/2019, the correct code was still in private repo and cloning the above link did not function correctly.
	

Checkout the master branch:

``` bash
git checkout master
```

If you are only going to run a standalone single node, you only need the `scripts` directory from the repo.

-->

First, get <a href="https://www.docker.com/get-started">Docker</a>.

Next, pull and launch our published image.

``` bash
docker pull fetchai/oef-search:latest
```

Now download the <a href="/oef/assets/node_config.json" download="">`node_config.json`</a> file.

And run the Docker image with the configuration.

``` bash
docker run -it -v `pwd`:/config -p 20000:20000 -p 10000:10000 -p 40000:40000 -p 7500 fetchai/oef-search:latest node no_sh --config_file /config/node_config.json
```

A successful run will start producing stats dumps after a few seconds. 

You'll need to have several ports available on your machine: `10000`, `20000`, `30000`, and `7500`.

<!--
``` bash
sudo python3 scripts/launch.py -c ./scripts/launch_config.json
```


You are now running a full OEF node. It contains a core node on `port 10000` connected to a search node on `port 20000`.

The `launch_config.json` file in the `scripts` directory configures port forwarding on the host machine. By default, the `scripts` directory is mounted onto the container.

The `image` entry in the same file defaults to the Fetch.AI public image on 

The `config_file` entry points to `/config/node_config.json` which has a whole bunch of options for each node's setup.

Node content is in `/docker-images/config`. 





<H3>Running the container in the background</H3>

First, configure logging on the node.

1. Create a folder `logs` in the current directory.
2. Open `scripts/node_config.json` and update `log_dir` to `"log_dir": "/logs",`.
3. Open `scripts/launch_config.json` and extend the `params` list with: `"-v", "$PWD/logs:/logs"`. `$PWD` grabs the full path to the project root.

Now launch the node with the `background` flag.

``` bash
python3 scripts/launch.py -c ./scripts/launch_config.json --background
```

You will see `search.log`, `core.log`, etc. in the `/logs` directory.

To stop a running Docker image, run `docker ps` and copy the `CONTAINERID`. Then run `docker kill CONTAINERID`. To kill all running Docker images, run `docker kill $(docker ps -q)`.




## Verify

The verification demo allows an agent to connect to the network and issue a network-wide query for weather data in a particular location. The network nodes broadcast and propagate the location-based query. 

Use `docker-images/demo_network.py` to start multiple nodes at once. There are a number of option flags: 

* `--num_nodes` specifies the number of nodes. 
* `--run_director` positions each node in a UK city and registers a weather agent on each node. Cities are ordered by population and start at London. 
* `--link` connects nodes to each other by a list of tuples representing source:destination `SRC:DST`.
* `--http_port_map` enables the HTTP search endpoint on individual nodes. It contains a list of `ID:PORT` entries, where the `ID` is `0`-`num_nodes` and `PORT` is a unique port number for each node.
* Access the HTTP interface with `https://localhost:PORT`. 
 
 
For example, start two connected nodes:

```bash
python3 docker-images/demo_network.py --num_nodes 2 --link 0:1 --http_port_map 0:7500 --log_dir `pwd`/docker-images/logs/ --run_director
```

The above command runs two full nodes, two search nodes, and two oef-core nodes. Core nodes are connected to their search nodes. 

The `--link` argument connects the two nodes. Agents talk to each other via search ports. The SDK does not need to know about these ports.

The ports for the running nodes are as follows:

<center>

| Node   |      Search Port      |  Core Port |
|----------|:-------------:|------:|
| 1 |  20000 | 10000 |
| 2 |    20001   |   10001 |

</center>


Let's try another example. Start three connected nodes, where every node is connected to every other node, and two of the nodes have `http` interfaces:

```bash
python3 docker-images/demo_network.py --num_nodes 3 --link 0:1 0:2 1:0 1:2 2:0 2:0 --http_port_map 0:7500 1:7501 --log_dir `pwd`/docker-images/logs/ --run_director
```

-->

Now we have a node up and running, let's get the SDK.
