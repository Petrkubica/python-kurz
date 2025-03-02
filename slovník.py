# country = {"Poland" :" P ", "Germany":"G","Slovakia":"S","Austria":"A" }


import pickle

státy = {}

def add_staty():
    země = input("Zadejte název země: ")
    hl_mesta = input("Zadejte hlavní město: ")
    státy[země] = hl_mesta
    print(f"Přidáno: {země} - {hl_mesta}")

def vymaž_staty():
    země = input("Zadejte název země k odstranění: ")
    if země in státy:
        del státy[země]
        print(f"Země {země} byla odstraněna.")
    else:
        print("Země nebyla nalezena.")

def hledej_staty():
    země = input("Zadejte název země k vyhledání: ")
    print(státy.get(země, "Země nebyla nalezena."))

def oprav_staty():
    země = input("Zadejte název země k úpravě: ")
    if země in státy:
        hl_mesta = input("Zadejte nové hlavní město: ")
        státy[země] = hl_mesta
        print(f"Aktualizováno: {země} - {hl_mesta}")
    else:
        print("Země nebyla nalezena.")

def save_data():
    with open("countries.pkl", "wb") as f:
        pickle.dump(státy, f)
    print("Data byla uložena.")

def load_data():
    global státy
    try:
        with open("countries.pkl", "rb") as f:
            státy = pickle.load(f)
        print("Data byla načtena.")
    except FileNotFoundError:
        print("Soubor s daty nebyl nalezen.")

while True:
    print("\n1. Přidat zemi")
    print("2. Smazat zemi")
    print("3. Vyhledat zemi")
    print("4. Upravit zemi")
    print("5. Uložit data")
    print("6. Načíst data")
    print("7. Ukončit")
    
    choice = input("Vyberte akci (1-7): ")
    
    if choice == "1":
        add_staty()
    elif choice == "2":
        vymaž_staty()
    elif choice == "3":
        hledej_staty()
    elif choice == "4":
        oprav_staty()
    elif choice == "5":
      save_data()
    elif choice == "6":
        load_data()
    elif choice == "7":
        break
    else:
        print("Neplatná volba.")

print("Program ukončen.")


