# Openbaar Testnet
Als je gewoon wilt beginnen met experimenteren zonder fysieke netwerken te bouwen, ben je van harte welkom om lid te worden van het Public Reticulum Testnet. Het testnet is precies dat: een informeel netwerk voor testen en experimenteren. Het zal het grootste deel van de tijd actief zijn en iedereen kan meedoen, maar het betekent ook dat er geen garanties zijn voor de beschikbaarheid van de service.

Het testnet draait de allernieuwste versie van Reticulum (vaak zelfs kort voordat deze publiekelijk wordt vrijgegeven). Soms kunnen experimentele versies van Reticulum worden ingezet op knooppunten op het testnet, wat betekent dat er vreemd gedrag kan optreden. Als dit u allemaal niet afschrikt, kunt u zich via TCP of I2P bij het testnet aansluiten.

Voeg gewoon een van de volgende interfaces toe aan uw Reticulum-configuratiebestand:

```
# TCP/IP interface to the Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# TCP/IP interface to the BetweenTheBorders Hub (door de gemeenschap geleverd)
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

Het testnet bevat ook een aantal [Nomad Network](https://github.com/markqvist/nomadnet) knooppunten en [LXMF](https://github.com/markqvist/lxmf) propagatieknooppunten.

# Community Entrypoints
De community heeft een aantal openbaar beschikbare entrypoints voor Reticulum-netwerken geleverd. Voor dagelijks gebruik is het raadzaam om deze te gebruiken in plaats van het testnet.

U kunt uw apparaten of instanties verbinden met een of meer van deze om toegang te krijgen tot alle Reticulum-netwerken waarmee ze fysiek verbonden zijn.

Idealiter stelt u een Reticulum Transport Node in die uw eigen apparaten lokaal kunnen bereiken en verbindt u die transport node vervolgens met een aantal openbare entrypoints. Dit zorgt voor efficiënte verbindingen en redundantie in het geval dat een van hen uitvalt.

{PUBLIC_ENTRYPOINTS}

<p align="right"><a href="docs_nl.html">Volgend onderwerp: lees de handleiding</a></p>
