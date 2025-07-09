weight = input("Wie viel wiegst du? ")
art = input("(K)g oder (L)bs? ")
art_lower = art.lower()

if(art_lower == "l"):
    kg = int(weight) * 0.453592
    print("Du wiegst: " + str(round(kg, 1)) + " Kilogramm.")
elif(art_lower == "k"):
    lbs = int(weight) * 2.20462
    print("Du wiegst: " + str(round(lbs, 1)) + " Pfund.")
else:
    print("DU DUMM!")