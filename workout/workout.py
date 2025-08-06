import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from playsound import playsound  # pip install playsound
import winsound

def play_countdown_sound(sec):
    freq = int(500 + (5 - sec) * 200)
    duration = 100  # ms
    if sec < 2: duration =1000
    winsound.Beep(freq, duration)


# Trainingsplan als Dict: Wochentag -> Liste von Übungen mit Beschreibung und Wiederholungen/Zeit
trainingsplan = {
    "Montag": [
        ("Joggen gehen", None),
    ],
    "Dienstag": [
        ("Liegestütze (verschiedene Varianten)", "4 Sätze x 10-15 Wiederholungen"),
        ("Pause zwischen den Sätzen", "60-90 Sekunden"),
        ("Hantel-Bankdrücken (auf dem Boden liegend)", "4 Sätze x 8-12 Wiederholungen"),
        ("Pause", "60-90 Sekunden"),
        ("Plank (Unterarmstütz)", "3 Sätze, jeweils 30-60 Sekunden halten"),
        ("Pause", "30-60 Sekunden"),
        ("Seitstütz (je Seite)", "3 Sätze x 30 Sekunden"),
        ("Pause", "30-60 Sekunden"),
        ("Bizeps-Curls mit Hantel", "3 Sätze x 10-12 Wiederholungen"),
        ("Pause", "60 Sekunden"),
        ("Trizeps-Kickbacks mit Hantel", "3 Sätze x 10-12 Wiederholungen"),
        ("Pause", "60 Sekunden"),
        ("Schulterheben (Shrugs) mit Hantel", "3 Sätze x 12-15 Wiederholungen"),
        ("Pause", "60 Sekunden"),
    ],
    "Mittwoch": [
        ("Pause / Erholung", None),
    ],
    "Donnerstag": [
        ("Russian Twists (mit Hantel)", "3 Sätze x 20 Wiederholungen (10 pro Seite)"),
        ("Pause", "30-60 Sekunden"),
        ("Beinheben liegend", "3 Sätze x 12-15 Wiederholungen"),
        ("Pause", "30-60 Sekunden"),
        ("Superman-Hold", "3 Sätze x 30 Sekunden"),
        ("Pause", "30 Sekunden"),
        ("Schulterdrücken mit Hantel", "3 Sätze x 8-12 Wiederholungen"),
        ("Pause", "60-90 Sekunden"),
        ("Hantelrudern einarmig", "3 Sätze x 10-12 Wiederholungen pro Seite"),
        ("Pause", "60 Sekunden"),
        ("Hammer-Curls (neutraler Griff)", "3 Sätze x 10-12 Wiederholungen"),
        ("Pause", "60 Sekunden"),
    ],
    "Freitag": [
        ("Joggen gehen", None),
    ],
    "Samstag": [
        ("Liegestütze", "3 Sätze x 12-15 Wiederholungen"),
        ("Pause", "60 Sekunden"),
        ("Hantel-Sumo-Kniebeuge", "3 Sätze x 12 Wiederholungen"),
        ("Pause", "60-90 Sekunden"),
        ("Plank", "3 Sätze x 45 Sekunden"),
        ("Pause", "30-60 Sekunden"),
        ("Bizeps- und Trizeps Supersatz mit Hantel", "je 3 Sätze x 10 Wiederholungen"),
        ("Pause", "60 Sekunden"),
        ("Schulterkreisen mit Hantel", "3 Sätze x 15 pro Richtung"),
        ("Pause", "30 Sekunden"),
    ],
    "Sonntag": [
        ("Pause / Erholung", None),
    ],
    "Debug": [
        ("Liegestütze", "3 Sätze x 12-15 Wiederholungen"),
        ("Pause", "6 Sekunden"),
    ],
}



class TrainingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trainingsplan Timer")

        self.day_var = tk.StringVar(value="Montag")
        self.exercise_index = 0
        self.timer_running = False

        # Wochentag Auswahl
        ttk.Label(root, text="Wähle den Wochentag:").pack(pady=5)
        self.day_combo = ttk.Combobox(root, values=list(trainingsplan.keys()), textvariable=self.day_var, state="readonly")
        self.day_combo.pack(pady=5)
        self.day_combo.bind("<<ComboboxSelected>>", self.reset_exercise)

        # Anzeige Übung
        self.exercise_label = ttk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.exercise_label.pack(pady=20)

        # Anzeige Wiederholungen / Zeit
        self.detail_label = ttk.Label(root, text="", font=("Arial", 14))
        self.detail_label.pack(pady=5)

        # Timer Label
        self.timer_label = ttk.Label(root, text="", font=("Arial", 24), foreground="red")
        self.timer_label.pack(pady=15)

        # Knöpfe
        self.next_button = ttk.Button(root, text="Start / Weiter", command=self.next_exercise)
        self.next_button.pack(pady=10)

        self.reset_exercise()

    def reset_exercise(self, event=None):
        self.exercise_index = 0
        self.timer_running = False
        self.timer_label.config(text="")
        self.show_exercise()

    def show_exercise(self):
        day = self.day_var.get()
        exercises = trainingsplan[day]

        if self.exercise_index >= len(exercises):
            self.exercise_label.config(text="Training beendet!")
            self.detail_label.config(text="")
            self.next_button.config(state="disabled")
            self.timer_label.config(text="")
            return

        exercise, detail = exercises[self.exercise_index]
        self.exercise_label.config(text=exercise)
        self.detail_label.config(text=detail if detail else "")
        self.timer_label.config(text="")
        self.next_button.config(state="normal")

    def next_exercise(self):
        if self.timer_running:
            return  # Verhindere mehrfach Start

        day = self.day_var.get()
        exercises = trainingsplan[day]

        if self.exercise_index >= len(exercises):
            return

        exercise, detail = exercises[self.exercise_index]

        # Wenn Pause mit Zeitangabe, dann Timer starten
        if detail and ("Sekunden" in detail or "Sek" in detail):
            seconds = self.parse_seconds(detail)
            if seconds:
                self.next_button.config(state="disabled")
                self.timer_running = True
                threading.Thread(target=self.countdown, args=(seconds,)).start()
                return

        # Bei Wiederholungen einfach weiter zum nächsten mit Klick
        self.exercise_index += 1
        self.show_exercise()

    def parse_seconds(self, detail):
        # Detail enthält typischerweise "60 Sekunden" oder "30-60 Sekunden"
        import re
        match = re.findall(r"(\d+)", detail)
        if match:
            # Bei Bereich wie 30-60 nehmen wir den Mittelwert
            if len(match) >= 2:
                return (int(match[0]) + int(match[1])) // 2
            return int(match[0])
        return None

    def countdown(self, seconds):
        for sec in range(seconds, 0, -1):
            self.timer_label.config(text=f"{sec} s")
            if sec <= 5:
                try:
                    play_countdown_sound(sec)
                except:
                    pass
            time.sleep(1)
        play_countdown_sound(sec)
        self.timer_label.config(text="Fertig!")
        self.timer_running = False
        self.exercise_index += 1
        self.show_exercise()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingsApp(root)
    root.mainloop()
