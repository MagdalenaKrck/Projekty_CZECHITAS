import requests
import json

# ČÁST 1

# uživatel zadá IČO subjektu
ico = input("Zadejte IČO subjektu: ")

# adresa pro GET požadavek
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

#  data z API
response =  requests.get(url)

# převedení JSON do Pythonu
data = response.json()

# získání dat
obchodni_jmeno = data.get('obchodniJmeno')
adresa = data.get('textovaAdresa')

print(obchodni_jmeno)
print(adresa)

#   ČÁST 2

# zadání hledaného názvu
nazev_subjektu = input("Zadejte název subjektu pro vyhledání: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

#  vytvořím data pro POST požadavek
data = json.dumps({"obchodniJmeno": nazev_subjektu})

#  pošlu POST požadavek na API
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

response = response.json()

# získání počtu nalezených subjektů
nalezeny_pocet = response.get('pocetCelkem')
print(f"Nalezeno subjektů: {nalezeny_pocet}")

# výpis detailů
subjekty = response.get('ekonomickeSubjekty')
for subjekt in subjekty:
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")