.. DokumentacjaSphinx documentation master file, created by
   sphinx-quickstart on Fri May 30 15:36:54 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DokumentacjaSphinx documentation
================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


1. Wprowadzenie
---------------

Projekt „Roślinka” to edukacyjna aplikacja desktopowa napisana w języku Python, której celem jest symulacja życia rośliny. 
Użytkownik może podlewać roślinę, obserwować zmiany jej parametrów (wilgotność, nasłonecznienie, temperatura) oraz 
symulować upływ czasu (godzina, dzień). Celem projektu jest nauka podstaw wzorca MVC, obsługi GUI w Tkinterze, 
zarządzania stanem aplikacji oraz testowania i dokumentowania kodu.

2. Instalacja i uruchomienie
----------------------------

- Python 3.10 lub nowszy
- Pakiety: `sphinx`, `pytest`

Instalacja zależności:

.. code-block:: bash

   pip install sphinx pytest

.. code-block:: bash

   pip install flake8

Uruchomienie aplikacji:

.. code-block:: bash

   python controller.py

Uruchomienie testów jednostkowych (z katalogu głównego projektu):

.. code-block:: bash

   pytest

Generowanie dokumentacji:

.. code-block:: bash

   cd docs
   make html
   start _build/html/index.html

3. Struktura kodu
------------------

Projekt podzielony jest zgodnie ze wzorcem MVC (Model-View-Controller):

- **model.py**  logika i stan rośliny (wilgotność, temperatura, światło, godzina).
- **view.py**  interfejs graficzny zbudowany w Tkinterze.
- **controller.py**  pośrednik łączący widok i model.
- **test_model.py**  zestaw testów jednostkowych modelu.
- **docs/**  dokumentacja projektu generowana przez Sphinx.

4. Opis wprowadzonych zmian w GUI oraz zastosowane zasady projektowania interfejsów
-------------------------------

Interfejs został zmodyfikowany głównie o zasadę: 

**Zasada Czytelności i Minimalizmu**, opartą na "The Design of Everyday Things" (2013) autorstwa Don Norman, a dokładnie rozdziałach "The Psychology of Everyday Actions" oraz "The Design Challenge".

.. quote::

   “Good design is actually a lot harder to achieve than just making things look fancy or complicated.
    It means stripping away what is unnecessary so that users can focus on what is essential.”

   — Donald Norman, *The Design of Everyday Things*

Interfejs został podzielony na czytelne sekcje, dzięki wykorzystaniu grupujących ramek (LabelFrame) oraz prostych, intuicyjnych elementów takich jak przyciski i paski postępu. Minimalistyczne podejście eliminuje zbędne elementy, przez co użytkownik szybko odnajduje potrzebne informacje i akcje.

W trakcie tworzenia i usprawniania interfejsu graficznego aplikacji zostały także uwzględnione i zaimplementowane następujące zasady projektowania GUI, mające na celu poprawę użyteczności i doświadczenia użytkownika:

A - **Zasada Responsywności i Skalowalności**

Interfejs został zaprojektowany tak, aby dynamicznie dostosowywał się do zmiany rozmiaru okna aplikacji. Dzięki odpowiedniemu wykorzystaniu mechanizmu rozmieszczania widgetów (grid oraz pack z konfiguracją rozciągania) poszczególne elementy interfejsu (np. paski postępu, przyciski, ramki) skalują się i przesuwają proporcjonalnie, co zapobiega utracie czytelności i zapewnia komfort użytkowania na różnych rozmiarach okna.

B - **Zasada Bezpośredniej Manipulacji (Direct Manipulation)**

Aplikacja umożliwia użytkownikowi łatwą i bezpośrednią interakcję z modelem rośliny przez przyciski służące do podlewania oraz symulacji czasu (godzina/dzień). Takie bezpośrednie działanie pozwala na intuicyjne sterowanie stanem rośliny i natychmiastową obserwację efektów.

C - **Zasada Spójności (Consistency)**

Elementy interfejsu są spójne pod względem wyglądu i zachowania — np. wszystkie przyciski mają jednolity styl, a paski postępu stosują te same kolory i mechanizmy aktualizacji. Spójność poprawia naukę obsługi aplikacji i redukuje ryzyko błędów użytkownika.

-------------------------------
-------------------------------
Zmodyfikowano interfejs graficzny, aby był **responsywny** przy zmianie rozmiaru okna. 
W tym celu zastosowano następujące zasady projektowania interfejsów:

- **Grid layout** z odpowiednimi atrybutami `.rowconfigure()` i `.columnconfigure()`, aby elementy mogły się automatycznie skalować.
- Użycie opcji `sticky='nsew'` dla wszystkich kontrolek, dzięki czemu rozciągają się wraz z rozmiarem okna.
- Zastosowano **czytelne etykiety**, paski postępu i zmienne dynamicznie odświeżane przez kontroler.
- Zachowano **czytelność i prostotę**, zgodnie z zasadą minimalizmu w GUI.

Dzięki tym zmianom interfejs automatycznie dostosowuje się do rozmiaru okna użytkownika.

5. Proces debugowania i naprawy błędów
--------------------------------------

Poprawa działania kodu w przypadku "przewijania" dnia poprzez dodanie nowej metody **model.simulate_day**, by nasłonecznienie oraz temperatura było bardziej adekwatne do obecnej godziny.

Do statycznej analizy kodu wykorzystano narzędzie:

- **Flake8**

Typowe błędy wykryte i naprawione:

- **E501** – zbyt długie linie (ponad 79 znaków).
- **W291/W293** – zbędne spacje końcowe i puste linie.
- Nieczytelne komentarze oraz brak docstringów – uzupełniono.

Użycie `pytest` pozwoliło stworzyć zestaw **testów jednostkowych** w pliku `test_model.py`, który pokrywa najważniejsze przypadki w module logiki (`model.py`), np. podlewanie, symulacja czasu, poprawność statusu zdrowia rośliny.

.. code-block:: console

   collected 12 items

   test_model.py ............                                                                                       [100%]

   ================================================= 12 passed in 0.03s ==================================================



Spis treści modułów
-------------------

.. toctree::
   :maxdepth: 2
   :caption: Moduły:

   model
   view
   controller

Indeksy i wyszukiwanie
----------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
