# Şifreleme Temelleri
Reticulum, genel amaçlı CPU'lerde ve mikrodenetleyicilerde kullanılabilen yaygın olarak bulunan uygulamalara sahip, etkili, güçlü ve modern bir şifreleme temel paketi kullanır. Gerekli temel öğeler şunlardır:

- Dijital İmzalar için Ed25519
- ECDH anahtar değişimleri için X22519
- Anahtar oluşturmak için HKDF
- CBC modunda AES-128
- Mesaj doğrulama için HMAC-SHA256
- SHA-256
- SHA-512

Varsayılan kurulum yapılandırmasında, `X25519`, `Ed25519` ve `AES-128-CBC` temel öğeleri, [OpenSSL](https://www.openssl.org/) (aracılığıyla [PyCA/cryptography](https://github.com/pyca/cryptography) paketi üzerinden) tarafından sağlanır. Karma fonksiyonları `SHA-256` ve `SHA-512`, standart Python [hashlib](https://docs.python.org/3/library/hashlib.html) tarafından sağlanır. `HKDF`, `HMAC`, `Fernet` temel öğeleri ve `PKCS7` dolgu fonksiyonu her zaman şu içsel uygulamalar tarafından sağlanır:

- [HKDF.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HKDF.py)
- [HMAC.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/HMAC.py)
- [Fernet.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/Fernet.py)
- [PKCS7.py](https://github.com/markqvist/Reticulum/blob/master/RNS/Cryptography/PKCS7.py)

Reticulum ayrıca tüm gerekli temel öğelerin saf Python'da tam bir uygulamasını içerir. Reticulum başlatıldığında sistemde OpenSSL ve PyCA kullanılamıyorsa, Reticulum bunun yerine içsel saf Python temel öğelerini kullanacaktır. Bu durumun basit bir sonucu performanstır, çünkü OpenSSL *çok* daha hızlıdır. Ancak, en önemli sonuç, OpenSSL'den daha az inceleme, test ve gözden geçirme görmemiş temellerin kullanılmasıyla güvenlik kaybının potansiyelidir.

Eğer içsel saf Python temel öğelerini kullanmak istiyorsanız, bunun getirdiği riskleri iyi anlamanız ve bu risklerin sizin için kabul edilebilir olup olmadığına dair bilinçli bir karar vermeniz **son derece tavsiye edilir**.

Reticulum nispeten genç bir yazılımdır ve buna göre değerlendirilmelidir. Kriptografi en iyi uygulamaları gözetilerek inşa edilmiş olmasına rağmen, dış güvenlik denetimi yapılmamıştır ve gizlilik veya güvenlik ihlali yapabilecek hatalar olabilir. Yardımcı olmak veya maddi açıdan bir güvenlik denetimi yapılmasını desteklemek istiyorsanız, lütfen iletişime geçin.

<p align="right"><a href="credits.html">Sonraki Konu: Teşekkürler ve Saygılar</a></p>