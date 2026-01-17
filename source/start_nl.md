# Begin
De beste manier om aan de slag te gaan met de Reticulum Network Stack hangt af van wat jij wilt doen. Voor volledige details en voorbeelden, kijk eens naar de sectie [Snel aan de slag](manual/gettingstartedfast.html) van de [Reticulum Manual](manual/index.html).

## Installatie
Om Reticulum en gerelateerde hulpprogramma's op uw systeem te installeren, is de eenvoudigste manier via pip:

``` bash
pip install rns
```

U kunt vervolgens elk programma starten dat Reticulum gebruikt, of Reticulum starten als een systeemservice met [het rnsd-hulpprogramma] (manual/using.html#the-rnsd-utility).

Als `pip` niet beschikbaar is op uw systeem, installeer dan eerst de pakketten `python3` en `python3-pip` voor uw besturingssysteem.

Wanneer Reticulum voor het eerst wordt gestart, zal het een standaardconfiguratiebestand maken, dat basisconnectiviteit biedt met andere Reticulum-peers die mogelijk lokaal bereikbaar zijn. Als een van deze lokale peers een Transport Instantie is, kunnen deze u verbinden met bredere netwerken. Het standaardconfiguratiebestand bevat enkele voorbeelden en referenties voor het maken van een complexere configuratie.

Voor meer gedetailleerde voorbeelden over hoe u de communicatie kunt uitbreiden via vele media, zoals packet radio of LoRa, seriële poorten, of via snelle IP-verbindingen en internet met behulp van de UDP- en TCP-interfaces, kunt u de [Ondersteunde interfaces] (handleiding/interfaces) raadplegen. .html) sectie van de [Reticulum Manual](manual/index.html).


## Inbegrepen hulpprogramma's
Reticulum bevat een reeks handige hulpprogramma's voor het beheren van uw netwerken, het bekijken van status en informatie en andere taken. U kunt meer over deze programma's lezen in het hoofdstuk [Included Utility Programs](manual/using.html#included-utility-programs) van de [Reticulum Manual](manual/index.html).

- De systeemdaemon `rnsd` voor het uitvoeren van Reticulum als een altijd beschikbare service
- Een interfacestatushulpprogramma genaamd `rnstatus`, dat informatie over interfaces weergeeft
- Het hulpmiddel voor het opzoeken en beheren van paden `rnpath` waarmee u padtabellen kunt bekijken en wijzigen
- Een diagnostisch hulpmiddel genaamd `rnprobe` voor het controleren van de connectiviteit met bestemmingen
- Een eenvoudig programma voor bestandsoverdracht genaamd `rncp`, waarmee u eenvoudig bestanden naar externe systemen kunt kopiëren
- Het programma voor het uitvoeren van opdrachten op afstand `rnx` waarmee u opdrachten en programma's kunt uitvoeren en uitvoer van externe systemen kunt ophalen

Alle tools, inclusief `rnx` en `rncp`, werken betrouwbaar en goed, zelfs via verbindingen met een zeer lage bandbreedte, zoals LoRa of Packet Radio.

## Programma's die Reticulum gebruiken
Als je snel een idee wilt krijgen van wat Reticulum kan doen, bekijk dan de volgende bronnen.

- Voor een off-grid, gecodeerd en veerkrachtig mesh-communicatieplatform, zie [Nomad Network](https://github.com/markqvist/NomadNet)
- De Android-, Linux- en macOS-app [Sideband](https://github.com/markqvist/sideband) heeft een grafische interface en is gericht op gebruiksgemak.
- [LXMF](https://github.com/markqvist/lxmf) is een gedistribueerd, vertragings- en verstoringstolerant protocol voor berichtoverdracht, gebouwd op Reticulum

## Afhankelijkheden
Voor de installatie van het standaard `rns`-pakket zijn de onderstaande afhankelijkheden vereist. Bijna alle systemen en distributies hebben pakketten beschikbaar voor deze afhankelijkheden, en wanneer het `rns`-pakket met `pip` wordt geïnstalleerd, zullen deze ook worden gedownload en geïnstalleerd.

- [PyCA/cryptografie](https://github.com/pyca/cryptografie)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

Op meer ongebruikelijke systemen, en in sommige zeldzame gevallen, is het misschien niet mogelijk om een of meer van de bovenstaande modules te installeren of zelfs te compileren. In dergelijke situaties kunt u in plaats daarvan het pakket `rnspure` gebruiken, waarvoor geen externe afhankelijkheden nodig zijn voor de installatie. Houd er rekening mee dat de inhoud van de pakketten `rns` en `rnspure` *identiek* is. Het enige verschil is dat het `rnspure`-pakket geen afhankelijkheden vermeldt die vereist zijn voor de installatie.

Ongeacht hoe Reticulum is geïnstalleerd en gestart, het zal alleen externe afhankelijkheden laden als deze *nodig* en *beschikbaar* zijn. Als u bijvoorbeeld Reticulum wilt gebruiken op een systeem dat [pyserial](https://github.com/pyserial/pyserial) niet kan ondersteunen, is het perfect mogelijk om dit te doen met het `rnspure`-pakket, maar Reticulum zal dan niet in staat zijn om seriële interfaces te gebruiken. Alle andere beschikbare modules worden nog steeds geladen wanneer dat nodig is.

**Let op!** Als u het `rnspure`-pakket gebruikt om Reticulum uit te voeren op systemen die [PyCA/cryptography](https://github.com/pyca/cryptography) niet ondersteunen, is het belangrijk dat u eerst het [Cryptografische Primitieven](crypto_nl.html) hoofdstuk van deze site leest en begrijpt.

## Prestatie
Reticulum streeft naar een *zeer* breed bruikbaar prestatiebereik, maar geeft prioriteit aan functionaliteit en prestaties boven mediums met een lage bandbreedte. Het doel is om een dynamisch prestatiebereik te bieden van 250 bits per seconde tot 1 gigabit per seconde op normale hardware.

Momenteel bedraagt het bruikbare prestatiebereik ongeveer 150 bits per seconde tot 1200 megabits per seconde, waarbij fysieke media sneller dan dat niet verzadigd zijn. Prestaties boven het huidige niveau zijn bedoeld voor toekomstige upgrades, maar krijgen geen hoge prioriteit totdat het draadformaat en de API zijn vergrendeld.

<p align="right"><a href="hardware_nl.html">Volgend onderwerp: ondersteunde hardware</a></p>
