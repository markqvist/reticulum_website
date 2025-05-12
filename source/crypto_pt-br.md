# Primitivos Criptográficos
Reticulum utiliza uma suíte simples de primitivos criptográficos modernos, fortes e eficientes, com diversas implementações disponíveis que pode ser utilizados tanto em CPUs convencionais como microcontroladores. Os primitivos necessários são:

- Ed25519 para assinaturas
- X22519 para trocas de chave ECDH
- HKDF para derivação de chaves
- AES-256 em modo CBC
- HMAC-SHA256 para autenticação de mensagem
- SHA-256
- SHA-512

Na configuração de instalação padrão, os primitivos `X25519`, `Ed25519` e `AES-256-CBC` são fornecidos pela [OpenSSL](https://www.openssl.org/) (pelo pacote [PyCA/cryptography](https://github.com/pyca/cryptography) ). As funções de hash `SHA-256` e `SHA-512` são fornecidas pela biblioteca Python [hashlib](https://docs.python.org/3/library/hashlib.html). Os primitivos `HKDF`, `HMAC`, `Token`, e a função de preenchimento `PKCS7` são sempre fornecidas pelas seguintes implementações internas:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Token.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Token.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)


Reticulum também incluí a implementação completa de todos os primitivos necessários em Python puro. Se o OpenSSL & PyCA não estão disponíveis no sistema que o Reticulum é iniciado, Reticulum vai utilizar os primitivos internos. A consequência trivial disso é o desempenho, com a biblioteca OpenSSL sendo mais rápida. A consequência mais importante no entanto, é a potencial perda de segurança por utilizar primitivos que não possuem o mesmo nível de suporte, teste e revisão que o OpenSSL.

Se você quer utilizar primitivos internos em Python, é aconselhável que você entenda os riscos envolvidos, e tome uma decisão informada conforme os ricos são aceitáveis para você.

Reticulum é um software relativamente jovem, e deve ser considerado como tal. Enquanto ele é desenvolvido com as melhores práticas de criptografia em mente, ainda não foi auditado externamente, e pode haver bugs para segurança e privacidade. Se você quer ajudar, ou patrocinar uma auditoria, nos informe.

<p align="right"><a href="credits_pt-br.html">Próxima Página: Agradecimentos & Créditos</a></p>
