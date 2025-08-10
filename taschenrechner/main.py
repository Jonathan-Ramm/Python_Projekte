import tkinter as tk
from tkinter import ttk

equation = ""  # Anzeige
operator = None
operand1 = None
last_equations = []  # Historie der letzten Berechnungen

def number_press(num):
    global equation
    equation += str(num)
    canvas.itemconfig(text_1, text=equation)

def set_operator(op):
    global equation, operand1, operator
    if equation == "":
        return
    operand1 = equation
    operator = op
    equation = ""
    canvas.itemconfig(text_1, text=equation)

def equal():
    global equation, operand1, operator
    if operand1 is None or equation == "" or operator is None:
        return
    try:
        operand2 = equation
        if operator == "+":
            result = float(operand1) + float(operand2)
        elif operator == "-":
            result = float(operand1) - float(operand2)
        elif operator == "*":
            result = float(operand1) * float(operand2)
        elif operator == "/":
            result = float(operand1) / float(operand2)
        elif operator == "^":
            result = float(operand1) ** float(operand2)
        else:
            result = "ERR"
        last_equations.append(f"{operand1} {operator} {operand2} = {result}")
        if len(last_equations) > 10:  # Maximal 10 Einträge in der Historie
            last_equations.pop(0)
        last_text = "\n".join(last_equations)
        last.itemconfig(text_2, text=last_text)
        equation = str(result)
        canvas.itemconfig(text_1, text=equation)
        operand1 = None
        operator = None
    except:
        equation = "ERR"
        canvas.itemconfig(text_1, text=equation)
        operand1 = None
        operator = None

def clear():
    global equation, operand1, operator
    equation = ""
    operand1 = None
    operator = None
    canvas.itemconfig(text_1, text=equation)


# GUI Aufbau
root = tk.Tk()
root.geometry("600x800")
min_x = 600
min_y = 400
root.minsize(min_x, min_y)
root.configure(bg="gray")
root.title("Taschenrechner")



canvas = tk.Canvas(root, bg="lightblue", height=130)
canvas.pack(side="top", fill="x")
last = tk.Canvas(root, bg="lightgray", height=800-400)
last.pack(side="left", fill="x", expand=True, )
text_2 = last.create_text(590, 10, text="", font=("Arial", 16), fill="black", anchor="se")


buttons = tk.Canvas(root, bg="blue", height=400)
buttons.pack(side="bottom", fill="x")

text_1 = canvas.create_text(0, 0, text="", font=("Arial", 20), anchor="center")

def on_resize(event):
    width = event.width
    height = canvas.winfo_height()
    canvas.coords(text_1, width / 2, height / 2)
    font_size = max(8, min(int(height / 2), int(width / 12)))
    canvas.itemconfig(text_1, font=("Arial", font_size))
    width = last.winfo_width()
    last.coords(text_2, width - 10, 10)

canvas.bind("<Configure>", on_resize)


# Zahlenbuttons
for i, num in enumerate(range(1, 10)):
    ttk.Button(buttons, text=str(num), command=lambda n=num: number_press(n)).grid(
        column=(i % 3) + 1, row=(2 - i // 3) + 1, padx=20, pady=20)

ttk.Button(buttons, text="0", command=lambda: number_press(0)).grid(column=2, row=4, padx=20, pady=20)

# Operatoren
ttk.Button(buttons, text="+", command=lambda: set_operator("+")).grid(column=4, row=1, padx=20, pady=20)
ttk.Button(buttons, text="-", command=lambda: set_operator("-")).grid(column=4, row=2, padx=20, pady=20)
ttk.Button(buttons, text="*", command=lambda: set_operator("*")).grid(column=4, row=3, padx=20, pady=20)
ttk.Button(buttons, text="/", command=lambda: set_operator("/")).grid(column=4, row=4, padx=20, pady=20)
ttk.Button(buttons, text="^", command=lambda: set_operator("^")).grid(column=5, row=2, padx=20, pady=20)
ttk.Button(buttons, text=".", command=lambda: number_press(".")).grid(column=1, row=4, padx=20, pady=20)

# Ergebnis und Löschen
ttk.Button(buttons, text="=", command=equal).grid(column=5, row=4, padx=20, pady=20)
ttk.Button(buttons, text="C", command=clear).grid(column=5, row=3, padx=20, pady=20)

root.mainloop()
