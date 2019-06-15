We will focus solely on Python SDK examples throughout the documentation. 

## Python

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

Now download the <a href="/oef/assets/examples.tgz" download="">working examples bundle</a>.


<!--
## Java/Kotlin

First clone the repo:

!!! Warning
	This is an internal private repo.

``` bash
git clone git@github.com:uvue-git/oef-sdk-kotlin.git
```

In your IDE in the `oef-sdk-kotlin` directory, build and install to your local maven with:

``` bash
./gradlew clean
./gradlew build -x test
./gradlew publishToMavenLocal
```

To run some examples, clone the following repo:

``` bash
git clone git@github.com:uvue-git/oef-sdk-kj-examples.git
```

!!! Warning
	This is an internal private repo.


In your IDE, run:

``` bash
./gradlew clean
./gradlew build -x test
```

You can now run the `WeatherClient` example.


## C++

Run the following commands:

``` bash
git clone git@github.com:uvue-git/oef-sdk-cpp.git
cd oef-sdk-cpp
cmake .
```
-->




