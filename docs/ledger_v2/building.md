# Building the Ledger

## Prerequists

- Go 1.14+ (installation instructions available from https://golang.org/dl/)

## Building the code

Download the latest released version from github and build the project using the following commands:

    $ git clone https://github.com/fetchai/fetchd.git -b releases/v0.2.x
    $ cd fetchd
    $ make build

This will generate the following binaries:

- `./build/wasmcli` - This is the command line client that is useful for interacting with the network
- `./build/wasmd` - This is the block chain node daemon and can be configured to join the network

For non developer users we recommend that the user installs the binaries into the system. This can be done with the following command:

    $ sudo make install
