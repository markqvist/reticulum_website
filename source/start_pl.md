# Jak zacząć
Najlepszy sposób na rozpoczęcie pracy z Reticulum Network Stack zależy od tego, co
co chcesz zrobić. Aby uzyskać pełne szczegóły i przykłady, sprawdź rodział [Jak szybko zacząć](manual/gettingstartedfast.html) w [Podręczniku Reticulum](manual/index.html).

## Instalacja
Najprostszym sposobem, żeby zainstalować Reticulum i powiązane narzędzia jest przy wykorzystanie pip:

```bash
pip install rns
```

Możesz wtedy uruchomić każdy program, który używa Reticulum, lub uruchomić Reticulum jako usługę systemową za pomocą [narzędzia rnsd](manual/using.html#the-rnsd-utility).

Jeśli `pip` nie jest dostępny na twoim systemie, zainstaluj najpierw pakiety `python3` i `python3-pip` dla swojego systemu operacyjnego.

Przy pierwszym uruchomieniu Reticulum tworzy domyślny plik konfiguracyjny, zapewniający podstawową łączność z innymi serwerami Reticulum, które mogą być osiągalne lokalnie. Jeśli któryś z tych lokalnych peerów jest Instancją Transportową, może on połączyć Ciebie z większymi sieciami. Domyślny plik konfiguracyjny zawiera kilka przykładów oraz referencje do tworzenia bardziej złożonych konfiguracji.

W celu uzyskania bardziej szczegółowych przykładów dotyczących rozszerzenia komunikacji za pomocą wielu mediów, takich jak packet radio lub LoRa, porty szeregowe lub za pomocą szybkich łączy IP i Internetu przy użyciu interfejsów UDP i TCP, sprawdź sekcję [Wspierane Interfejsy](manual/interfaces.html) w [Podręczniku Reticulum](manual/index.html).


## Zawarte Narzędzia
Reticulum zawiera szereg przydatnych narzędzi do zarządzania sieciami, przeglądania stanu i informacji oraz innych zadań. You can read more about these programs in the Możesz przeczytać więcej o tych programach w sekcji [Zawarte Programy Użytkowe](manual/using.html#included-utility-programs) w [Podręczniku Reticulum](manual/index.html).

- Demon systemowy `rnsd` do uruchamiania Reticulum jako zawsze dostępnej usługi
- Narzędzie statusu interfejsu o nazwie `rnstatus`, które wyświetla informacje o interfejsach
- Narzędzie do wyszukiwania i zarządzania ścieżkami `rnpath` pozwalające na przeglądanie i modyfikowanie tablic ścieżek
- Narzędzie diagnostyczne o nazwie `rnprobe` do sprawdzania łączności z miejscami docelowymi
- Prosty program do transferu plików o nazwie `rncp` ułatwiający kopiowanie plików na zdalne systemy
- Program do zdalnego wykonywania poleceń `rnx`, który pozwala uruchamiać polecenia i programy oraz pobierać dane wyjściowe ze zdalnych systemów

Wszystkie narzędzia, w tym `rnx` i `rncp`, działają niezawodnie i dobrze nawet na łączach o bardzo niskiej przepustowości, takich jak LoRa czy Packet Radio.

## Programy Używające Reticulum
Jeśli chcesz szybko zorientować się, co potrafi Reticulum, zapoznaj się z poniższymi materiałami.

- Dla pozasieciowej, szyfrowanej i odpornej platformy komunikacyjnej typu mesh, zobacz [Nomad Network](https://github.com/markqvist/NomadNet)
- Aplikacja [Sideband](https://github.com/markqvist/sideband) na Androida, Linuxa i macOS posiada interfejs graficzny i koncentruje się na łatwości użytkowania.
- [LXMF](https://github.com/markqvist/lxmf) jest rozproszonym, odpornym na opóźnienia i zakłócenia protokołem wysyłania wiadomości zbudowanym na Reticulum

## Zależności
Instalacja domyślnego pakietu `rns` wymaga zależności wymienionych poniżej. Prawie wszystkie systemy i dystrybucje mają łatwo dostępne pakiety dla tych zależności, a kiedy pakiet `rns` jest instalowany z `pip`, zostaną one pobrane i zainstalowane również.

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

Na bardziej nietypowych systemach, w niektórych rzadkich przypadkach, może nie być możliwe zainstalowanie lub nawet skompilowanie jednego lub więcej z powyższych modułów. W takich sytuacjach można użyć pakietu `rnspure`, który nie wymaga zewnętrznych zależności do instalacji. Proszę zauważyć, że zawartość pakietów `rns` i `rnspure` jest *identyczna*. Jedyną różnicą jest to, że pakiet `rnspure` nie zawiera żadnych zależności wymaganych do instalacji.

Bez względu na to, jak Reticulum jest zainstalowane i uruchomione, załaduje zewnętrzne zależności tylko wtedy, gdy są one *potrzebne* i *dostępne*. Jeśli na przykład chcesz używać Reticulum na systemie, który nie może obsługiwać [pyserial](https://github.com/pyserial/pyserial), jest to całkowicie możliwe przy użyciu pakietu rnspure, ale Reticulum nie będzie w stanie korzystać z interfejsów opartych na portach szeregowych. Wszystkie inne dostępne moduły będą nadal ładowane w razie potrzeby.

**Uwaga!** Jeśli używasz pakietu rnspure do uruchomienia Reticulum na systemach, które nie wspierają [PyCA/cryptography](https://github.com/pyca/cryptography), ważne jest, abyś przeczytał i zrozumiał sekcję [Prymitywy Kryptograficzne](crypto.html) na tej stronie.

## Wydajność
Reticulum celuje w *bardzo* szeroki zakres wydajności użytkowej, ale priorytetowo traktuje funkcjonalność i wydajność w stosunku do mediów o niskiej przepustowości. Celem jest zapewnienie dynamicznej wydajności od 250 bitów na sekundę do 1 gigabita na sekundę na normalnym sprzęcie.

Obecnie użyteczna wydajność wynosi około 150 bitów na sekundę do 40 megabitów na sekundę, z nośnikami fizycznymi szybszymi niż te które nie są nienasycone. Wydajność wykraczająca poza obecny poziom jest przeznaczona do przyszłych aktualizacji, ale nie ma wysokiego priorytetu do czasu zablokowania formatu przewodów i API.

<p align="right"><a href="hardware_pl.html">Następny Temat: Wspierany Hardware</a></p>
