# Cryptografische primitieven
Reticulum maakt gebruik van een eenvoudige reeks efficiënte, sterke en moderne cryptografische primitieven, met algemeen beschikbare implementaties die zowel op CPU's voor algemene doeleinden als op microcontrollers kunnen worden gebruikt. De noodzakelijke primitieven zijn:

- Ed25519 voor handtekeningen
- X22519 voor ECDH-sleuteluitwisselingen
- HKDF voor sleutelafleiding
- AES-128 in CBC-modus
- HMAC-SHA256 voor berichtauthenticatie
- SHA-256
- SHA-512

In de standaard installatieconfiguratie worden de primitieven `X25519`, `Ed25519` en `AES-128-CBC` geleverd door [OpenSSL](https://www.openssl.org/) (via het [PyCA/cryptography](https://github.com/pyca/cryptography) pakket). De hashfuncties `SHA-256` and `SHA-512` worden geleverd door de standaard Python [hashlib](https://docs.python.org/3/library/hashlib.html). De `HKDF`, `HMAC`, `Fernet` primitieven en de `PKCS7` opvullingsfunctie worden altijd geleverd door de volgende interne implementaties:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)


Reticulum bevat ook een volledige implementatie van alle benodigde primitieven in pure Python. Als OpenSSL en PyCA niet beschikbaar zijn op het systeem wanneer Reticulum wordt gestart, zal Reticulum in plaats daarvan de interne pure-python-primitieven gebruiken. Een triviaal gevolg hiervan zijn de prestaties, waarbij de OpenSSL-backend *veel* sneller is. Het belangrijkste gevolg is echter het potentiële verlies aan veiligheid door het gebruik van primitieven die niet dezelfde hoeveelheid onderzoek, testen en beoordeling hebben ondergaan als die van OpenSSL.

Als u de interne pure Python-primitieven wilt gebruiken, is het **zeer aan te raden** dat u een goed inzicht heeft in de risico's die dit met zich meebrengt, en een weloverwogen beslissing neemt of deze risico's voor u acceptabel zijn.

Reticulum is relatief jonge software en moet als zodanig worden beschouwd. Hoewel het is gebouwd met de best practices op het gebied van cryptografie in het achterhoofd, is er geen externe beveiligingsaudit uitgevoerd en kunnen er bugs in zitten die de privacy of de beveiliging schenden. Als u wilt helpen of een audit wilt sponsoren, neem dan contact met ons op.

<p align="right"><a href="credits.html">Volgend onderwerp: dankbetuigingen en credits</a></p>
