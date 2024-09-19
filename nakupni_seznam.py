# funkce pro správu nákupního seznamu
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

#hlavní program