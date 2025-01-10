Imię i nazwisko autora: 337258
Stanisław Liszewski

Cel i opis projektu:
Aplikacja stanowiąca pomoc w układaniu planu zajęć w szkole / na uczeli z perspektywy planującego zajęcia dla wielu grup.

Aplikacja terminalowa tworząca bazę danych nauczycieli oraz zajęć przez nich zaplanowanych. Aplikacja umożliwia wyświetlanie znajdujących się w bazie danych nauczycieli oraz ich planów zajęć, dodawanie nowych nauczycieli do bazy danych, dodawanie i usuwanie zajęć do planów nauczycieli, usuwanie nauczycieli z bazy danych, zapisywanie do pliku typu .json listy nauczycieli i ich zajęć z bazy danych oraz wczytywanie z pliku tej listy.

Instrukcja uruchomienia:
1. Zainstalować pakiety dostarczone w ramach pliku `requirements.txt`
2. Uruchomić plik `main.py`

Aby wczytać plik z danymi, należy umieścić odpowiedni plik typu .json w folderze data_files, a następnie wybrać w menu opcję 6. i podać nazwę pliku z danymi. Jeśli format pliku jest niepoprawny, aplikacja o tym poinformuje.
W folderze znajduje się plik sampledata.json z dwoma nauczycielami, z których jeden ma zaplanowanych kilka zajęć. Można wczytać ten plik w menu, aby przetestować działanie programu.

Użytkowanie aplikacji opiera się na nawigacji tekstowego terminala poprzez wpisywanie odpowiednich komend, o które aplikacja będzie prosić. Po dodaniu przynajmniej jednego nauczyciela będzie możliwe "zalogowanie" (wybierając opcję 4 w menu). Z tego poziomu będzie możliwe dodawanie i usuwanie nowych zajęć do planu zalogowanego nauczyciela.

Menu składa się z 7 opcji:
1. Wypisanie listy wszystkich nauczycieli oraz ich planów,
2. Dodanie nowego nauczyciela do bazy danych,
3. Usunięcie istniejącego nauczyciela z bazy danych,
4. Zalogowanie jako istniejący nauczyciel,
5. Zapisanie danych z programu do pliku,
6. Wczytanie danych do programu z pliku,
0. Wyjście.

Menu po zalogowaniu wyświetli się drugie menu, składające się z kolejnych 4 opcji:
1. Wypisanie planu zalogowanego nauczyciela,
2. Dodanie nowego kursu do swojego planu,
3. Usunięcie istniejącego kursu ze swojego planu,
4. Powrót do menu głównego.

Wyświetlanie planu zajęć poszczególnych nauczycieli odbywa się również w terminalu.

Kreator nauczycieli i kursów są intuicyjne, proszą po kolei o wpisywanie odpowiednich danych dotyczących nauczyciela lub kursu oraz informują o błędach, jeśli takowe wystąpią. Przy tworzeniu kursu przez nauczyciela w pewnym momencie wyświetli się jego plan, aby mógł zobaczyć, kiedy ma już zaplanowane zajęcia.
W przypadku próby dodania kursu dla grupy, która ma w danym czasie inne zajęcia (u tego samego lub innego nauczyciela) lub próby dodania kursu odbywającego się w sali, w której w danym czasie odbywają się inne zajęcia, aplikacja poinformuje o wystąpieniu kolizji i nie doda kursu do bazy danych.