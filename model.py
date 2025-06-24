import random


class PlantModel:
    """Model roślinki, który przechowuje jej stan i logikę."""

    def __init__(self):
        """Inicjalizuje stan roślinki."""
        self._moisture = 50
        self._light = 60
        self._temperature = 22
        self._time_of_day = 12
        self._message = "Witaj, roślinko!"
        self._health_status = "Dobry"

    # --- Gettery ---

    def get_moisture(self) -> int:
        return self._moisture

    def get_light(self) -> int:
        return self._light

    def get_temperature(self) -> int:
        return self._temperature

    def get_time_of_day(self) -> int:
        return self._time_of_day

    def get_message(self) -> str:
        return self._message

    def get_health_status(self) -> str:
        return self._health_status

    # --- Akcje ---

    def water(self) -> None:
        """Podlewa roślinkę i aktualizuje jej stan."""
        self._moisture = 70 + random.randint(-5, 5)
        self._moisture = min(max(self._moisture, 0), 100)
        self._message = "Podlano!"
        self._update_health()

    def simulate_time(self, hours: int = 1) -> None:
        """Symuluje upływ czasu o zadaną liczbę godzin."""
       
        self._moisture -= int(5 + random.random() * 2)
        self._moisture = min(max(self._moisture, 0), 100)

        self._time_of_day = (self._time_of_day + 1) % 24

        if 6 <= self._time_of_day < 18:
            self._light = min(100, self._light + int(5 + random.random() * 5))
            self._temperature = min(40, self._temperature + int(0.5 + random.random()))
            if random.random() < 0.1:
                self._light -= random.randint(5, 15)
        else:
            self._light = max(0, self._light - int(10 + random.random() * 5))
            self._temperature = max(0, self._temperature - int(0.5 + random.random()))
            if random.random() < 0.1:
                self._temperature += random.randint(1, 3)

        self._light = min(max(self._light, 0), 100)
        self._temperature = min(max(self._temperature, 0), 40)

        self._message = f"Minęło {hours} godzin. Aktualny czas: {int(self._time_of_day):02d}:00"
        self._update_health()

    def simulate_day(self) -> None:
        """Symuluje 24 godziny w oparciu o zależne od pory dnia warunki pogodowe."""
        for _ in range(24): 
            self._moisture -= int(5 + random.random() * 2)     
        
        self._moisture = min(max(self._moisture, 0), 100)    
        self._time_of_day = (self._time_of_day + 1) % 24

        hour = self._time_of_day

        # Zależne od pory dnia światło
        if 5 <= hour <= 7:
            self._light = random.randint(0, 30)
        elif 7 < hour <= 10:
            self._light = random.randint(30, 55)
        elif 11 <= hour <= 15:
            self._light = random.randint(45, 100)
        elif 16 <= hour <= 20:
            self._light = random.randint(50, 75)
        else:
            self._light = random.randint(0, 10)

            # Temperatura uzależniona od światła (w skali 15–30°C)
        self._temperature = int(15 + (self._light / 100) * 15)

        self._message = f"Zasymulowano cały dzień. Aktualny czas: {int(self._time_of_day):02d}:00"
        self._update_health()

    # --- Pomocnicze ---

    def _update_health(self) -> None:
        """Aktualizuje status zdrowia roślinki."""
        if self._moisture < 20:
            self._health_status = "Potrzebuje wody!"
        elif self._light < 30:
            self._health_status = "Za mało światła!"
        elif self._temperature < 10:
            self._health_status = "Za zimno!"
        elif self._temperature > 30:
            self._health_status = "Za gorąco!"
        elif self._moisture >= 90:
            self._health_status = "Za dużo wody!"
        else:
            self._health_status = "Dobry"
