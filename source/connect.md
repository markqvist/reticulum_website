# Bootstrapping Connectivity

Reticulum is not a service you subscribe to, nor is it a single global network you “join”. It is a *networking stack*; a toolkit for building communications systems that align with your specific values, requirements, and operational environment. The way you choose to connect to other Reticulum peers is entirely your own choice.

When you first start using Reticulum, you need a way to obtain connectivity with the peers you want to communicate with - the process of *bootstrapping connectivity*. Once you have obtained one or more valid interface definitions, you can add them to the `[interfaces]` section of your Reticulum configuration.

This page provides the most basic overview, but to fully understand the flexibility and options available for bootstrapping connectivity, read the [Bootstrapping Connectivity](manual/gettingstartedfast.html#creating-a-network-with-reticulum) section of the manual.

## Connect to the Distributed Backbone

A global, distributed backbone of Reticulum Transport Nodes is being run by volunteers from around the world. This network constitutes a heterogenous collection of both public and private nodes that form an uncoordinated, voluntary inter-networking backbone that currently provides global transport and internetworking capabilities for Reticulum.

A good place to find interface definitions for bootstrapping connectivity are community-run websites like [directory.rns.recipes](https://directory.rns.recipes/) and [rmap.world](https://rmap.world/).

Reticulum encourages the approach of *organic growth*. Instead of relying on permanent static connections to distant servers, you can use temporary bootstrap connections to continously *discover* more relevant or local infrastructure. Once discovered, your system can automatically form stronger, more direct links to these peers, and discard the temporary bootstrap links. This results in a web of connections that are geographically relevant, resilient and efficient.

## Build Personal Infrastructure

We strongly encourage everyone, even home users, to think in terms of building **personal infrastructure**. Don’t connect every phone, tablet, and computer in your house directly to a public internet gateway. Instead, repurpose an old computer, a Raspberry Pi, or a supported router to act as your own, personal **Transport Node**:

* Your local Transport Node sits in your home, connected to your WiFi and perhaps a radio interface (like an RNode).
* You configure this node with a `bootstrap_only` interface (perhaps a TCP tunnel to a wider network) and enable interface discovery.
* While you sleep, work, or cook, your node listens to the network. It discovers other local community members, validates their Network Identities, and automatically establishes direct links.
* Your personal devices now connect to your *local* node, which is integrated into a living, breathing local mesh. Your traffic flows through local paths provided by other real people in the community rather than bouncing off a distant server.

**Don’t wait for others to build the networks you want to see**. Every network is important, perhaps even most so those that support individual families and persons. Once enough of this personal, local infrastructure exist, connecting them directly to each other, without traversing the public Internet, becomes inevitable.

<p align="right"><a href="docs.html">Next Topic: Read The Manual</a></p>
