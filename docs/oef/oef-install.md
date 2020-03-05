## Initial setup

First, get <a href="https://www.docker.com/get-started">Docker</a>.

Next, pull our published image.

``` bash
docker pull fetchai/oef-search:latest
```
Grab the configuration file.

``` bash
curl https://docs.fetch.ai/oef/assets/node_config.json \
  --output node_config.json
```

And run the Docker image with the configuration.

``` bash
docker run -it -v `pwd`:/config -p 20000:20000 -p 10000:10000 -p 40000:40000 -p 7500 fetchai/oef-search:latest node no_sh --config_file /config/node_config.json
```

A successful run will start producing stats dumps after a few seconds. 

You'll need to have several ports available on your machine: `10000`, `20000`, `30000`, and `7500`.


## Get the OEF SDK

First, run the pip installation command:

``` bash
pip3 install -v -v -v --no-cache-dir oef
```

After that, let's check we installed the SDK correctly:

``` bash
python3
from oef import agents
```

When a function needs a core address, use `127.0.0.1` and port `10000`.


## Get the example code

Download the <a href="/oef/assets/examples.tgz" download="">working examples bundle</a>.

Or curl them here:

``` bash
curl https://docs.fetch.ai/oef/assets/examples.tgz \
  --output examples.tgz
```

<br/>
