# Genel Test Ağı
Eğer fiziksel ağlar oluşturmadan sadece denemelere başlamak istiyorsanız, Genel Reticulum Test Ağı'na katılmaktan hoş geldiniz. Test ağı tam olarak bunun için, test etmek ve denemeler yapmak için gayri resmi bir ağdır. Çoğu zaman aktif olacak ve herkes katılabilir, ancak bu aynı zamanda hizmetin sürekli kullanılabilirliği için garanti olmadığı anlamına gelir.

Test ağı, Reticulum'un en güncel sürümünü çalıştırır (çoğu zaman genel olarak yayınlanmadan kısa bir süre önce). Ara sıra Reticulum'un deneysel sürümleri, test ağındaki düğümlere dağıtılabilir, bu da tuhaf davranışlara neden olabilir. Eğer hiçbiri sizi korkutmuyorsa, test ağına TCP veya I2P aracılığıyla katılabilirsiniz.

Reticulum yapılandırma dosyanıza aşağıdaki arayüzlerden birini ekleyin:

```
# Dublin Hub için TCP/IP arabirimi
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# BetweenTheBorders Hub için TCP/IP arabirimi (topluluk tarafından sağlanmış)
  [[RNS Testnet BetweenTheBorders]]
    type = TCPClientInterface
    enabled = yes
    target_host = betweentheborders.com
    target_port = 4242

# I2P Hub A için arabirim
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = g3br23bvx3lq5uddcsjii74xgmn6y5q325ovrkq2zw2wbzbqgbuq.b32.i2p
```

Test ayrıca bir dizi [Nomad Network](https://github.com/markqvist/nomadnet) düğümü ve [LXMF](https://github.com/markqvist/lxmf) yayılma düğümü içerir.

<p align="right"><a href="docs_tr.html">Sonraki Konu: Kılavuzu Okuyun</a></p>