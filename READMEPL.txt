READMEPL BodyTracking

Program został stworzony przez Jana Kamińskigo (https://github.com/jkaminski677) w ramach projektu PBL na studiach. Celem programu analiza ruchów człowieka podczas wystąpień przed kamerą. Program bada i zapisuje przemieszczanie się konkretnych części ciała człowieka. Aktualnie ustawione są tylko dłonie, środek barek, środek bioder, środek ciała (okolice serca). Aby zmienić badane części ciała należy to zrobić z poziomu kodu źródłowego.

Aby zainstalować program należy rozpakować folder nadrzędny z formatu .zip oraz otworzyć plik wykonywalny w formacie .exe.

Jeśli po uruchomieniu programu pojawi się problem z biblioteką vcruntime140.dll to należy wykonać następujące kroki.
Należy rozpakować plik vcruntime140__.zip (w zależności od architektury systemu w komputerze albo wersję 32 bit albo 64 bit).
Kopiujemy plik do odpowiednich folderów:
32 - bitowy windows:
   32 - bitowy plik do C:/Windows/System32
64 - bitowy windows:
   32 - bitowy plik do C:/Windows/System32
   oraz (jeśli jest taki folder)
   64 - bitowy plik do C:/Windows/System64 lub SysWOW64


Po uruchomieniu programu należy czekać, aż na czarnym ekranie pojawi się powitanie. Jeśli dłuższą chwilę nic się nie dzieje, można nacisnąć jakieś litery na klawiaturze, czasem to pomaga. Kiedy wyświetli się powitanie należy wybrać źródło obrazu do analizowania - albo film z kamerki internetowej lub kamery podłączonej przez USB albo film zapisany w pamięci komputera co jest zalecane, ponieważ program analizując film na żywo zapisuje tylko obraz, bez dźwięku, co więcej nie ma możliwości zapisu w jednej prędkości, dlatego możliwe są przyspieszenia lub opóźnienia w nagraniu. Po wyborze źródła oraz lokalizacji filmu w pamięci komputera należy wybrać folder w którym zostaną zapisane wszystkie dane i wykresy. Następnie należy wybrać jedną klatkę z analizowanego filmu, która będzie tłem na wykresach z analizą ruchu w osi x oraz y. Należy wybrać moment, w którym jest dobrze widoczny prezenter. Filmy analizowane są z prędkością około 26 klatek na sekundę, więc łatwo policzyć wybrany moment. Następnie należy wybrać czy chce się wydobyć odpowiednie fragmenty z całego zbioru danych, np. wybranych momentów, które nas najbardziej interesują. Można wybrać niezliczoną ilość takich fragmentów, lecz należy uważać aby czas początkowy był wcześniejszy niż czas końcowy, ponieważ może się wysypać program. Do każdego wyciętego fragmentu należy wybrać gęstość danych podawanych na osi x (czyli czasu), ponieważ gdy film trwa np. 5 minut to na osi x nie będzie nic widać ze względu na ilość danych. Przykłady wartości gęstości: 80 - 19pom/min, 60 - 25pom/min, 40 - 37pom/min, 35 - 42pom/min, 80 - 5pom/15sek, 60 - 7pom/15sek, 40 - 10pom/15sek, 20 - 19pom/15sek . Po wyborze gęstości fragmentów należy wybrać gęstość pliku z danymi z całego filmu. Tu zaleca się duże wartości. Na końcu można wybrać możliwość analizy kolejnego filmu, lub zamknięcia programu.


Licencja programu obejmuje:
 - wykorzystywanie programu tylko i wyłącznie do rozwijania oraz realizowania projektu pbl "Opracowanie stanowiska do podnoszenia kompetencji komunikacyjnych z wykorzystaniem nowoczesnych rozwiązań audiowizualnych".

Projekt jest w trakcie rozwijania, możliwe że w najbliższej przyszłości pojawi się nowa wersja.