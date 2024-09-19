# funkce pro správu nákupního seznamu
def pridat_polozku(seznam):
    polozka = input("Zadej názem položky k přidání: ")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")


#hlavní program