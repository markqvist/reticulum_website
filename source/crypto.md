# Cryptographic Primitives
Reticulum uses a simple suite of efficient, strong and well-tested cryptographic primitives, with widely available implementations that can be used both on general-purpose CPUs and on microcontrollers.

One of the primary considerations for choosing this particular set of primitives is that they can be implemented *safely* with relatively few pitfalls, on practically all current computing platforms.

The primitives listed here **are authoritative**. Anything claiming to be Reticulum, but not using these exact primitives **is not** Reticulum, and possibly an intentionally compromised or weakened clone. The utilised primitives are:

- Ed25519 for signatures
- X22519 for ECDH key exchanges
- HKDF for key derivation
- AES-128 in CBC mode
- AES-256 in CBC mode
- HMAC-SHA256 for message authentication
- SHA-256
- SHA-512

In the default installation configuration, the `X25519`, `Ed25519` and `AES-128-CBC` primitives are provided by [OpenSSL](https://www.openssl.org/) (via the [PyCA/cryptography](https://github.com/pyca/cryptography) package). The hashing functions `SHA-256` and `SHA-512` are provided by the standard Python [hashlib](https://docs.python.org/3/library/hashlib.html). The `HKDF`, `HMAC`, `Fernet` primitives, and the `PKCS7` padding function are always provided by the following internal implementations:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)


Reticulum also includes a complete implementation of all necessary primitives in pure Python. If OpenSSL & PyCA are not available on the system when Reticulum is started, Reticulum will instead use the internal pure-python primitives. A trivial consequence of this is performance, with the OpenSSL backend being *much* faster. The most important consequence however, is the potential loss of security by using primitives that has not seen the same amount of scrutiny, testing and review as those from OpenSSL.

If you want to use the internal pure-python primitives, it is **highly advisable** that you have a good understanding of the risks that this pose, and make an informed decision on whether those risks are acceptable to you.

Reticulum is relatively young software, and should be considered as such. While it has been built with cryptography best-practices very foremost in mind, it _has not_ been externally security audited, and there could very well be privacy or security breaking bugs. If you want to help out, or help sponsor an audit, please do get in touch.

<p align="right"><a href="credits.html">Next Topic: Acknowledgements & Credits</a></p>
