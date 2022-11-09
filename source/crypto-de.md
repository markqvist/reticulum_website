# Kryptographische Primitive
Reticulum verwendet eine einfache Reihe von effizienten, starken und modernen kryptographischen Primitiven mit weithin verfügbaren Implementierungen, die sowohl auf Allzweck-CPUs als auch auf Mikrocontrollern verwendet werden können. Die notwendigen Primitive sind:

- Ed25519 für Signaturen
- X22519 für ECDH Schlüsselaustausch
- HKDF für die Schlüsselableitung
- AES-128 im CBC modus
- HMAC-SHA256 für die Nachrichtenauthentifizierung
- SHA-256
- SHA-512

In der Standard-Installationskonfiguration werden die Primitive `X25519`, `Ed25519` und `AES-128-CBC` von [OpenSSL](https://www.openssl.org/) (mit dem [PyCA/cryptography](https://github.com/pyca/cryptography) Packet mitgebracht). Die Hashing-Funktionen `SHA-256` und `SHA-512` werden vom Standard-Python bereitgestellt [hashlib](https://docs.python.org/3/library/hashlib.html). Die `HKDF`, `HMAC`, `Fernet` Primitive, und die `PKCS7` Auffüllfunktion werden immer von den folgenden internen Implementierungen bereitgestellt:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)


Reticulum enthält außerdem eine vollständige Implementierung aller erforderlichen Primitive in reinem Python. Wenn OpenSSL und PyCA beim Start von Reticulum nicht auf dem System verfügbar sind, verwendet Reticulum stattdessen die internen reinen Python-Primitive. Eine triviale Folge hiervon ist die Leistung, da das OpenSSL-Backend *viel* schneller ist. Die wichtigste Konsequenz ist jedoch der potenzielle Verlust an Sicherheit durch die Verwendung von Primitiven, die nicht in gleichem Maße wie die von OpenSSL untersucht, getestet und geprüft wurden.

Wenn Sie die internen reinen Python-Primitive verwenden wollen, ist es **sehr ratsam**, dass Sie die damit verbundenen Risiken gut verstehen und eine fundierte Entscheidung darüber treffen, ob diese Risiken für Sie akzeptabel sind.

Reticulum ist eine relativ junge Software, die als solche betrachtet werden sollte. Obwohl es unter Berücksichtigung der besten Kryptographie-Praktiken entwickelt wurde, ist es _nicht_ extern sicherheitsgeprüft worden, und es könnte sehr wohl Fehler enthalten, die den Datenschutz oder die Sicherheit verletzen. Wenn Sie mithelfen oder ein Audit sponsern wollen, nehmen Sie bitte Kontakt auf.

<p align="right"><a href="credits.html">Nächstes Thema: Danksagungen & Credits</a></p>