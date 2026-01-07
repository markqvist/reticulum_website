# Verbindingen Opbouwen  

Reticulum is geen dienst waarop u zich abonneert, noch een enkel wereldwijd netwerk waar u zich bij aansluit. Het is een *netwerkstack*; een toolkit voor het bouwen van communicatiesystemen die aansluiten bij uw specifieke waarden, vereisten en operationele omgeving. De manier waarop u verbinding maakt met andere Reticulum-peers is volledig uw eigen keuze.  

Wanneer u voor het eerst Reticulum gaat gebruiken, heeft u een manier nodig om verbinding te krijgen met de peers waarmee u wilt communiceren - het proces van *verbinden opbouwen* (bootstrapping connectivity). Zodra u één of meerdere geldige interfacedefinities heeft verkregen, kunt u deze toevoegen aan het gedeelte `[interfaces]` van uw Reticulum-configuratie.  

Deze pagina geeft de meest elementaire overzicht, maar om de flexibiliteit en opties voor het opbouwen van verbindingen volledig te begrijpen, lees de sectie [Bootstrapping Connectivity](manual/gettingstartedfast.html#creating-a-network-with-reticulum) in de handleiding.  

## Verbinding Maken met het Gedistribueerde Backbone  

Een wereldwijd, gedistribueerd backbone van Reticulum Transport Nodes wordt gedraaid door vrijwilligers van over de hele wereld. Dit netwerk bestaat uit een heterogene verzameling van zowel openbare als privé-knooppunten die een ongecoördineerd, vrijwillig inter-netwerkbackbone vormen dat momenteel wereldwijde transport- en inter-netwerkmogelijkheden biedt voor Reticulum.  

Een goede plek om interfacedefinities te vinden voor het opbouwen van verbindingen zijn door de gemeenschap beheerde websites zoals [directory.rns.recipes](https://directory.rns.recipes/) en [rmap.world](https://rmap.world/).  

Reticulum moedigt de aanpak van *organische groei* aan. In plaats van te vertrouwen op permanente statische verbindingen met verre servers, kunt u tijdelijke bootstrap-verbindingen gebruiken om continu relevantere of lokale infrastructuur te *ontdekken*. Zodra deze is ontdekt, kan uw systeem automatisch sterkere, meer directe links vormen met deze peers, en de tijdelijke bootstrap-links discarden. Dit resulteert in een web van verbindingen die geografisch relevant, veerkrachtig en efficiënt zijn.  

## Persoonlijke Infrastructuur Bouwen  

We moedigen iedereen sterk aan, zelfs thuisebruikers, om te denken in termen van het bouwen van **persoonlijke infrastructuur**. Verbind niet elke telefoon, tablet en computer in uw huis direct met een openbare internetgateway. Gebruik in plaats daarvan een oude computer, een Raspberry Pi, of een ondersteunde router om te fungeren als uw eigen, persoonlijke **Transport Node**:  

* Uw lokale Transport Node staat in uw huis, verbonden met uw WiFi en mogelijk een radio-interface (zoals een RNode).  
* U configureert dit knooppunt met een `bootstrap_only` interface (misschien een TCP-tunnel naar een breder netwerk) en schakelt interface-discovery in.  
* Terwijl u slaapt, werkt of kookt, luistert uw knooppunt naar het netwerk. Het ontdekt andere lokale gemeenschapsleden, valideert hun Network Identities, en stelt automatisch directe links op.  
* Uw persoonlijke apparaten verbinden nu met uw *lokale* knooppunt, dat is geïntegreerd in een levende, ademende lokale mesh. Uw verkeer stroomt via lokale paden die door andere echte mensen in de gemeenschap worden geleverd, in plaats van op en neer te stuiteren op een verre server.  

**Wacht niet op anderen om de netwerken te bouwen die u wilt zien**. Elk netwerk is belangrijk, misschien zelfs vooral degenen die individuele families en personen ondersteunen. Zodra er genoeg van deze persoonlijke, lokale infrastructuur bestaat, wordt het onvermijdelijk om deze direct met elkaar te verbinden, zonder gebruik te maken van het openbare Internet.

<p align="right"><a href="docs_nl.html">Volgend onderwerp: lees de handleiding</a></p>
