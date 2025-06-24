import tkinter as tk
from model import PlantModel
from view import PlantView


class PlantController:
    """Kontroler aplikacji, który pośredniczy między modelem a widokiem."""

    def __init__(self):
        """Inicjalizuje kontroler, model i widok."""
        self.model = PlantModel()
        self.root = tk.Tk()
        self.view = PlantView(self.root, self)
        self.update_view()

    def update_view(self) -> None:
        """Pobiera stan z modelu i aktualizuje widok."""
        self.view.update_status_display(
            moisture=self.model.get_moisture(),
            light=self.model.get_light(),
            temperature=self.model.get_temperature(),
            time_of_day=self.model.get_time_of_day(),
            message=self.model.get_message(),
            health_status=self.model.get_health_status()
        )

    def water_plant(self) -> None:
        """Obsługuje kliknięcie przycisku podlewania."""
        self.model.water()
        self.update_view()

    def simulate_hour(self) -> None:
        """Symuluje jedną godzinę upływu czasu."""
        self.model.simulate_time(hours=1)
        self.update_view()

    def simulate_day(self) -> None:
        """Symuluje 24 godziny upływu czasu."""
        self.model.simulate_day()
        self.update_view()

    def run(self) -> None:
        """Uruchamia główną pętlę aplikacji GUI."""
        self.root.mainloop()


if __name__ == "__main__":
    app = PlantController()
    app.run()
