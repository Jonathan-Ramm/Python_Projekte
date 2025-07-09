# Zerlegung in Primzahl Addition mit dem Goldbach Algorithmus
from bitarray import bitarray

def sieve_bitarray(limit):
    is_prime = bitarray(limit + 1)
    is_prime.setall(True)
    is_prime[0:2] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i*i : limit + 1 : i] = False
    return is_prime

def goldbach_bit(n):
    if n <= 2 or n % 2 != 0:
        return False

    is_prime = sieve_bitarray(n)
    for p in range(2, n // 2 + 1):
        if is_prime[p] and is_prime[n - p]:
            print(f"{n} = {p} + {n - p}")
            return True
    return False

# Beispielaufruf
zahl = int(input("Gib eine gerade Zahl > 2 ein: "))
if goldbach_bit(zahl):
    print("Goldbach-Zerlegung gefunden.")
else:
    print("Keine Zerlegung gefunden.")
