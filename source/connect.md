# Public Testnet
If you just want to get started experimenting without building any physical networks, you are welcome to join the Public Reticulum Testnet. The testnet is just that, an informal network for testing and experimenting. It will be up most of the time, and anyone can join, but it also means that there's no guarantees for service availability.

The testnet runs the very latest version of Reticulum (often even a short while before it is publicly released). Sometimes experimental versions of Reticulum might be deployed to nodes on the testnet, which means strange behaviour can occur. If none of that scares you, you can join the testnet via eihter TCP or I2P. Just add one of the following interfaces to your Reticulum configuration file:

```
# For connecting over TCP/IP:

  [[RNS Testnet Frankfurt]]
    type = TCPClientInterface
    interface_enabled = yes
    outgoing = True
    target_host = frankfurt.rns.unsigned.io
    target_port = 4965


# For connecting over I2P:

  [[RNS Testnet I2P Node A]]
    type = I2PInterface
    interface_enabled = yes
    peers = ykzlw5ujbaqc2xkec4cpvgyxj257wcrmmgkuxqmqcur7cq3w3lha.b32.i2p
```

The testnet also contains a number of [Nomad Network](https://github.com/markqvist/nomadnet) nodes, and [LXMF](https://github.com/markqvist/lxmf) propagation nodes.

<p align="right"><a href="docs.html">Next Topic: Read The Manual</a></p>
