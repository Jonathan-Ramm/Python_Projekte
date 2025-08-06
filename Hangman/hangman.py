import random

with open("Hangman/woerter.txt") as f:
  wort = random.choice(f.read().splitlines()).lower()

versuche= 8
gesucht = set(b for b in wort)
geraten = set()

while versuche > 0:
  text = f'Noch {versuche} Versuche: '
  text += " ".join([f"{buchstabe if buchstabe in geraten else '_'}" for buchstabe in wort])
  versuch = input(text + " Ihr Buchstabe? ").lower()
  geraten.add(versuch)
  if versuch not in gesucht: versuche -= 1
  if gesucht.issubset(geraten): break

text = "GEWONNEN! " if versuche > 0 else "VERLOREN! "
print(text + "Das gesuchte Wort war", wort)