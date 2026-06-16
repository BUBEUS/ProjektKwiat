# 🌿 Zdalna Roślinka — Symulacja życia rośliny w Pythonie
# EARLY AI SZPONT

Aplikacja edukacyjna symulująca życie rośliny w czasie rzeczywistym. Zbudowana w Pythonie przy użyciu wzorca MVC i biblioteki Tkinter.

---

## 📌 Wprowadzenie

Projekt **„Roślinka”** to edukacyjna aplikacja desktopowa napisana w języku Python. Celem aplikacji jest umożliwienie użytkownikowi symulowania życia rośliny: podlewania jej, obserwowania zmian warunków środowiskowych (wilgotność, światło, temperatura), a także upływu czasu (godzina, dzień).

Projekt pełni funkcję dydaktyczną, ucząc:

- wzorca projektowego **MVC** (Model-View-Controller),
- projektowania GUI w **Tkinterze**,
- zarządzania stanem aplikacji,
- testowania z użyciem **pytest**,
- generowania dokumentacji za pomocą **Sphinx**.

---

## ⚙️ Wymagania i Instalacja

### Wymagania

- Python **3.10** lub nowszy
- Pakiety:
  - `sphinx`
  - `pytest`
  - `flake8`

### Instalacja

```bash
pip install sphinx pytest flake8
```

### Uruchomienie aplikacji

```bash
python controller.py
```

### Uruchomienie testów jednostkowych

```bash
pytest
```

### Generowanie dokumentacji

```bash
cd docs
make html
start _build/html/index.html
```

---

## 🗂️ Struktura Projektu

Projekt został zorganizowany zgodnie ze wzorcem **MVC**:

```
📁 root/
├── controller.py        # Warstwa pośrednia – logika łączenia modelu i widoku
├── model.py             # Model danych – stan i logika symulacji rośliny
├── view.py              # Warstwa prezentacji – GUI w Tkinterze
├── test_model.py        # Testy jednostkowe dla modelu
└── docs/                # Dokumentacja generowana za pomocą Sphinx
```

---

## 🧠 Zasady Projektowania GUI

GUI aplikacji zostało zaprojektowane w oparciu o zasady z książki **"The Design of Everyday Things" – Don Norman** oraz praktyki użyteczności.

### ✅ Minimalizm i Czytelność

> „Good design means stripping away what is unnecessary so users can focus on what is essential.”  
> — Don Norman

- Interfejs został podzielony na logiczne sekcje z użyciem `LabelFrame`.
- Paski postępu i etykiety są proste, intuicyjne i bez zbędnych dekoracji.

### 📐 Responsywność

- Użyto `grid()` z konfiguracją `rowconfigure()` i `columnconfigure()` dla dynamicznej skalowalności.
- Wszystkie elementy GUI mają `sticky='nsew'`, co pozwala im rozszerzać się wraz z oknem.

### 🖱️ Bezpośrednia Manipulacja

- Przycisk „💧 Podlej Roślinkę” oraz przyciski symulacji czasu pozwalają na intuicyjne sterowanie aplikacją.

### 🔁 Spójność

- Styl elementów GUI jest jednolity.
- Aktualizacja pasków postępu, etykiet i kolorystyki oparta na czasie symulacji.

---

## 🧪 Testowanie i Debugowanie

### Debugowanie

Poprawiono mechanizm symulacji dnia (`simulate_day`) – teraz warunki środowiskowe (np. światło, temperatura) lepiej odzwierciedlają rzeczywistą zmianę pór dnia.

### Statyczna analiza kodu – `flake8`

Naprawione błędy:

- `E501` – zbyt długie linie
- `W291`, `W293` – zbędne spacje i puste linie
- Brak docstringów – uzupełniono

### Testy jednostkowe – `pytest`

Testy w pliku `test_model.py` pokrywają:

- podlewanie rośliny,
- zmianę stanu na skutek symulacji czasu,
- ocenę zdrowia rośliny.

Przykład:

```bash
collected 12 items

test_model.py ............    [100%]

============================ 12 passed in 0.03s =============================
```

---

## 📚 Dokumentacja

Aby wygenerować pełną dokumentację HTML:

```bash
cd docs
make html
start _build/html/index.html
```

Struktura dokumentacji Sphinx zawiera:

- `model.py` – logika stanu rośliny
- `controller.py` – metody sterujące i aktualizujące GUI
- `view.py` – komponenty interfejsu użytkownika

Dostępne indeksy i wyszukiwanie:

- [Genindex](#)
- [Modindex](#)
- [Search](#)

---


## 🖼️ Zrzuty ekranu (opcjonalnie)

![image](https://github.com/user-attachments/assets/0dbdc015-05c3-4be9-93c9-9dbee31623b9)
---
![image](https://github.com/user-attachments/assets/e03e745f-a019-49f1-8385-4c8b4be83c52)
---
![image](https://github.com/user-attachments/assets/6aec41c1-767f-4609-8033-ca9cbc35689f)

---
