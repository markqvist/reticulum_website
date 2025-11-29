# Los geht's
Wie Sie am besten mit dem Reticulum Network Stack beginnen, hängt davon ab, was
Sie durchführen möchten. Ausführliche Informationen und Beispiele finden Sie im Abschnitt [Schneller Einstieg](manual/gettingstartedfast.html) des [Reticulum-Handbuchs](manual/index.html).

## Gemeinschaft & Unterstützung
Wenn Sie Probleme haben oder etwas nicht funktioniert, finden Sie hier einige gute Stellen, an denen Sie um Hilfe bitten können:

- Das [Diskussionsforum](https://github.com/markqvist/Reticulum/discussions) auf GitHub
- Der [Reticulum-Matrixkanal](https://matrix.to/#/#reticulum:matrix.org) bei `#reticulum:matrix.org`
- Der [Reticulum-Subreddit](https://reddit.com/r/reticulum)

## Installation
Der einfachste Weg, Reticulum und zugehörige Dienstprogramme auf Ihrem System zu installieren, ist über pip:

```bash
pip install rns
```

Sie können dann jedes Programm starten, das Reticulum verwendet, oder Reticulum als Systemdienst starten mit [dem Dienstprogramm rnsd] .(manual/using.html#the-rnsd-utility).

Wenn `pip` auf Ihrem System nicht verfügbar ist, installieren Sie zuerst die Pakete `python3` und `python3-pip` für Ihr Betriebssystem.

Beim ersten Start erstellt Reticulum eine Standardkonfigurationsdatei, die eine grundlegende Konnektivität zu anderen Reticulum-Peers herstellt, die lokal erreichbar sein könnten. Wenn es sich bei einem dieser lokalen Peers um eine Transportinstanz handelt, können Sie über diese eine Verbindung zu einem größeren Netzwerk herstellen. Die Standardkonfigurationsdatei enthält einige Beispiele und Referenzen für die Erstellung einer komplexeren Konfiguration.

Ausführlichere Beispiele für die Erweiterung der Kommunikation über verschiedene Medien wie Packet Radio oder LoRa, serielle Schnittstellen oder über schnelle IP-Verbindungen und das Internet unter Verwendung der UDP- und TCP-Schnittstellen finden Sie im Abschnitt [Unterstützte Schnittstellen](manual/interfaces.html) im [Reticulum Handbuch](manual/index.html).


## Enthaltene Dienstprogramme
Reticulum enthält eine Reihe nützlicher Hilfsprogramme zur Verwaltung Ihrer Netzwerke, zur Anzeige von Status und Informationen und für andere Aufgaben. Weitere Informationen zu diesen Programmen finden Sie im Abschnitt [Enthaltene Dienstprogramme](manual/using.html#included-utility-programs) im [Reticulum Handbuch](manual/index.html).

- Der System-Daemon `rnsd` für den Betrieb von Reticulum als immer verfügbarer Dienst
- Ein Dienstprogramm für den Schnittstellenstatus namens `rnstatus`, das Informationen über Schnittstellen anzeigt
- Das Werkzeug `rnpath` zum Nachschlagen und Verwalten von Pfaden, mit dem Sie Pfad-Tabellen anzeigen und ändern können
- Ein Diagnosewerkzeug namens `rnprobe` zur Überprüfung der Konnektivität zu Zielen
- Ein einfaches Dateiübertragungsprogramm namens `rncp`, das das Kopieren von Dateien auf entfernte Systeme erleichtert
- Das Programm `rnx` zur Ausführung von Fernbefehlen, mit dem Sie Befehle und Programme ausführen und Ausgaben von entfernten Systemen abrufen können

Alle Tools, einschließlich `rnx` und `rncp`, arbeiten zuverlässig und gut auch über Verbindungen mit sehr geringer Bandbreite wie LoRa oder Packet Radio.

## Programme welche Reticulum verwenden
Wenn Sie sich schnell einen Überblick über die Möglichkeiten von Reticulum verschaffen möchten, werfen Sie einen Blick auf die folgenden Ressourcen.

- Eine netzunabhängige, verschlüsselte und widerstandsfähige Mesh-Kommunikationsplattform finden Sie unter [Nomad Network](https://github.com/markqvist/NomadNet)
- Die Android-, Linux- und macOS-Anwendung [Sideband](https://github.com/markqvist/sideband) verfügt über eine grafische Oberfläche und legt den Schwerpunkt auf Benutzerfreundlichkeit.
- [LXMF](https://github.com/markqvist/lxmf) ist ein verteiltes, verzögerungs- und unterbrechungstolerantes Nachrichtenübertragungsprotokoll, das auf Reticulum aufbaut.

## Abhängigkeiten
Die Installation des Standardpakets `rns` erfordert die unten aufgeführten Abhängigkeiten. Fast alle Systeme und Distributionen haben leicht verfügbare Pakete für diese Abhängigkeiten, und wenn das `rns`-Paket mit `pip` installiert wird, werden sie ebenfalls heruntergeladen und installiert.

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

Auf ungewöhnlicheren Systemen und in einigen seltenen Fällen ist es möglicherweise nicht möglich, eines oder mehrere der oben genannten Module zu installieren oder gar zu kompilieren. In solchen Situationen können Sie stattdessen das Paket `rnspure` verwenden, das keine externen Abhängigkeiten für die Installation benötigt. Bitte beachten Sie, dass der Inhalt der Pakete `rns` und `rnspure` *identisch* ist. Der einzige Unterschied besteht darin, dass das Paket `rnspure` keine Abhängigkeiten auflistet, die für die Installation erforderlich sind.

Unabhängig davon, wie Reticulum installiert und gestartet wird, lädt es externe Abhängigkeiten nur, wenn sie *benötigt* und *verfügbar* sind. Wenn Sie Reticulum beispielsweise auf einem System verwenden möchten, das [pyserial](https://github.com/pyserial/pyserial) nicht unterstützt, ist es durchaus möglich, das Paket `rnspure` zu verwenden, aber Reticulum kann dann keine seriell basierten Schnittstellen nutzen. Alle anderen verfügbaren Module werden bei Bedarf weiterhin geladen.

**Bitte beachten Sie!** Wenn Sie das Paket `rnspure` verwenden, um Reticulum auf Systemen zu betreiben, die [PyCA/cryptography](https://github.com/pyca/cryptography) nicht unterstützen, ist es wichtig, dass Sie den Abschnitt [Kryptographische Primitiven](crypto_de.html) auf dieser Website lesen und verstehen.

## Leistung
Reticulum zielt auf einen *sehr* großen nutzbaren Leistungsbereich ab, gibt aber der Funktionalität und Leistung Vorrang auf Medien mit geringer Bandbreite. Ziel ist es, einen dynamischen Leistungsbereich von 250 Bit pro Sekunde bis zu 1 Gigabit pro Sekunde auf normaler Hardware bereitzustellen.

Derzeit liegt der nutzbare Leistungsbereich bei etwa 150 Bit pro Sekunde bis 40 Megabit pro Sekunde, wobei schnellere physische Medien nicht gesättigt sind. Eine über das derzeitige Niveau hinausgehende Leistung ist für künftige Upgrades vorgesehen, hat aber keine hohe Priorität, solange das Leitungsformat und die API noch nicht festgelegt sind.

<p align="right"><a href="hardware_de.html">Nächstes Thema: Unterstützte Hardware</a></p>
