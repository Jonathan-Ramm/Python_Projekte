import random

def main():
    number = random.randint(lower_limit, upper_limit)
    guess = int(input(f"Errate die Zahl zwischen {lower_limit} und {upper_limit}: "))
    attempts = 1    
    while guess is not number:
        if guess < number:
            print("Die gesuchte Zahl ist größer.")
            lower_limit = max(lower_limit, guess + 1)  
        elif guess > number:
            print("Die gesuchte Zahl ist kleiner.")
            upper_limit = min(upper_limit, guess - 1)
        guess = int(input(f"Errate die Zahl zwischen {lower_limit} und {upper_limit}: "))
        attempts += 1
    print(f"Herzlichen Glückwunsch! Du hast die Zahl {number} in {attempts} Versuchen erraten.")






def auto_main(lower_limit, upper_limit, number=None):
    if number is None:
        number = random.randint(lower_limit, upper_limit)
    
    attempts = 1
    guess = (lower_limit + upper_limit) // 2

    while guess != number:
        if guess < number:
            lower_limit = max(lower_limit, guess + 1)  
        else:
            upper_limit = min(upper_limit, guess - 1)
        guess = (lower_limit + upper_limit) // 2    
        attempts += 1

    return attempts



if __name__ == "__main__":
    i = 0
    all_attempts = 0
    max_attempts = 0
    min_attempts = 10000
    runs = 1000000000
    lower_limit = 1
    upper_limit = 100_000_000

    while i < runs:
        attempts = auto_main(lower_limit, upper_limit)
        all_attempts += attempts
        if attempts > max_attempts:
            max_attempts = attempts
            print(f"Neuer maxi Rekord: {max_attempts} Versuche!")
        if attempts < min_attempts:
            min_attempts = attempts
            print(f"Neuer mini Rekord: {min_attempts} Versuche!")
        i += 1
        if min_attempts == 1:
            print(f"Abbgebrochen nach {i} Versuchen!")
            break

    print(f"Maximale Anzahl an Versuchen: {max_attempts}")
    print(f"Minimale Anzahl an Versuchen: {min_attempts}")
    print(f"Durchschnittliche Anzahl an Versuchen: {all_attempts / i:.4f}")