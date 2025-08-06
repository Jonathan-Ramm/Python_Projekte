import tkinter as tk

equation = "1 + 2 * 3 - 4 / 5"  # Beispielgleichung

root = tk.Tk()
root.geometry("600x800")           # Startgröße
root.minsize(400, 600)             # Mindestgröße

root.configure(bg="lightblue")

canvas = tk.Canvas(root, bg="lightgray", height=130)
canvas.pack(side="top", fill="x")
buttons = tk.Canvas(root, bg="blue", height=400)
buttons.pack(side="bottom", fill="x")

# Optional: Text zentrieren und skalieren
text_id = canvas.create_text(0, 0, text=f"{equation}", font=("Arial", 20), anchor="center")

def on_resize(event):
    width = event.width
    height = canvas.winfo_height()
    canvas.coords(text_id, width / 2, height / 2)
    font_size = max(8, min(int(height / 2.5), int(width / 15)))
    canvas.itemconfig(text_id, font=("Arial", font_size))

canvas.bind("<Configure>", on_resize)

root.mainloop()