from math import factorial
from decimal import Decimal, getcontext

def calculate_pi_chudnovsky(precision):
    """
    Berechnet π mit dem Chudnovsky-Algorithmus.
    """
    # Setzt die Dezimalgenauigkeit
    getcontext().prec = precision + 5

    # Konstanten
    C = 426880 * Decimal(10005).sqrt()
    M = Decimal('545140134')
    L = Decimal('13591409')
    X = Decimal('-640320')**3
    K = Decimal(6)
    S = Decimal(0)

    for k in range(precision // 14 + 1):  # Iterationen, abhängig von der gewünschten Präzision
        # Berechne jeden Term der Chudnovsky-Reihe
        numerator = Decimal(factorial(6 * k)) * (L + M * k)
        denominator = Decimal(factorial(3 * k)) * (Decimal(factorial(k))**3) * X**k
        S += numerator / denominator

    pi = C / S
    return str(+pi)[:precision + 2]  # Entfernt überschüssige Stellen

# Anzahl der Dezimalstellen
decimal_places = 10000 
pi = calculate_pi_chudnovsky(decimal_places)
print(f"Pi mit {decimal_places} Dezimalstellen:\n{pi}")
