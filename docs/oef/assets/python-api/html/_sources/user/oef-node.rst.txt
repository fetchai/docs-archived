.. _oef-node:

Set up an OEF Node
==================

This is a guide that explains how to run an instance of the OEF Node.

We support two methods:

* Using the Docker image
* Build from source

Using the Docker image
~~~~~~~~~~~~~~~~~~~~~~


Using Docker
````````````

It assumes that `Docker <https://docs.docker.com/>`_ is installed. Please refer to the installation guide, depending
on your platform:


* `Linux (Ubuntu) <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_
  (be sure to follow the `Post-installation steps <https://docs.docker.com/install/linux/linux-postinstall/>`_ as well)
* `MacOS <https://docs.docker.com/docker-for-mac/install/>`_
* `Windows <https://docs.docker.com/docker-for-windows/install/>`_



Build and run the image
```````````````````````


We recommend you use the Docker image provided by
the `OEF Core <https://github.com/fetchai/oef-core.git>`_ project,
by following these steps:

* Clone ``oef-core``

.. code-block:: bash

  git clone https://github.com/fetchai/oef-core.git --recursive && cd oef-core/

* Build the image

.. code-block:: bash

  ./oef-core-image/scripts/docker-build-img.sh

* Run the image. This will start the OEF node, listening to port ``3333`` at ``localhost``:

.. code-block:: bash

  ./oef-core-image/scripts/docker-run.sh -p 3333:3333 --

Your terminal will be busy while the Docker image is running.
If you would prefer to run the OEF node in the background, add the ``-d`` flag:

.. code-block:: bash

  ./oef-core-image/scripts/docker-run.sh -p 3333:3333 -d --

After you have completed this tutorial,
you can exit the Docker container by running the following line:

.. code-block:: bash

  docker stop $(docker ps | grep oef-core-image | awk '{ print $1 }')

Build from source
~~~~~~~~~~~~~~~~~

You will need:

* ``cmake``
* ``gcc``
* Google Protocol Buffers library.

On Linux (Ubuntu) you can run:

.. code-block:: none

  git clone https://github.com/fetchai/oef-core.git --recursive && cd oef-core
  sudo apt-get install cmake protobuf-compiler libprotobuf-dev
  mkdir build && cd build
  cmake ..
  make -j 4

And to run an instance of ``OEFNode``:

.. code-block:: none

  ./apps/node/OEFNode

Optional: you can also install it in your system:

.. code-block:: none

  make install

For full details, please follow the
`installation instructions for the OEFCore <https://github.com/fetchai/oef-core/blob/master/INSTALL.txt>`_.

