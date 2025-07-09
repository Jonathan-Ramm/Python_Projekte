# Wie viele Primzahlen gibt es bis a, wie hoch ist der Anteil dieser
def sieve_of_eratosthenes(limit):
    prime = [True for _ in range(limit+1)]
    p = 2
    while (p * p <= limit):
        if prime[p]:
            for i in range(p * p, limit+1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit) if prime[p]]
    return len(prime_numbers)


a = 100

prime_count = sieve_of_eratosthenes(a + 1)
prime_perc = prime_count / (a)
print ("Anteil: " + str(prime_perc))
print ("Anzahl: " + str(prime_count))
