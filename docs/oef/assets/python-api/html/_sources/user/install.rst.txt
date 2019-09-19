.. _install:

Installation
============

This is the full guide about how to install the OEF Python SDK.

The supported platforms are:

* Linux (especially Ubuntu 18.04)
* MacOS
* Windows

The instructions may change depending on the operating system version/distribution.

The installation requires Python 3.5 or later versions.
Also, we assume you have `pip` and `git` installed on your system.

At the moment, we only support installation from source.

Protobuf Compiler
-----------------

The ``oef`` package requires the `Google Protocol Buffers <https://developers.google.com/protocol-buffers/>`_
compiler (version >= 2.0.0).

In order to check if it is installed on your machine, run:

::

  protoc


If you get ``Missing input file.``, then you already have it.

Otherwise, you can install it in several ways, depending on your platform.


Linux (Ubuntu 18.04)
~~~~~~~~~~~~~~~~~~~~

You can follow one of the following instructions:

* Using the package manager:

.. code-block:: bash

  sudo apt-get install protobuf-compiler

* From the release

.. code-block:: bash

  PROTOC_ZIP=protoc-3.3.0-linux-x86_64.zip
  curl -OL https://github.com/google/protobuf/releases/download/v3.3.0/$PROTOC_ZIP
  sudo unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
  rm -f $PROTOC_ZIP


.. code-block:: bash

  sudo apt-get install protobuf-compiler
  git clone https://github.com/fetchai/oef-sdk-python.git --recursive
  cd oef-sdk-python/
  sudo python3 setup.py install

For other platforms and other details, please follow the installation guide: :ref:`install`.

Mac OS X
~~~~~~~~

You can follow one of the following instructions:

* If you have `Homebrew <https://brew.sh/>`_, just run:

.. code-block:: bash

  brew install protobuf

* Alternatively, run the following commands:

.. code-block:: bash

  PROTOC_ZIP=protoc-3.3.0-osx-x86_64.zip
  curl -OL https://github.com/google/protobuf/releases/download/v3.3.0/$PROTOC_ZIP
  sudo unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
  rm -f $PROTOC_ZIP


Other platforms
~~~~~~~~~~~~~~~

You can do it manually by checking the `release page <https://github.com/protocolbuffers/protobuf/releases>`_ and
by choosing the release for your platform.
The name format is ``protoc-$(VERSION)-$(PLATFORM).zip`` (e.g. for Windows look at ``protoc-$(VERSION)-win32.zip``).

Alternatively, you can
`Compile from source <https://github.com/protocolbuffers/protobuf/blob/master/src/README.md#c-installation---windows>`_.



Install ``oef``
---------------

To install the Python package ``oef``, follow these steps:

* Clone the repository:

::

    git clone https://github.com/fetchai/oef-sdk-python.git --recursive && cd oef-sdk-python/


* Install the package:

::

    sudo python3 setup.py install

Use the OEF Node
----------------

In several parts of the documentation, we require that an instance of the OEF Node is running on your local machine.

We suggest following the guide about how to run an OEF Node:  :ref:`oef-node`.