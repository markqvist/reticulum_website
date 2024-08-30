# Publiczny Testnet
Jeśli chcesz po prostu zacząć eksperymentować bez budowania fizycznych sieci, zachęcam do przyłączenia się do Publicznego Testnetu Reticulum. Testnet to po prostu nieformalna sieć do testowania i eksperymentowania. Będzie działać przez większość czasu i każdy może do niej dołączyć, ale oznacza to również, że nie ma gwarancji dostępności usług.

W sieci testowej działa najnowsza wersja Reticulum (często nawet krótko przed jej publicznym udostępnieniem). Czasami eksperymentalne wersje Reticulum mogą zostać wdrożone do węzłów w sieci testowej, co oznacza, że ​​mogą wystąpić dziwne zachowania. Jeśli Ciebie to nie przeraża, możesz dołączyć do sieci testowej przez TCP lub I2P.

Dodaj jeden z następujących interfejsów do pliku konfiguracyjnego Reticulum:

```
# TCP/IP interface to the Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# TCP/IP interface to the BetweenTheBorders Hub (community-provided)
  [[RNS Testnet BetweenTheBorders]]
    type = TCPClientInterface
    enabled = yes
    target_host = reticulum.betweentheborders.com
    target_port = 4242

# Interface to I2P Hub A
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = g3br23bvx3lq5uddcsjii74xgmn6y5q325ovrkq2zw2wbzbqgbuq.b32.i2p
```

Testnet zawiera również liczne węzły [Nomad Network](https://github.com/markqvist/nomadnet), i węzły propagacyjne [LXMF](https://github.com/markqvist/lxmf).

<p align="right"><a href="docs_pl.html">Następny Temat: Przeczytaj Podręcznik</a></p>
