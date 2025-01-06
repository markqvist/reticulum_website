# Public Testnet
If you just want to get started experimenting without building any physical networks, you are welcome to join the Public Reticulum Testnet. The testnet is just that, an informal network for testing and experimenting. It will be up most of the time, and anyone can join, but it also means that there's no guarantees for service availability.

**Please note!** For everyday use of Reticulum, such as for messaging and other communications, it is much better to use one or more of the community-provided public entrypoints. Please see the next section for details. 

The testnet runs the very latest version of Reticulum (often even a short while before it is publicly released). Sometimes experimental versions of Reticulum might be deployed to nodes on the testnet, which means strange behaviour can occur. If none of that scares you, you can join the testnet via either TCP or I2P.

Just add one of the following interfaces to your Reticulum configuration file:

```
# TCP/IP interface to the Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# TCP/IP interface to the BetweenTheBorders Hub (community-provided)
  [[RNS Testnet BetweenTheBorders]]
    type = TCPClientInterface
    enabled = yes
    target_host = reticulum.betweentheborders.com
    target_port = 4242

# Interface to I2P Hub A
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = g3br23bvx3lq5uddcsjii74xgmn6y5q325ovrkq2zw2wbzbqgbuq.b32.i2p
```

The testnet also contains a number of [Nomad Network](https://github.com/markqvist/nomadnet) nodes, and [LXMF](https://github.com/markqvist/lxmf) propagation nodes.

# Community Entrypoints
A number of publicly available entrypoints to Reticulum networks have been provided by the community. For everyday use, it is recommended to use these instead of the testnet.

You can connect your devices or instances to one or more of these to gain access to any Reticulum networks they are physically connected to.

Ideally, set up a Reticulum Transport Node that your own devices can reach locally, and then connect that transport node to a couple of public entrypoints. This will provide efficient connections and redundancy in case any of them go down.

{PUBLIC_ENTRYPOINTS}

<p align="right"><a href="docs.html">Next Topic: Read The Manual</a></p>
