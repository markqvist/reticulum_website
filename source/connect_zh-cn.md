# 公共测试网络

如果你只是想立刻上手使用，而不想搭建物理意义上的网络的话，你可以加入公开的 Reticulum 测试网络。这是一个非正式的用于测试与实验的网络。大部分时间它都会在线，所有人都可以加入。同时，“测试”也意味着没有可用性保障。

**请注意！**对于 Reticulum 的日常使用，例如消息传递和其他通信，最好使用社区提供的一个或多个公共入口点。请参阅下一节了解详细信息。

测试网络运行的是最新版的 Reticulum（甚至会在正式发布之前更新）。有时实验版的 Reticulum 会被部署到测试网络的节点之上，这可能会产生奇怪的行为。如果这些都没让你感到害怕，欢迎通过 TCP 或是 I2P 加入测试网络。

你仅需在 Reticulum 的配置文件中加入以下任意一个界面：

```
# Dublin Hub 的 TCP/IP 界面
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# BetweenTheBorders Hub (社区提供) 的 TCP/IP 界面
  [[RNS Testnet BetweenTheBorders]]
    type = TCPClientInterface
    enabled = yes
    target_host = reticulum.betweentheborders.com
    target_port = 4242

# I2P Hub A 界面
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = g3br23bvx3lq5uddcsjii74xgmn6y5q325ovrkq2zw2wbzbqgbuq.b32.i2p
```

测试网络中还有几个 [Nomad Network](https://github.com/markqvist/nomadnet) 节点和 [LXMF](https://github.com/markqvist/lxmf) 传播节点（propagation nodes）。

# 社区入口点
社区提供了许多可公开访问的 Reticulum 网络入口点。对于日常使用，建议使用这些入口点而不是测试网。

您可以将设备或实例连接到其中一个或多个入口点，以访问它们物理连接的任何 Reticulum 网络。

理想情况下，设置一个您自己的设备可以在本地访问的 Reticulum 传输节点，然后将该传输节点连接到几个公共入口点。这将提供有效的连接和冗余，以防其中任何一个出现故障。

{PUBLIC_ENTRYPOINTS}

<p align="right"><a href="docs_zh-cn.html">下一个主题：阅读手册</a></p>
