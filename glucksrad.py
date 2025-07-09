import tkinter as tk
import random

felder = ["WAT", "Biologie", "Deutsch", "Politische Bildung", "Erdkunde", "Physik", "Geschichte", "Mathe", "Informatik"]

class GluecksradApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎡 Glücksrad")

        self.label = tk.Label(root, text="", font=("Arial", 24), width=30, height=4)
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Drehen!", font=("Arial", 18), command=self.drehen)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 20))
        self.result_label.pack(pady=20)

        self.running = False

    def drehen(self):
        if self.running:
            return  
        self.running = True
        self.result_label.config(text="")
        self.animate(0, random.randint(30, 50)) 

    def animate(self, count, max_count):
        if count >= max_count:
            gewinner = self.label["text"]
            self.result_label.config(text=f"🎉 Ergebnis: {gewinner}")
            self.running = False
            return

        feld = random.choice(felder)
        self.label.config(text=feld)
        delay = int(20 + (count**1.3)) 
        self.root.after(delay, lambda: self.animate(count + 1, max_count))


root = tk.Tk()
app = GluecksradApp(root)
root.mainloop()
