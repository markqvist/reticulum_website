# Verbindungsaufbau initialisieren  
  
Reticulum ist kein Dienst, den Sie abonnieren, und auch kein einzelnes globales Netzwerk, dem Sie „beitreten“. Es ist ein *Netzwerk-Stack*; ein Werkzeugkasten für den Aufbau von Kommunikationssystemen, die mit Ihren spezifischen Werten, Anforderungen und Ihrem Betriebsumfeld übereinstimmen. Die Art und Weise, wie Sie sich mit anderen Reticulum-Peers verbinden, liegt ganz in Ihrer Hand.  
  
Wenn Sie Reticulum erstmals verwenden, benötigen Sie eine Möglichkeit, Konnektivität zu den Peers herzustellen, mit denen Sie kommunizieren möchten – der Prozess des *initialen Verbindungsaufbaus*. Sobald Sie eine oder mehrere gültige Schnittstellendefinitionen erhalten haben, können Sie diese zum Abschnitt `[interfaces]` Ihrer Reticulum-Konfiguration hinzufügen.  
  
Diese Seite bietet die grundlegendste Übersicht, aber um die Flexibilität und Optionen für den initialen Verbindungsaufbau vollständig zu verstehen, lesen Sie den Abschnitt [Bootstrapping Connectivity](manual/gettingstartedfast.html#creating-a-network-with-reticulum) im Handbuch.  
  
## Mit dem verteilten Backbone verbinden  
  
Ein globaler, verteilter Backbone aus Reticulum-Transportknoten wird von Freiwilligen aus der ganzen Welt betrieben. Dieses Netzwerk bildet eine heterogene Sammlung sowohl öffentlicher als auch privater Knoten, die einen unkoordinierten, freiwilligen Internetworking-Backbone bilden, der derzeit globale Transport- und Internetworking-Funktionen für Reticulum bereitstellt.  
  
Ein guter Ort, um Schnittstellendefinitionen für den initialen Verbindungsaufbau zu finden, sind von der Community betriebene Websites wie [directory.rns.recipes](https://directory.rns.recipes/) und [rmap.world](https://rmap.world/).  
  
Reticulum fördert den Ansatz des *organischen Wachstums*. Anstatt sich auf permanente statische Verbindungen zu entfernten Servern zu verlassen, können Sie temporäre Bootstrap-Verbindungen verwenden, um kontinuierlich relevantere oder lokale Infrastruktur zu *entdecken*. Sobald entdeckt, kann Ihr System automatisch stärkere, direktere Verbindungen zu diesen Peers herstellen und die temporären Bootstrap-Verbindungen verwerfen. Dies führt zu einem Geflecht von Verbindungen, die geografisch relevant, resilient und effizient sind.  
  
## Persönliche Infrastruktur aufbauen  
  
Wir ermutigen alle, sogar Heimanwender, dazu, in Kategorien des Aufbaus von **persönlicher Infrastruktur** zu denken. Verbinden Sie nicht jedes Telefon, Tablet und jeden Computer in Ihrem Haushalt direkt mit einem öffentlichen Internet-Gateway. Nutzen Sie stattdessen einen alten Computer, einen Raspberry Pi oder einen unterstützten Router, um als Ihr eigener, persönlicher **Transportknoten** zu fungieren:  
  
* Ihr lokaler Transportknoten befindet sich in Ihrem Zuhause, mit Ihrem WiFi und möglicherweise einer Funkschnittstelle (wie einem RNode) verbunden.  
* Sie konfigurieren diesen Knoten mit einer `bootstrap_only`-Schnittstelle (vielleicht einen TCP-Tunnel zu einem größeren Netzwerk) und aktivieren die Schnittstellenentdeckung.  
* Während Sie schlafen, arbeiten oder kochen, lauscht Ihr Knoten dem Netzwerk. Er entdeckt andere lokale Community-Mitglieder, validiert deren Netzwerkidentitäten und stellt automatisch direkte Verbindungen her.  
* Ihre persönlichen Geräte verbinden sich nun mit Ihrem *lokalen* Knoten, der in ein lebendiges, atmendes lokales Mesh integriert ist. Ihr Verkehr fließt über lokale Pfade, die von anderen echten Personen in der Community bereitgestellt werden, anstatt an einem entfernten Server abzuprallen.  
  
**Warten Sie nicht darauf, dass andere die Netzwerke aufbauen, die Sie sehen möchten**. Jedes Netzwerk ist wichtig, vielleicht sogar am meisten jene, die einzelne Familien und Personen unterstützen. Sobald genug dieser persönlichen, lokalen Infrastruktur existiert, wird es unvermeidlich, diese direkt miteinander zu verbinden, ohne das öffentliche Internet zu durchqueren.

<p align="right"><a href="docs_de.html">Nächstes Thema: Lesen Sie das Handbuch</a></p>
