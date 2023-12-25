# 暗号プリミティブ
Reticulumは、効率的で強力かつ現代的な暗号プリミティブのシンプルなスイートを使用しています。これらは、一般的な用途のCPUおよびマイクロコントローラーの両方で使用できる広く利用可能な実装を備えています。必要なプリミティブには以下が含まれます：

- 署名用のEd25519
- ECDH鍵交換用のX22519
- 鍵導出用のHKDF
- CBCモードでのAES-128
- メッセージ認証用のHMAC-SHA256
- SHA-256
- SHA-512

デフォルトのインストール構成では、`X25519`、`Ed25519`、および`AES-128-CBC`のプリミティブは[OpenSSL](https://www.openssl.org/)（[PyCA/cryptography](https://github.com/pyca/cryptography)パッケージを介して）によって提供されます。ハッシュ関数`SHA-256`および`SHA-512`は、標準のPython [hashlib](https://docs.python.org/3/library/hashlib.html)によって提供されています。`HKDF`、`HMAC`、`Fernet`プリミティブ、および`PKCS7`パディング関数は、常に次の内部実装によって提供されます：

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)

Reticulumには、すべての必要なプリミティブの純粋なPythonによる完全な実装も含まれています。Reticulumが開始されるときにシステムにOpenSSL＆PyCAが利用できない場合、Reticulumは代わりに内部の純粋なPythonプリミティブを使用します。これの取り決めの一因はパフォーマンスであり、OpenSSLバックエンドが非常に速いことです。しかし、最も重要な結果は、OpenSSLと同じくらいの精査、テスト、およびレビューを受けていないプリミティブを使用することによるセキュリティの潜在的な損失です。

内部の純粋なPythonプリミティブを使用したい場合は、このリスクが許容できるかどうかを検討し、よく理解した上で情報を得ることが**強くお勧め**されます。

Reticulumは比較的新しいソフトウェアであり、それに準じて考えるべきです。暗号化のベストプラクティスを非常に重視して構築されていますが、外部からのセキュリティ監査はまだ行われておらず、プライバシーやセキュリティを崩壊させる可能性があります。協力したり、監査をスポンサーしたりしたい場合は、どうぞお知らせください。

<p align="right"><a href="credits.html">次のトピック: 謝辞とクレジット</a></p>
