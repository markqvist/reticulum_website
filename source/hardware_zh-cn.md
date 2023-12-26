# 硬件支持
Reticulum 可以被用在任意一个最低支持 500 bps 吞吐量、具有 500 字节 MTU(最大传输单元)的半/全双工信道上。Reticulum 支持各种物理设备：数字无线电、调制解调器、LoRa 无线电、串口线、AX.25 终端节点控制器(TNCs)、业余无线电台的数字模式、WiFi与以太网、自由空间光通信等等。以下是一个简单列表：

- 任意以太网设备
- 几乎所有基于 WiFi 的硬件
- LoRa (使用 [RNode](https://unsigned.io/rnode/))
- 封包无线电 TNC(带或不带 AX.25 均可)
- 兼容KISS的硬件或软件调制解调器
- 任何带串口的设备
- TCP over IP
- UDP over IP
- 外部程序(通过 stdio 或是管道)
- 自制硬件(通过 stdio 或是管道)

若想了解更多细节或是查看完整的支持列表，请参阅手册的[通信硬件(Communications Hardware)](manual/hardware.html)与[受支持的界面(Supported Interfaces)](manual/interfaces.html)部分。

Reticulum 也可以在现有的 IP 网络之上建立连接，因此你也能在有线以太网，本地无线网或是互联网上使用它。事实上，Reticulum 的一大优势就是允许你混合使用各种基础设施，把不同的传输介质连接成一个自配置、自恢复、强加密的网状网络。

就比如，你可以搭建一个连着 LoRa 无线电、封包无线电 TNC 和 WiFi 的树莓派。在这些硬件都设置好之后，Reticulum 会处理剩下的一切——所有在 WiFi 一侧的设备便可以和无线电一侧的设备自由通信了，反之亦然。

<p align="right"><a href="connect_zh-cn.html">下一个主题: 公共测试网络</a></p>
