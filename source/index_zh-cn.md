
# Reticulum
Reticulum 是一个基于密码学的网络栈。人们可以用现有的硬件设备基于 Reticulum 搭建本地乃至广域的网络。它甚至可以在极高延迟与极低带宽的情况下运行。

目前的 Reticulum 能够让任何人运行自己的通讯网络。用独立、互联、自治的网络覆盖大片地域从未如此简单与低价。Reticulum 是为了人民、势不可挡的网络。

<p align="center"><img width="30%" src="gfx/reticulum_logo_512.png"></p>

Reticulum 不是*一个*网络，而是用于搭建*成千上万*网络的工具——成千上万个没有停止按钮（kill-switches）、没有监控、没有审查与控制，但却协调运作、有机结合、为了人类的网络。

在用户看来，Reticulum 能够用来创造尊重社区与个人的自治型与独立性的应用。它提供了无法被外部操纵、篡改、审查的安全数字通信。

Reticulum 可以构建下至小规模，大至全星球的网络体系，而无需任何层级或是官僚化的结构来控制与管理，同时还能保证社区与个人在自己那部分网络的完全自主权。

## 值得注意的特质（Notable Characteristics）
虽然 Reticulum 解决的是任何一个网络栈都会试着去解决的问题（把数据通过数个中间节点可靠地从一方传输到另一方），但是解决问题的方式却与其他网络技术相当不同。

- Reticulum 不使用源地址（source addresses）。发出包不会包含源地址、发送位置、机器与操作者之类的信息。
- Reticulum 中没有对于地址空间的中央控制。任何人都可以在需要的时候分配任意多的地址。
- Reticulum 保证端到端连接性。新生的地址会在几秒到数分钟之内全局可及。
- 地址是*[自主](https://zh.wikipedia.org/zh-cn/%E8%BA%AB%E4%BB%BD%E8%87%AA%E4%B8%BB%E6%9D%83)（[self-sovereign](https://en.wikipedia.org/wiki/Self-sovereign_identity)）*且*便携（portable）*的。它们可以在物理上被移动到网络的另一位置并仍旧保持可及。
- 所有通信都默认是由[现代、健壮的加密](crypto.html)保护的。
- 所有的加密密钥都是临时（ephemeral）的。通信默认自带前向保密（forward secrecy）。
- 不可能在 Reticulum 网络中建立未加密连接。
- 不可能在 Reticulum 网络中向任何目标发送未加密的数据包。
- 收到未加密数据包的目标会将数据包视为无效并丢弃。

<p align="right"><a href="start_zh-cn.html">下一个主题: 开始使用</a></p>
