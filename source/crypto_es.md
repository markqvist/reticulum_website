# Primitivas Criptográficas
Reticulum utiliza un conjunto sencillo de primitivas criptográficas eficientes, potentes y modernas, con implementaciones ampliamente disponibles que pueden utilizarse tanto en CPU de propósito general como en microcontroladores. Las primitivas necesarias son:

- Ed25519 para firmas
- X22519 para cambios de llaves ECDH
- HKDF para derivación de llaves
- AES-128 en modo CBC
- HMAC-SHA256 para autenticación de mensajes
- SHA-256
- SHA-512

En la configuración de instalación por defecto, las primitivas `X25519`, `Ed25519` y `AES-128-CBC` son proporcionadas por [OpenSSL](https://www.openssl.org/) (a través del paquete [PyCA/cryptography](https://github.com/pyca/cryptography)). Las funciones hash `SHA-256` y `SHA-512` las proporciona el paquete estándar de Python [hashlib](https://docs.python.org/3/library/hashlib.html). Las primitivas `HKDF`, `HMAC`, `Fernet` y la función de relleno `PKCS7` son siempre proporcionadas por las siguientes implementaciones internas:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)

Reticulum también incluye una implementación completa de todas las primitivas necesarias en Python puro. Si OpenSSL y PyCA no están disponibles en el sistema cuando se inicia Reticulum, éste utilizará en su lugar las primitivas internas de Python puro. Una consecuencia trivial de esto es el rendimiento, ya que el backend OpenSSL es *mucho* más rápido. Sin embargo, la consecuencia más importante es la pérdida potencial de seguridad al utilizar primitivas que no han sido sometidas a la misma cantidad de escrutinio, pruebas y revisiones que las de OpenSSL.

Si desea utilizar las primitivas internas de Python puro, es **altamente recomendable** que usted tenga una buena comprensión de los riesgos que esto plantea, y tomar una decisión informada sobre si esos riesgos son aceptables para usted.

Reticulum es un software relativamente joven y debe ser considerado como tal. Aunque se ha construido teniendo muy presentes las mejores prácticas criptográficas, _no_ ha sido auditado externamente en materia de seguridad, y es muy posible que haya errores que rompan la privacidad o la seguridad. Si quieres ayudar o patrocinar una auditoría, ponete en contacto con nosotros.

<p align="right"><a href="credits_es.html">Siguiente tema: Agradecimientos y créditos</a></p>
