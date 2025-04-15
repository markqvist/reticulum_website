# Prymitywy kryptograficzne
Reticulum wykorzystuje prosty zestaw wydajnych, silnych i nowoczesnych prymitywów kryptograficznych, z szeroko dostępnymi implementacjami, które mogą być używane zarówno na procesorach ogólnego przeznaczenia, jak i na mikrokontrolerach. Niezbędne prymitywy to:

- Ed25519 dla sygnatur
- X22519 dla wymiany kluczy ECDH
- HKDF dla wyodrębnienia klucza
- AES-128 w trybie CBC
- AES-256 w trybie CBC
- HMAC-SHA256 dla uwierzytelnienia wiadomości
- SHA-256
- SHA-512

W domyślnej konfiguracji instalacji, prymitywy `X25519`, `Ed25519`, `AES-128-CBC` i `AES-256-CBC` są dostarczone przez [OpenSSL](https://www.openssl.org/) (przez pakiet [PyCA/cryptography](https://github.com/pyca/cryptography)). Funkcja hashu `SHA-256` i `SHA-512` są dostarczone przez standard Pythona [hashlib](https://docs.python.org/3/library/hashlib.html). Prymitywy `HKDF`, `HMAC`, `Fernet` i funkcja padding `PKCS7` są zawsze dostarczane przez następujące wewnętrzne implementacje:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)


Reticulum zawiera również kompletną implementację wszystkich niezbędnych prymitywów w czystym Pythonie. Jeśli OpenSSL i PyCA nie są dostępne w systemie podczas uruchamiania Reticulum, Reticulum użyje wewnętrznych prymitywów w czystym Pythonie. Trywialną konsekwencją tego jest wydajność, backend OpenSSL jest *znacznie* szybszy. Najważniejszą konsekwencją jest jednak potencjalna utrata bezpieczeństwa poprzez użycie prymitywów, które nie zostały poddane takiej samej analizie, testom i przeglądom jak te z OpenSSL.

Jeśli chcesz używać wewnętrznych czystych prymitywów pythona, jest **bardzo wskazane**, abyś dobrze rozumiał ryzyko, jakie to stwarza, i podjął świadomą decyzję, czy to ryzyko jest dla ciebie do przyjęcia.

Reticulum jest stosunkowo młodym oprogramowaniem i powinno być traktowane jako takie. Chociaż zostało zbudowane z myślą o najlepszych praktykach kryptograficznych, _nie zostało_ poddane zewnętrznemu audytowi bezpieczeństwa i bardzo możliwe, że zawiera błędy naruszające prywatność lub bezpieczeństwo. Jeśli chcesz pomóc lub zasponsorować audyt, skontaktuj się ze mną.

<p align="right"><a href="credits_pl.html">Next Topic: Podziękowania & Zasługi</a></p>
