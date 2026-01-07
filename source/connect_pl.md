
# Inicjalizacja łączności

Reticulum nie jest usługą, do której subskrybujesz, ani jedną globalną siecią, do której się "dołączasz". Jest to *stos sieciowy*; zestaw narzędzi do budowania systemów komunikacyjnych, które są zgodne z Twoimi konkretnymi wartościami, wymaganiami i środowiskiem operacyjnym. Sposób, w jaki wybierzesz połączenie z innymi węzłami równorzędnymi Reticulum, zależy wyłącznie od Ciebie.

Kiedy zaczniesz używać Reticulum, będziesz potrzebować sposobu na uzyskanie łączności z węzłami równorzędnymi, z którymi chcesz się komunikować – to proces *inicjalizacji łączności*. Gdy uzyskasz jedną lub więcej poprawnych definicji interfejsów, możesz dodać je do sekcji `[interfaces]` w konfiguracji Reticulum.

Ta strona przedstawia najbardziej podstawowy przegląd, ale aby w pełni zrozumieć elastyczność i opcje dostępne dla inicjalizacji łączności, przeczytaj sekcję [Inicjalizacja łączności](manual/gettingstartedfast.html#creating-a-network-with-reticulum) w podręczniku.

## Połącz się z rozproszoną siecią szkieletową

Globalna, rozproszona sieć szkieletowa Węzłów Transportowych Reticulum jest obsługiwana przez wolontariuszy z całego świata. Ta sieć stanowi heterogeniczną kolekcję węzłów publicznych i prywatnych, które tworzą nieskoordynowaną, dobrowolną sieć szkieletową między sieciami, która obecnie zapewnia globalne możliwości transportu i internetworkingu dla Reticulum.

Dobrym miejscem do znalezienia definicji interfejsów dla inicjalizacji łączności są strony internetowe prowadzone przez społeczność, takie jak [directory.rns.recipes](https://directory.rns.recipes/) i [rmap.world](https://rmap.world/).

Reticulum promuje podejście *organicznego wzrostu*. Zamiast polegać na trwałych, statycznych połączeniach z odległymi serwerami, możesz używać tymczasowych połączeń inicjalizujących do ciągłego *odkrywania* bardziej odpowiedniej lub lokalnej infrastruktury. Po odkryciu Twój system może automatycznie tworzyć silniejsze, bardziej bezpośrednie połączenia z tymi węzłami równorzędnymi i porzucać tymczasowe połączenia inicjalizujące. Skutkuje to siecią połączeń, które są geograficznie trafne, odporne i wydajne.

## Zbuduj infrastrukturę osobistą

Gorąco zachęcamy każdego, nawet użytkowników domowych, do myślenia w kategoriach budowania **infrastruktury osobistej**. Nie podłączaj każdego telefonu, tabletu i komputera w swoim domu bezpośrednio do publicznej bramy internetowej. Zamiast tego zaadaptuj stary komputer, Raspberry Pi lub obsługiwany router, aby działał jako Twój własny, osobisty **Węzeł Transportowy**:

* Twój lokalny Węzeł Transportowy znajduje się w Twoim domu, podłączony do Twojej sieci WiFi i być może interfejsu radiowego (jak RNode).
* Konfigurujesz ten węzeł z interfejsem `bootstrap_only` (być może tunelem TCP do szerszej sieci) i włączasz wykrywanie interfejsów.
* Gdy śpisz, pracujesz lub gotujesz, Twój węzeł nasłuchuje sieci. Odkrywa innych członków lokalnej społeczności, weryfikuje ich Tożsamości Sieciowe i automatycznie ustanawia bezpośrednie połączenia.
* Twoje urządzenia osobiste łączą się teraz z Twoim *lokalnym* węzłem, który jest zintegrowany z żywą, pulsującą lokalną siecią typu mesh. Twój ruch przepływa przez lokalne ścieżki udostępniane przez inne prawdziwe osoby w społeczności, zamiast odbijać się od odległego serwera.

**Nie czekaj, aż inni zbudują sieci, które chcesz zobaczyć**. Każda sieć jest ważna, być może przede wszystkim te, które wspierają poszczególne rodziny i osoby. Gdy istnieje wystarczająco dużo tej osobistej, lokalnej infrastruktury, łączenie ich bezpośrednio ze sobą, bez przechodzenia przez publiczny Internet, staje się nieuniknione.

<p align="right"><a href="docs_pl.html">Następny Temat: Przeczytaj Podręcznik</a></p>
