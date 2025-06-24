import tkinter as tk
from tkinter import ttk


class PlantView:
    """Widok aplikacji, odpowiedzialny za interfejs użytkownika."""

    def __init__(self, master: tk.Tk, controller):
        self.master = master
        self.controller = controller
        master.title("Zdalna Roślinka 🌿")
        master.geometry("480x400")
        master.resizable(True, True)

        self.style = ttk.Style()

        # Główna ramka
        self.main_frame = ttk.Frame(master, padding=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        self.main_frame.rowconfigure((0, 2, 3), weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        # Nagłówek
        header = ttk.Label(self.main_frame, text="🌱 Panel Opieki Nad Roślinką", font=('Arial', 14, 'bold'))
        header.grid(row=0, column=0, pady=(0, 10), sticky="ew")

        # Status Roślinki
        self.status_frame = ttk.LabelFrame(self.main_frame, text="Stan Roślinki", padding=10)
        self.status_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        for i in range(4):
            self.status_frame.columnconfigure(i, weight=1)
        for i in range(3):
            self.status_frame.rowconfigure(i, weight=1)

        self.moisture_label = ttk.Label(self.status_frame, text="Wilgotność:")
        self.moisture_label.grid(row=0, column=0, sticky='w')
        self.moisture_bar = ttk.Progressbar(self.status_frame, orient="horizontal", mode="determinate", maximum=100)
        self.moisture_bar.grid(row=0, column=1, sticky='ew', padx=5)
        self.moisture_value = ttk.Label(self.status_frame, text="--%")
        self.moisture_value.grid(row=0, column=2, sticky='w')

        self.light_label = ttk.Label(self.status_frame, text="Światło:")
        self.light_label.grid(row=1, column=0, sticky='w')
        self.light_bar = ttk.Progressbar(self.status_frame, orient="horizontal", mode="determinate", maximum=100)
        self.light_bar.grid(row=1, column=1, sticky='ew', padx=5)
        self.light_value = ttk.Label(self.status_frame, text="--%")
        self.light_value.grid(row=1, column=2, sticky='w')

        self.temperature_label = ttk.Label(self.status_frame, text="Temperatura:")
        self.temperature_label.grid(row=2, column=0, sticky='w')
        self.temperature_bar = ttk.Progressbar(self.status_frame, orient="horizontal", mode="determinate", maximum=40)
        self.temperature_bar.grid(row=2, column=1, sticky='ew', padx=5)
        self.temperature_value = ttk.Label(self.status_frame, text="--°C")
        self.temperature_value.grid(row=2, column=2, sticky='w')

        self.time_label = ttk.Label(self.status_frame, text="Czas: --:00")
        self.time_label.grid(row=0, column=3, sticky='w', padx=(20, 0))

        self.health_label = ttk.Label(self.status_frame, text="Zdrowie: ---", font=('Arial', 10, 'bold'))
        self.health_label.grid(row=2, column=3, sticky='w', padx=(20, 0))

        # Separator
        separator = ttk.Separator(self.main_frame, orient='horizontal')
        separator.grid(row=2, column=0, sticky='ew', pady=5)

        # Akcje
        self.actions_frame = ttk.LabelFrame(self.main_frame, text="Akcje", padding=10)
        self.actions_frame.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        self.actions_frame.columnconfigure((0, 1), weight=1)

        self.water_button = ttk.Button(self.actions_frame, text="💧 Podlej Roślinkę", command=self.controller.water_plant)
        self.water_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.simulate_hour_button = ttk.Button(self.actions_frame, text="🕒 Symuluj 1 Godzinę", command=self.controller.simulate_hour)
        self.simulate_hour_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.simulate_day_button = ttk.Button(self.actions_frame, text="🌄 Symuluj 24 Godziny", command=self.controller.simulate_day)
        self.simulate_day_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Komunikat
        self.message_frame = ttk.LabelFrame(self.main_frame, text="Komunikat", padding=10)
        self.message_frame.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
        self.message_frame.columnconfigure(0, weight=1)

        self.message_label = ttk.Label(self.message_frame, text="---", font=('Arial', 10, 'italic'))
        self.message_label.grid(row=0, column=0, sticky="ew")

    def update_status_display(self, moisture: int, light: int, temperature: int, time_of_day: int, message: str, health_status: str) -> None:
        self.moisture_bar['value'] = moisture
        self.light_bar['value'] = light
        self.temperature_bar['value'] = temperature

        self.moisture_value.config(text=f"{moisture}%")
        self.light_value.config(text=f"{light}%")
        self.temperature_value.config(text=f"{temperature}°C")

        self.time_label.config(text=f"Czas: {int(time_of_day):02d}:00")
        self.message_label.config(text=message)

        self.health_label.config(text=f"Zdrowie: {health_status}")
        if health_status == "Dobry":
            self.health_label.config(foreground="green")
        else:
            self.health_label.config(foreground="red")

        self._set_dynamic_theme(time_of_day)

    def _set_dynamic_theme(self, time_of_day: int) -> None:
        """Dostosowuje motyw interfejsu w zależności od pory dnia."""
        day_color = "#f0f8ff"
        night_color = "#2e2e2e"

        if 18 <= time_of_day <= 22:
            factor = (time_of_day - 18) / 4
        elif 4 <= time_of_day <= 7:
            factor = 1 - ((time_of_day - 4) / 3)
        elif 7 < time_of_day < 18:
            factor = 0.0
        else:
            factor = 1.0

        bg_color = self._interpolate_color(day_color, night_color, factor)
        text_color = "black" if factor < 0.5 else "white"

        self.style.configure("TFrame", background=bg_color)
        self.style.configure("TLabel", background=bg_color, foreground=text_color)
        self.style.configure("TLabelframe", background=bg_color, foreground=text_color)
        self.style.configure("TLabelframe.Label", background=bg_color, foreground=text_color)
        self.master.configure(bg=bg_color)

    def _interpolate_color(self, start_color: str, end_color: str, factor: float) -> str:
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(*rgb)

        start_rgb = hex_to_rgb(start_color)
        end_rgb = hex_to_rgb(end_color)

        blended_rgb = tuple(
            int(start + (end - start) * factor)
            for start, end in zip(start_rgb, end_rgb)
        )
        return rgb_to_hex(blended_rgb)
