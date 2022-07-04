# Public Testnet
If you just want to get started experimenting without building any physical networks, you are welcome to join the Public Reticulum Testnet. The testnet is just that, an informal network for testing and experimenting. It will be up most of the time, and anyone can join, but it also means that there's no guarantees for service availability.

The testnet runs the very latest version of Reticulum (often even a short while before it is publicly released). Sometimes experimental versions of Reticulum might be deployed to nodes on the testnet, which means strange behaviour can occur. If none of that scares you, you can join the testnet via eihter TCP or I2P.

Just add one of the following interfaces to your Reticulum configuration file:

```
# TCP/IP interface to the Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# TCP/IP interface to the Frankfurt Hub
  [[RNS Testnet Frankfurt]]
    type = TCPClientInterface
    enabled = yes
    target_host = frankfurt.connect.reticulum.network
    target_port = 5377

# Interface to I2P Hub A
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = mrwqlsioq4hoo2lmeeud7dkfscnm7yxak7dmiyvsrnpfag3z5tsq.b32.i2p

# Interface to I2P Hub B
  [[RNS Testnet I2P Hub B]]
    type = I2PInterface
    enabled = yes
    peers = iwoqtz22dsr73aemwpw7guocplsjjoamyl7sogj33qtcd6ds4mza.b32.i2p
```

The testnet also contains a number of [Nomad Network](https://github.com/markqvist/nomadnet) nodes, and [LXMF](https://github.com/markqvist/lxmf) propagation nodes.

<p align="right"><a href="docs.html">Next Topic: Read The Manual</a></p>
