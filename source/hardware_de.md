
# Unterstützte Hardware
Reticulum kann über praktisch jedes Medium verwendet werden, das mindestens einen Halbduplex-Kanal mit einem Durchsatz von 500 Bit pro Sekunde und einer MTU von 500 Byte unterstützt. Datenfunkgeräte, Modems, LoRa-Funkgeräte, serielle Leitungen, AX.25-TNCs, digitale Amateurfunkmodi, WiFi- und Ethernet-Geräte, optische Verbindungen im freien Raum und ähnliche Systeme sind Beispiele für physische Geräte, die Reticulum verwenden kann. Zu den unterstützten Schnittstellentypen gehören:

- Jedes Ethernet-Gerät
- Fast alle WiFi-basierte Hardware
- LoRa mit [RNode](https://unsigned.io/projects/rnode/)
- Packet Radio TNCs (mit oder ohne AX.25)
- KISS-kompatible Hardware- und Software-Modems
- Jedes Gerät mit einer seriellen Schnittstelle
- TCP über IP Netzwerke
- UDP über IP Netzwerke
- Externe Programme über stdio oder Pipes
- Kundenspezifische Hardware über stdio oder Pipes

Ausführlichere Informationen und eine vollständige Liste der unterstützten Schnittstellentypen finden Sie in den Kapiteln [Kommunikationshardware](manual/hardware.html) und [Unterstützte Schnittstellen](manual/interfaces.html) des Handbuchs.

Reticulum kann auch über bestehende IP-Netzwerke gekapselt werden, so dass dem Einsatz über ein kabelgebundenes Ethernet, Ihr lokales WiFi-Netzwerk oder das Internet nichts im Wege steht, wo es genauso gut funktioniert. Eine der Stärken von Reticulum besteht darin, dass Sie verschiedene Medien ganz einfach zu einem selbstkonfigurierenden, robusten und verschlüsselten Mesh verbinden können, wobei jede verfügbare Infrastruktur genutzt werden kann.

So ist es beispielsweise möglich, einen Raspberry Pi sowohl mit einem LoRa-Funkgerät als auch mit einem Paketfunk-TNC und einem WiFi-Netzwerk zu verbinden. Sobald die Schnittstellen konfiguriert sind, kümmert sich Reticulum um den Rest, und jedes Gerät im WiFi-Netzwerk kann mit Knoten auf der LoRa- und Paketfunkseite des Netzwerks kommunizieren und umgekehrt.

<p align="right"><a href="connect_de.html">Nächstes Thema: Öffentliches Testnetz</a></p>
