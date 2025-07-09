def factorial(number):
    y = 1
    for x in range(1, number + 1):
        y = y * x
    return y


def wissenschaftliche_notation(zahl):
    exponent = int(f"{zahl:.0e}".split('e')[1])  # Exponent extrahieren
    mantisse = zahl / (10 ** exponent)          # Mantisse berechnen
    return f"{mantisse:.3f} * 10^{exponent}"    # Ausgabe mit 3 Nachkommastellen




a = 13
print(factorial(a))
print(wissenschaftliche_notation(factorial(a)))