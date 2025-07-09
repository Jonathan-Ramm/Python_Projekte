import math

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0&1 no prime
    
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
                
    return primes


# Die n. Primzahl ist weniger als n * log(n * log(n))

n = 420
approx_limit = int(n * (math.log(n) + math.log(math.log(n))))
primes = sieve_of_eratosthenes(approx_limit)


while len(primes) < n:
    approx_limit *= 2
    primes = sieve_of_eratosthenes(approx_limit)


thousandth_prime = primes[n-1]
print(thousandth_prime)
