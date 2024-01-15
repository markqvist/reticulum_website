# Ondersteunde hardware
Reticulum kan worden gebruikt via vrijwel elk medium dat ten minste een half-duplex kanaal met een doorvoersnelheid van 500 bits per seconde en een MTU van 500 bytes kan ondersteunen. Dataradio's, modems, LoRa-radio's, seriële lijnen, AX.25 TNC's, digitale amateurradiomodi, WiFi- en Ethernet-apparaten, optische verbindingen in de vrije ruimte en soortgelijke systemen zijn allemaal voorbeelden van de soorten fysieke apparaten die Reticulum kan gebruiken. De ondersteunde interfacetypen zijn onder meer:

- Elke ethernetinterface
- Bijna alle op WiFi gebaseerde hardware
- LoRa met behulp van [RNode](https://unsigned.io/rnode/)
- Packet Radio TNC's (met of zonder AX.25)
- KISS-compatibele hardware- en softwaremodems
- Elk apparaat met een seriële poort
- TCP over IP-netwerken
- UDP via IP-netwerken
- Externe programma's via stdio of pipelines
- Aangepaste hardware via stdio of pijpen

Voor meer gedetailleerde informatie en een volledige lijst met ondersteunde interfacetypen kunt u de hoofdstukken  [Communicatiehardware](manual/hardware.html) en [Ondersteunde interfaces](manual/interfaces.html) van de handleiding lezen.

Reticulum kan ook worden ingekapseld over bestaande IP-netwerken, dus niets houdt u tegen om het te gebruiken via bedraad ethernet, uw lokale WiFi-netwerk of internet, waar het net zo goed zal werken. Een van de sterke punten van Reticulum is in feite hoe gemakkelijk u verschillende media kunt verbinden tot een zelfconfigurerend, veerkrachtig en gecodeerd netwerk, met behulp van elke beschikbare mix van beschikbare infrastructuur.

Het is bijvoorbeeld mogelijk om een Raspberry Pi op te zetten die is aangesloten op zowel een LoRa-radio, een packet-radio-TNC als een WiFi-netwerk. Zodra de interfaces zijn geconfigureerd, zorgt Reticulum voor de rest, en elk apparaat op het WiFi-netwerk kan communiceren met knooppunten aan de LoRa- en pakketradiozijde van het netwerk, en vice versa.

<p align="right"><a href="connect.html">Volgend onderwerp: openbaar testnet</a></p>
