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
        print(seznam)
    else:
        print("Seznam je prázdný.")


def seradit_seznam(seznam):
    seznam.sort()

def zobrazit_pocet_polozek(seznam):
    print(f"V seznamu je {len(seznam)} položek.")

def ukoncit_program():
    exit
    
#hlavní program
