# Hardware soportado
Reticulum puede utilizarse en prácticamente cualquier medio que admita al menos un canal semidúplex con un rendimiento de 500 bits por segundo y una MTU de 500 bytes. Radios de datos, módems, radios LoRa, líneas seriales, TNC AX.25, modos digitales de radioaficionados, dispositivos WiFi y Ethernet, enlaces ópticos de espacio libre y sistemas similares son ejemplos de los tipos de dispositivos físicos que puede utilizar Reticulum. Los tipos de interfaz admitidos incluyen:

- Cualquier dispositivo Ethernet
- Casi todo el hardware basado en WiFi
- LoRa utilizando [RNode](https://unsigned.io/rnode/)
- TNCs de Radio en paquetes (con o sin AX.25)
- Módems de hardware y software compatibles con KISS
- Cualquier dispositivo con puerto serial
- TCP sobre redes IP
- UDP sobre redes IP
- Programas externos a través de stdio o pipes
- Hardware personalizado a través de stdio o pipes

Para obtener información más detallada y una lista completa de los tipos de interfaz compatibles, lea los capítulos [Hardware de comunicaciones](manual/hardware.html) e [Interfaces compatibles](manual/interfaces.html) del manual.

Reticulum también puede encapsularse sobre redes IP existentes, por lo que nada le impide utilizarlo a través de Ethernet por cable, su red WiFi local o Internet, donde funcionará igual de bien. De hecho, uno de los puntos fuertes de Reticulum es la facilidad con la que permite conectar diferentes medios en una malla autoconfigurable, resistente y encriptada, utilizando cualquier mezcla de infraestructura disponible.

Como ejemplo, se puede setear una Raspberry Pi conectada a un dispositivo LoRa, una radio en paquetes TNC y una red WiFi. Cuando las interfaces esten configuradas, Reticulum se hace cargo del resto, y cualquier dispositivo en la red se va a poder comunitar con nodos en los lados de LoRa y radio en paquetes de la red y viceversa.

<p align="right"><a href="connect_es.html">Siguiente tema: Testnet publica</a></p>
