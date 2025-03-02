# # nespouštějte program!
# # jaké hodnoty se podle vás vytisknou do konzole? 
# # vaši předpověď napište do komentářů níže:
# #
# #
# #
# #
# #
# #
# #

# foods = ["pizza", "hamburger", "chicken"]

# favourite_food = foods[1]
# print(favourite_food)
# # hamburger

# number = 0
# print(foods[number])
# # pizza

# print(foods[-1])
# # chicken

# for meal in foods:
#     print("My favourite food is: " + meal)
#     #  pizza , hamburger,chicken

# if "pizza" in foods:
#     print("Yes!")
#     #  yes


names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Show name")
print("3. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")

###### Úkol - Prozkoumej kód

# Co se stane, pokud po spuštění programu vyberete možnost 1?
 # Odpověď: vytisknou se všechny jmena

# Co se stane, pokud po spuštění programu vyberete možnost 2 a vložíte index 0?
  # Odpověď: vytiskne se alex

# Co se stane, pokud po spuštění programu vyberete možnost 2 a vložíte index -5?
  # Odpověď:vytiskne se sue

# Co se stane, pokud po spuštění programu vyberete možnost 2 a vložíte index 7?
  # Odpověď: chyba value error

# Co je účelem příkazu int(input()) na řádku 7?
  # Odpověď:vložení bude číslo intiger a ne třeba string

# Jaký příkaz se provede, pokud nebude splněna žádná podmínka?
  # Odpověď: good bye