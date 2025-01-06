# Öffentliches Testnetz
Wenn Sie einfach nur experimentieren wollen, ohne ein physisches Netzwerk aufzubauen, können Sie sich gerne dem öffentlichen Reticulum Testnet anschließen. Das Testnetz ist genau das: ein informelles Netzwerk zum Testen und Experimentieren. Es wird die meiste Zeit verfügbar sein, und jeder kann mitmachen, aber das bedeutet auch, dass es keine Garantien für die Verfügbarkeit der Dienste gibt.

Auf dem Testnetz läuft die allerneueste Version von Reticulum (oft sogar kurz vor der öffentlichen Freigabe). Manchmal werden experimentelle Versionen von Reticulum auf Knoten im Testnetz eingesetzt, was bedeutet, dass seltsames Verhalten auftreten kann. 
Wenn Sie das alles nicht abschreckt, können Sie dem Testnetz über TCP oder I2P beitreten.

Fügen Sie einfach eine der folgenden Schnittstellen in Ihre Reticulum-Konfigurationsdatei ein:

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

Das Testnetz enthält auch eine Reihe von [Nomad Network](https://github.com/markqvist/nomadnet)-Knoten und [LXMF](https://github.com/markqvist/lxmf)-Propagationsknoten, Sowie [Sideband](https://github.com/markqvist/Sideband) Peers, welche untereinander erreichbar sind.

# Community-Einstiegspunkte
Die Community hat eine Reihe öffentlich verfügbarer Einstiegspunkte zu Reticulum-Netzwerken bereitgestellt. Für den alltäglichen Gebrauch wird empfohlen, diese anstelle des Testnetzes zu verwenden.

Sie können Ihre Geräte oder Instanzen mit einem oder mehreren dieser Punkte verbinden, um Zugriff auf alle Reticulum-Netzwerke zu erhalten, mit denen sie physisch verbunden sind.

Richten Sie im Idealfall einen Reticulum-Transportknoten ein, den Ihre eigenen Geräte lokal erreichen können, und verbinden Sie diesen Transportknoten dann mit einigen öffentlichen Einstiegspunkten. Dies sorgt für effiziente Verbindungen und Redundanz, falls einer von ihnen ausfällt.

{PUBLIC_ENTRYPOINTS}

<p align="right"><a href="docs_de.html">Nächstes Thema: Lesen Sie das Handbuch</a></p>
