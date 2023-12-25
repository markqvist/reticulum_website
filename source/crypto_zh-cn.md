# 密码学原语（Cryptographic Primitives）
Reticulum 使用了一系列高效、健壮、现代的密码学原语（cryptographic primitives）。它们都有着被广泛使用的现成的实现，在一般的 CPU 或是微控制器上都可以运行。这些必要的原语是：

- Ed25519 用于签名
- X22519 用于 ECDH 密钥交换
- HKDF 用于密钥派生
- AES-128 CBC 模式
- HMAC-SHA256 用于消息认证
- SHA-256
- SHA-512

在默认安装下，`X25519`、`Ed25519` 和 `AES-128-CBC` 都由 [OpenSSL](https://www.openssl.org/) 提供（通过[PyCA/cryptography](https://github.com/pyca/cryptography)）。散列函数 `SHA-256` 和 `SHA-512` 由 Python 标准库 [hashlib](https://docs.python.org/3/library/hashlib.html) 提供。`HKDF`、`HMAC`、`Fernet` 原语与 `PKCS7` 填充函数总是由以下内部实现提供：

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)

Reticulum 还包含了所有所需密码学原语的纯 Python 实现。如果 OpenSSL 和 PyCA 在系统上不可用的话，Reticulum 会使用自带的纯Python实现。这时，最明显的影响是速度——OpenSSL作为后端会*快的多*。然而最严重的影响，则可能是使用这些没有经受过与 OpenSSL 同级别安全审查、测试与评估的实现所带来的安全性问题。

如果你想使用自带的纯 Python 实现，我非常建议你充分了解可能的风险，并仔细思考这些风险是否适用在你身上。

Reticulum 目前还十分年轻，这一点必须牢记于心。虽说在构建时，开发者尽量遵守了密码学的最佳实践，但它*还没有*受过外部的安全审计，而且很可能会有破坏隐私或是安全性的 Bug。如果你愿意帮忙，或是愿意赞助进行安全审计，请联系开发者。

<p align="right"><a href="credits_zh-cn.html">下一个主题: 致谢与署名</a></p>
