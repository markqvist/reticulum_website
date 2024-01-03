# Get Started
The best way to get started with the Reticulum Network Stack depends on what
you want to do. For full details and examples, have a look at the [Getting Started Fast](manual/gettingstartedfast.html) section of the [Reticulum Manual](manual/index.html).

## Experimental Software
*Please Know!* Reticulum is still in beta. This means, that while it already works very well, and is very stable, there could very well still be critical bugs or flaws in the behaviour, privacy or security of the system as a whole. Use Reticulum if you are comfortable with this, and understand the implications.

## Community & Support

If you are having trouble, or if something is not working, here are some great places to ask for help:

- The [discussion forum](https://github.com/markqvist/Reticulum/discussions) on GitHub
- The [Reticulum Matrix Channel](https://matrix.to/#/#reticulum:matrix.org) at `#reticulum:matrix.org`
- The [Reticulum subreddit](https://reddit.com/r/reticulum)

## Installation
To install Reticulum and related utilities on your system, the easiest way is via pip:

```bash
pip install rns
```

You can then start any program that uses Reticulum, or start Reticulum as a system service with [the rnsd utility](manual/using.html#the-rnsd-utility).

If `pip` is not available on your system, install the `python3` and `python3-pip` packages for your OS first.

When first started, Reticulum will create a default configuration file, providing basic connectivity to other Reticulum peers that might be locally reachable. If any of those local peers are Transport Instances, these might connect you to wider networks. The default config file contains a few examples, and references for creating a more complex configuration.

For more detailed examples on how to expand communication over many mediums such as packet radio or LoRa, serial ports, or over fast IP links and the Internet using the UDP and TCP interfaces, take a look at the [Supported Interfaces](manual/interfaces.html) section of the [Reticulum Manual](manual/index.html).


## Included Utilities
Reticulum includes a range of useful utilities for managing your networks, viewing status and information, and other tasks. You can read more about these programs in the [Included Utility Programs](manual/using.html#included-utility-programs) section of the [Reticulum Manual](manual/index.html).

- The system daemon `rnsd` for running Reticulum as an always-available service
- An interface status utility called `rnstatus`, that displays information about interfaces
- The path lookup and and management tool `rnpath` letting you view and modify path tables
- A diagnostics tool called `rnprobe` for checking connectivity to destinations
- A simple file transfer program called `rncp` making it easy to copy files to remote systems
- The remote command execution program `rnx` that let's you run commands and programs and retrieve output from remote systems

All tools, including `rnx` and `rncp`, work reliably and well even over very low-bandwidth links like LoRa or Packet Radio.

## Programs Using Reticulum
If you want to quickly get an idea of what Reticulum can do, take a look at the following resources.

- For an off-grid, encrypted and resilient mesh communications platform, see [Nomad Network](https://github.com/markqvist/NomadNet)
- The Android, Linux and macOS app [Sideband](https://github.com/markqvist/sideband) has a graphical interface and focuses on ease of use.
- [LXMF](https://github.com/markqvist/lxmf) is a distributed, delay and disruption tolerant message transfer protocol built on Reticulum

## Dependencies
The installation of the default `rns` package requires the dependencies listed below. Almost all systems and distributions have readily available packages for these dependencies, and when the `rns` package is installed with `pip`, they will be downloaded and installed as well.

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

On more unusual systems, and in some rare cases, it might not be possible to install or even compile one or more of the above modules. In such situations, you can use the `rnspure` package instead, which require no external dependencies for installation. Please note that the contents of the `rns` and `rnspure` packages are *identical*. The only difference is that the `rnspure` package lists no dependencies required for installation.

No matter how Reticulum is installed and started, it will load external dependencies only if they are *needed* and *available*. If for example you want to use Reticulum on a system that cannot support [pyserial](https://github.com/pyserial/pyserial), it is perfectly possible to do so using the `rnspure` package, but Reticulum will not be able to use serial-based interfaces. All other available modules will still be loaded when needed.

**Please Note!** If you use the `rnspure` package to run Reticulum on systems that do not support [PyCA/cryptography](https://github.com/pyca/cryptography), it is important that you read and understand the [Cryptographic Primitives](crypto.html) section of this site.

## Performance
Reticulum targets a *very* wide usable performance envelope, but prioritises functionality and performance over low-bandwidth mediums. The goal is to provide a dynamic performance envelope from 250 bits per second, to 1 gigabit per second on normal hardware.

Currently, the usable performance envelope is approximately 150 bits per second to 40 megabits per second, with physical mediums faster than that not being saturated. Performance beyond the current level is intended for future upgrades, but not highly prioritised until the wire format and API has been locked in.

<p align="right"><a href="hardware.html">Next Topic: Supported Hardware</a></p>
