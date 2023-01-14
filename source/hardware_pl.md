# Wspierany Hardware
Reticulum może być używane praktycznie przez każde medium, które wspiera przynajmniej kanał półdupleksowy z przepustowością 500 bitów na sekundę, i MTU 500 bitów. Data radio, modemy, radia LoRa, porty szeregowe, AX.25 TNC, tryby cyfrowe radia amatorskiego, WiFi i urządzenia Ethernet, bezprzewodowe łącza optyczne (FSO), i podobne systemy są przykładem rodzajów fizycznych urządzeń, które Reticulum może używać. Wspierane rodzaje interfejsów zawierają:

- Każde urządzenie ethernet
- Prawie wszystkie urządzenia z WiFi
- LoRa używające [RNode](https://unsigned.io/rnode/)
- Packet Radio TNC (z lub bez AX.25)
- Hardware kompatybilny z KISS i modemy programowe
- Każde urządzenie z portem szeregowym
- TCP przez sieci IP
- UDP przez sieci IP
- Zewnętrzne programy przez stdio lub pipes
- Niestandardowy hardware przez stdio lub pipes

Bardziej szczegółowe informacje i pełną listę wspieranych rodzajów interfejsów można znaleźć w rozdziałach poświęconych [sprzętowi komunikacyjnemu](manual/hardware.html) i [wspieranych interfejsów](manual/interfaces.html).

Reticulum może być również umieszczone w istniejących sieciach IP, więc nic nie stoi na przeszkodzie, by używać go w przewodowej sieci ethernet, lokalnej sieci WiFi lub w Internecie, gdzie będzie działał równie dobrze. W rzeczywistości, jedną z mocnych stron Reticulum jest to, jak łatwo pozwala połączyć różne media w samokonfigurującą się, odporną i szyfrowaną sieć, wykorzystując dowolną mieszankę dostępnej infrastruktury.

Przykładowo, możliwe jest skonfigurowanie Raspberry Pi podłączonego zarówno do radia LoRa, TNC packet radio, jak i sieci WiFi. Po skonfigurowaniu interfejsów, Reticulum zajmie się resztą, a każde urządzenie w sieci WiFi może komunikować się z węzłami po stronie sieci LoRa i packet radio, i odwrotnie.

<p align="right"><a href="connect_pl.html">Następny Temat: Publiczny Testnet</a></p>
