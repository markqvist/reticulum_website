# 公共测试网络

如果你只是想立刻上手使用，而不想搭建物理意义上的网络的话，你可以加入公开的 Reticulum 测试网络。这是一个非正式的用于测试与实验的网络。大部分时间它都会在线，所有人都可以加入。同时，“测试”也意味着没有可用性保障。

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

<p align="right"><a href="docs_zh-cn.html">下一个主题：阅读手册</a></p>
