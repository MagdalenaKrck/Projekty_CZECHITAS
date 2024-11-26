import json

# Otevření a načtení obsahu souboru
with open('alice.txt', encoding='utf-8') as alenka:
    text = alenka.read()

# převod znaků na malá písmena a ignorovat nový řádek \n a mezery

text = text.lower().replace(" ", "").replace("\n", "")

# Nový slovník pro uložení četností znaků
cetnost = {}

# Projít každý znak v textu
for znak in text:
    if znak not in cetnost:
        cetnost[znak] = 1  # přidá do slovníku, pokud tam ještě není
    else:
        cetnost[znak] += 1 

serazeny = dict(sorted(cetnost.items()))

with open('hw01_output.json', 'w', encoding='utf-8') as alenka:
    json.dump(serazeny, alenka, ensure_ascii=False, indent=4) # indent=4 je kvůli čitelnosti

# for klic, hodnota in serazeny.items():
#     print(klic, hodnota)
