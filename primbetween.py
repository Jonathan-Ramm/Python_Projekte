def ist_primzahl(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ziffer_enthalten(zahl, ausgeschlossene_ziffern):
    for ziffer in ausgeschlossene_ziffern:
        if str(ziffer) in str(zahl):
            return True
    return False

def primzahlen_zwischen(a, b, ausgeschlossene_ziffern=[]):
    primzahlen = []
    for zahl in range(a, b + 1):
        if ist_primzahl(zahl) and not ziffer_enthalten(zahl, ausgeschlossene_ziffern):
            primzahlen.append(zahl)
    return primzahlen


a = int(input("Gib die Startzahl (a) ein: "))
b = int(input("Gib die Endzahl (b) ein: "))
ausgeschlossene_ziffern = input("Gib die auszuschließenden Ziffern ein (durch Komma getrennt, z.B. 7,8): ").split(",")


ausgeschlossene_ziffern = [ziffer.strip() for ziffer in ausgeschlossene_ziffern if ziffer.strip().isdigit()]


print(f"Primzahlen zwischen {a} und {b}, ohne die Ziffern {', '.join(ausgeschlossene_ziffern)}: {primzahlen_zwischen(a, b, ausgeschlossene_ziffern)}")
