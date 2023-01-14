# Supported Hardware
Reticulum can be used over practically any medium that can support at least a half-duplex channel with 500 bits per second throughput, and an MTU of 500 bytes. Data radios, modems, LoRa radios, serial lines, AX.25 TNCs, amateur radio digital modes, WiFi and Ethernet devices, free-space optical links, and similar systems are all examples of the types of physical devices Reticulum can use. The supported interface types include:

- Any ethernet device
- Almost all WiFi-based hardware
- LoRa using [RNode](https://unsigned.io/rnode/)
- Packet Radio TNCs (with or without AX.25)
- KISS-compatible hardware and software modems
- Any device with a serial port
- TCP over IP networks
- UDP over IP networks
- External programs via stdio or pipes
- Custom hardware via stdio or pipes

For a more detailed info, and a full list of supported interface types, please read the [Communications Hardware](manual/hardware.html) and [Supported Interfaces](manual/interfaces.html) chapters of the manual.

Reticulum can also be encapsulated over existing IP networks, so there's nothing stopping you from using it over wired ethernet, your local WiFi network or the Internet, where it'll work just as well. In fact, one of the strengths of Reticulum is how easily it allows you to connect different mediums into a self-configuring, resilient and encrypted mesh, using any available mixture of available infrastructure.

As an example, it's possible to set up a Raspberry Pi connected to both a LoRa radio, a packet radio TNC and a WiFi network. Once the interfaces are configured, Reticulum will take care of the rest, and any device on the WiFi network can communicate with nodes on the LoRa and packet radio sides of the network, and vice versa.

<p align="right"><a href="connect.html">Next Topic: Public Testnet</a></p>
