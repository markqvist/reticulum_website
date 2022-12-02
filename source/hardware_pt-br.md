# Hardware Compátivel
Reticulum pode ser usado sobre praticamente qualquer dispositivo que suporte pelo menos um canal half-duplex com 500 bits por segundo de taxa de transferência, um MTU de 500 bytes. Rádios de dados, roteadores, rádios LoRa, linhas seriais, AX.25 TNCs, modos de rádio digital amador, Wi-Fi, Bluetooth, links ópticos de espaço-livre e sistemas similares são todos exemplos dos tipos de dispositivos físicos que o Reticulum pode utilizar. Os tipos de interface suportados incluem:

- Qualquer dispositivo Ethernet
- Praticamente todo hardware com Wi-Fi
- LoRa utilizando [RNode](https://unsigned.io/projects/rnode/)
- Hardware/roteadores de software com filosofia KISS
- Qualquer dispositivo com uma porta serial
- TCP sobre redes IP
- UDP sobre redes IP
- Programas externos via stdio ou pipes
- Hardware personalizado via stdio ou pipes

Para informações detalhadas e uma lista completa de todos os tipos de interfaces suportadas, leia o [Hardware de Comunicações](https://reticulum.network/manual/hardware.html) e o capítulo de [Interfaces Suportadas](https://reticulum.network/manual/interfaces.html) do manual.

Reticulum pode ser utilizado sobre redes IP, nada lhe impede de utilizar via cabo Ethernet, sua rede local de Wi-Fi ou a Internet, onde ele funciona corretamente. Na verdade, um dos pontos fortes do Reticulum é como ele facilmente permite que você se conecte a diferentes dispositivos com mesh auto-configurável, resiliente e criptografada, utilizando apenas a infraestrutura disponível.

Como um exemplo, é possível utilizar um Raspberry Pi conectado em ambos, uma rádio LoRa, um rádio amador TNC e uma rede Wi-Fi. Uma vez que as interfaces estejam configuradas, Reticulum cuida do resto, e qualquer dispositivo na rede Wi-Fi pode se comunicar com nós do rádio LoRa e rádio amador, e vice-versa.

<p align="right"><a href="connect_pt-br.html">Próxima Página: Rede de Teste Pública</a></p>
