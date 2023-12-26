# 开始使用
开始使用 Reticulum 的第一步是看看自己想做什么。若想查看完整的细节与例子，请参阅[Reticulum 手册](manual/index.html)的[快速开始](manual/gettingstartedfast.html)部分。

## 实验性软件
*请注意！* Reticulum 仍旧处于 Beta 测试阶段。虽然它目前已经工作得相当良好而且稳定，但是在系统整体的行为、隐私或安全性上仍旧可能存在致命的漏洞与缺陷。如果你已经了解可能的后果，并且感觉没问题的话，就开始使用吧！

## 社区与支持

如果你遇到了问题，又或者是有些东西不工作，以下是一些寻求帮助的好地方：

- [Reticulum Github 讨论区](https://github.com/markqvist/Reticulum/discussions)
- [Reticulum Matrix 群组](element://room/!TRaVWNnQhAbvuiSnEK%3Amatrix.org?via=matrix.org)（`#reticulum:matrix.org`）
- [Reticulum Reddit 讨论版](https://reddit.com/r/reticulum)

## 安装
安装 Reticulum 及其相关工具最简单的方式是使用 pip：

```bash
pip install rns
```

安装完成后，你便可以启动任何依靠 Reticulum 运行的程序，或者是使用 [rnsd 工具](manual/using.html#the-rnsd-utility) 将 Reticulum 作为服务运行。

如果 `pip` 在你的系统上不可用，请首先安装 `python3` 与 `python3-pip`。

首次启动时，Reticulum 会创建一个默认的配置文件。它会试着连接本地可达的 Reticulum 节点(peer)。如果其中有些节点是”传输节点(Transport Instances)“，它们便可以让你连接上更大范围的网络。默认的配置文件提供了几个样例，以及用于创建复杂配置的参考。

如果想了解更多将通信扩展到各个媒介(如封包无线电，LoRa、串口、基于IP的高速连接、通过UDP/TCP连接互联网等)的细节，请参阅 [Reticulum 手册](manual/index.html) 的[受支持的界面](manual/interfaces.html)部分。

## 附带工具
Reticulum 附带了用于管理网络、查看状态与信息等用途的一系列工具。欲知详情，请参阅 [Reticulum 手册](manual/index.html)的[附带工具](manual/using.html#included-utility-programs)部分。

- 用于将 Reticulum 作为服务运行的守护进程（(Daemon) `rnsd`
- 用于查看界面信息的工具 `rnstatus`
- 用于查看与更改路径表(Path Tables)的工具 `rnpath`
- 用于检查与目标连接性的诊断工具 `rnprobe`
- 一个简单的文件传输工具 `rncp`
- 一个远程命令执行工具 `rnx`

以上提到的所有工具，包括 `rnx` 与 `rncp`，都运行的十分良好且可靠，就算是通过带宽非常低的连接（如 LoRa 与封包无线电）也一样。

## 使用 Reticulum 的程序
如果你想知道 Reticulum 能做什么，可以参考下面的链接。

- 无需基建、加密且可自恢复的网状通讯平台 [Nomad Network](https://github.com/markqvist/NomadNet)
- 带有图形界面、注重易用性、可在 Android、Linux 与 macOS 使用的 [Sideband](https://github.com/markqvist/sideband)
- 一个分布式、抗延迟、抗干扰、基于 Reticulum 的消息传输协议 [LXMF](https://github.com/markqvist/lxmf)

## 依赖处理
`rns` 包默认条件下的安装需要以下依赖。几乎所有的系统与发行版都有直接可用的包。如果是通过 `pip` 安装，这些依赖会直接被下载安装。

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

若使用的是较为少见的系统，或是在某种特殊情形下，上面的依赖不一定总是能安装或是编译成功。在这种情况下，你可以使用无需额外依赖的 `rnspure` 包。请注意`rns` 与 `rnspure`包的内容是*完全一致*的。唯一的区别是 `rnspure` 包没有显式包含需要安装的依赖。

不论安装 Reticulum 的手段为何，Reticulum 都会在*需要*且*可用*的情况下加载外部依赖。如果你想在一个不支持 [pyserial](https://github.com/pyserial/pyserial) 的系统上运行 Reticulum，使用 `rnspure` 包即可。但是 Reticulum 将无法使用基于串口的界面。所有其他模块仍旧会在需要时被 Reticulum 载入。

**注意！** 如果你在不支持 [PyCA/cryptography](https://github.com/pyca/cryptography) 的系统上使用 `rnspure` 包，请一定确保自己阅读并理解了[密码学原语（Cryptographic Primitives）](crypto.html)的相关内容。

## 性能
Reticulum 的性能差距范围会*非常*大。目前 Reticulum 会优先保证低带宽媒介的可用性与性能。Reticulum 的目标是提供一个 250 bps 到 1 Gbps(普通硬件条件下)的性能区间。

目前可用的性能区间是 500 bps 到 20 Mbps。更快的连接无法被充分利用。未来，Reticulum 可能会升级性能，但直到有线格式(wire format)和 API 完全稳定之前，性能升级都不会是优先事项。

<p align="right"><a href="hardware_zh-cn.html">下一个主题: 硬件支持</a></p>
