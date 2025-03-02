
# import json
# import pickle

# class Address:
#     def __init__(self, city, street, apartment):
#         self.city = city
#         self.street = street
#         self.apartment = apartment

#     def __str__(self):
#         return f"{self.city}{self.street}{self.apartment}"    
    
#     def to_dict(self):
#         return {
#             "city": self.city,
#             "street": self.street,
#             "apartment": self.apartment
#         }
    
# class Human:
#     def __init__(self, name, last_name, address):
#         self.name = name
#         self.last_name = last_name
#         self.address = address   

#     def __str__(self):
  
#       return f"{self.name}{self.last_name}{self.address}"
    

#     def to_dict(self):
#         return {
#             "name": self.name,
#             "last_name": self.last_name,
#             "address": self.address.to_dict()
#         }   
 

# first_obj = Human("Marc", "Dylan", Address("New York", "Mulberry Street 162", "33b")) 

# serialized = json.dumps(first_obj.to_dict())
# print(f"Serialized object:\n\n{serialized}\n\n")

# # Uložení do souboru
# with open("data.json", "w") as file:
#     json.dump(first_obj.to_dict(), file)

# # Načtení ze souboru
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)

# # Vytvoření objektu z načtených dat
# loaded_obj = Human(loaded_data["name"], loaded_data["last_name"], Address(**loaded_data["address"]))

# deserialized = json.loads(serialized)

# second_obj = Human(deserialized["name"], deserialized["last_name"], Address(**deserialized["address"]))
# print(f"Deserialized object:\n\n{second_obj}")





# Zde získejte jméno od uživatele

# Zde získejte věk od uživatele (jako číslo)

# Zde vytvořte pozdrav používající jméno a věk

# Vypište pozdrav


# print("Ahoj jak se máš ? Mohu se tě zeptat")
# name=input("Jak se jmenuješ?\n")
# age= int(input("kolik máš let?\n"))

# print (f"Velice mne těší " + name )
# print (f"už máš " + str(age)+ " let" + " To už jsi dost starý na to jít do kina")
# print ("Tak zase příště , měj se pěkně " + name)


# nákupní_seznam = []

# while True:
#     print("\nCo chcete udělat?")
#     print("1: Přidat položku")
#     print("2: Zobrazit seznam")
#     print("3: Odstranit položku")
#     print("4: Ukončit")
    
#     volba = input("Zadejte číslo volby: ")
    
#     if volba == "1":
#         položka = input("Zadejte název položky k přidání: ")
#         nákupní_seznam.append(položka)
#         print(f"Položka '{položka}' byla přidána do seznamu.")

#     elif volba == "2":
#         if nákupní_seznam:
#             print("Váš nákupní seznam:")
#             for index, položka in enumerate(nákupní_seznam, 1):
#                 print(f"{index}. {položka}")
#         else:
#             print("Váš nákupní seznam je prázdný.")

#     elif volba == "3":
#         if nákupní_seznam:
#             print("Aktuální seznam:")
#             for index, položka in enumerate(nákupní_seznam, 1):
#                 print(f"{index}. {položka}")
#             try:
#                 index_k_odstranění = int(input("Zadejte číslo položky k odstranění: ")) - 1
#                 odstraněná_položka = nákupní_seznam.pop(index_k_odstranění)
#                 print(f"Položka '{odstraněná_položka}' byla odstraněna ze seznamu.")
#             except (ValueError, IndexError):
#                 print("Neplatné číslo položky.")
#         else:
#             print("Seznam je prázdný, není co odstranit.")
#     elif volba == "4":
#         print("Děkuji za použití programu. Na shledanou!")
#         break
#     else:
#         print("Neplatná volba. Zkuste to znovu.")


# adresář={}


# print("Co chete udělat v adresáři?")
# print("1:vložte nový kontakt")
# print("2:odstraňte kontakt z adresáře")
# print("3:ukaž adresář")
# volba=input("zadej svou volbu")

# while True:

#     if volba =="1":
#      nový=input("Vložte nový kontakt")
#      adresář.append(nový)
#      print (f"Nový kontakt {nový} byl přidán do adresáře")

#     elif volba == "2" :
#        delete=input("Zadejte kontakt pro vymazání")
#        adresář.remove("Vložte kontakt pro vymazání")
#        print (f"Kontakt {delete} byl vymazán ze seznamu")

#     elif volba == "3":
#        print (f"Ve tvém adrsáři jsou následující kontakty.{adresář}")   

#     else:
#        print("Špatná volba")
             



# nespouštějte program!
# jaké hodnoty se podle vás vytisknou do konzole? 
# vaši předpověď napište do komentářů níže:
#
#
#
#
#
#
# #

# foods = ["pizza", "hamburger", "chicken"]

# favourite_food = foods[1]
# print(favourite_food)
# # hamburger
# number = 0
# print(foods[number])
# # pizza
# print(foods[-1])
# # # chicken
# for meal in foods:
#     print("My favourite food is: " + meal)
# # ˇvšechny položky
# if "pizza" in foods:
#     print("Yes!")
#    #  yes




# my_favorite_game = ["roblox","minecraft", "tetris"]

# print(my_favorite_game[0])


# for game in my_favorite_game :
#    game= (input( "How your favorite game\n"))
#    if game in my_favorite_game :
#     print ("I like too")
   
#    else:
#     print("It's not bet game") 



# my_favorite_games = ["roblox", "minecraft", "tetris"]

# for i in range(3):  # Opakujeme 3krát
#     game = input("What's your favorite game?\n").lower()  # Převedeme na malá písmena
#     if game in my_favorite_games:
#         print("I like that too!")
#     else:
#         print("That's not bad, but not my favorite.")



#  nespouštějte program!
# jaké hodnoty se podle vás vytisknou do konzole? 
# vaši předpověď napište do komentářů níže:
#
#
#
#
#
#
#

# groceries = ["eggs", "milk", "bread", "honey", "milk"]

# groceries[0] = "water" #na první pozici se objeví water místo eggs
# print(groceries)

# groceries.append("eggs") #přidá se do seznamu eggs
# print(groceries)

# groceries.remove("milk") #vymaže se ze seznamu první milk 
# print(groceries)

# print(len(groceries)) # vytiskne se do konzole  water , bread , honey , milk ,eggs


# wallet = [1, 2, 2, 5, 5, 5, 10, 20, 50, 100, 100, 200, 500, 2000]
# coin_wallet = []

# for money in wallet:
#     if money < 51:
#         coin_wallet.append(money)

# print("In my coin wallet are these coins: ")
# for coin in coin_wallet:
#     print(coin)

# Co se stane na řádku 2?
#   Odpověď vytiskne se postupně celý seznam řádek po řádku

# Popište, co se stane při první iteraci v prvním for cyklu na řádku 4.
#   Odpověď

# Co by se stalo, pokud bych NEodsadila příkaz na řádku 5? 
#   Odpověď

# Co by se stalo, pokud bych NEodsadila příkaz na řádku 6?
#   Odpověď

# Co by se stalo, pokud bych ODSADILA příkaz na řádku 8?
#   Odpověď




video_games = ["Mario", "Sonic", "Joust", "Zelda"]
print("[2]")
game=input("zadej číslo od 0-3\n")


for game in video_games:
   if game in video_games:
      print(game)