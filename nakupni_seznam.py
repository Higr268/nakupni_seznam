# funkce pro správu nákupního seznam

def pridat_polozku(seznam):
    polozka = input("Zadej název položky k přidání: ")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")

def odebrat_polozku(seznam):
    polozka = input("Zadej název položky k odebrání: ")
    if polozka in seznam:
        seznam.remove(polozka)
        print(f"Položka {polozka} byla odebrána.")
    else:
        print(f"Položka {polozka} není v nákupním seznamu.")

def zobrazit_seznam(seznam):
    if seznam:
        print(f"Tohle je tvůj nákupní seznam {seznam}.")
    else:
        print("Seznam je prázdný.")


def seradit_seznam(seznam):
    seznam.sort()
    print("Nákupní seznam byl abecedně seřazen.")

def zobrazit_pocet_polozek(seznam):
    print(f"V seznamu je {len(seznam)} položek.")

def ukoncit_program():
    print("Program byl ukončen.")
    exit()
    
#hlavní program
seznam = []

while True:
    print("\n1 pro přidání položky.")
    print("2 pro odebrání položky.")
    print("3 pro zobrazení nákupního seznamu.")
    print("4 pro abecední seřazení nákupního seznamu.")
    print("5 pro zobrazení počtu položek v nákupním seznamu.")
    print("6 pro ukončení programu.")

    vyber = input("\nVyber možnost 1 až 6: ")
    if vyber == "1":
        pridat_polozku(seznam)
    elif vyber == "2":
        odebrat_polozku(seznam)
    elif vyber == "3":
        zobrazit_seznam(seznam)
    elif vyber == "4":
        seradit_seznam(seznam)
    elif vyber == "5":
        zobrazit_pocet_polozek(seznam)
    elif vyber == "6":
        ukoncit_program()
    else:
        print("Neplatný výběr možnosti. Zkus to znovu.")