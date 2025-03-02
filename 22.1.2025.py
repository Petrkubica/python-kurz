# Spusťte program a odpovězte na otázky níže!

# number = 5
# print("I have thought of a number between 1 and 10")
# guess = int(input("Can you guess what it is?"))

# if guess == number:
#     print("Correct!")
# else:
#     print("Not correct!")

# print(guess == number)

##### Úkol - Prozkoumej kód

# Jakou hodnotu musí uživatel zadat do konzole, aby se vytiskl řetězec "Correct" do konzole?
# Odpověď: musí zadat 5 

# Co se stane, pokud uživatel zadá do konzole hodnotu 9 nebo 1 nebo -5?
# Odpověď: vytiskne se not corect

# Co vytiskne do konzole příkaz na řádku 12? Jakého datového typu je hodnota?
# Odpověď:
#  jeˇto  intiger a vytiskne se false
# Co by se stalo, pokud bych na řádku 8 zapomněla odsadit print příkaz?
# Odpověď: vytiskl by se vždy

# Co se stane, pokud zapomenu na řádku 7 zapsat dvojtečku za podmínku? Vyzkoušejte! Nezapomeňte si pak kód opravit!
# Odpověď: vyhodí mi to chybu . nebude uzavřena podmínka

# Co se stane, pokud na řádku 7 zapíši = místo == ?Vyzkoušejte! Nezapomeňte si pak kód opravit!
# Odpověď:s jedním rovnáse se přetipuje promenná dvě rovnáse  je porovnává 



# print("Welcome!\nWelcome to our coffee shop!")

# print("mohu vám nabídnout dnešní speciality \n Kaffelatte \n capuchino \n smothee\n juice  ")
# souhlas= input(("vlož ano / ne \n "))

# if souhlas == ("ano"):
#   print()
 
# else:
#  print("Mrzí nás že odcházíte") 
#  exit(0)


# drink=input("co si dáte k pití\n")

# kaffelatte=56
# capuchino=58
# smothee=78
# juice=36



# if drink=="kaffelatte":
#     print(f"cena nápoje je {kaffelatte} kč")

# elif drink=="capuchino":
#     print (f"cena nápoje je {capuchino} kč")

# elif drink=="smothee":
#     print (f"cena nápoje je {smothee}kč")       
    
     
# elif drink=="juice":
    
#     print(f"cena nápoje je {juice} kč")
# else:
#     print("tento nápoj bohužek nemáme")

# nespouštějte program!
# jaké 2 řetězce se podle vás vytisknou do konzole? 
# vaši předpověď napište do komentářů níže
#
#
#

# weather = "rain"

# if weather == "sunny":
#     print("Take your sunglasses!")
# elif weather == "snow":
#     print("Take your coat!")
# elif weather == "rain":
#     print("Take your umbrella!")
# else:
#     print("No advice for you!")

# number = 6

# if number > 7:
#     print("Number is higher than seven")
# elif number < 7:
#     print("Number is lower than seven")
# else:
#     print("Both numbers are the same")


# number1 = int(input("Please enter a number\n"))
# number2 = int(input("Please enter another number\n"))
# number3 = int(input("Please enter a third number\n"))

# if number1 > number2:
#   print("Number 1 is bigger than number 2")
# elif number2 > number1: 
#   print("Number 2 is bigger than number 1")
# elif number1>number3:
#   print("number is bigger than number")
# elif number2>number3:
#   print ("number2 is bigger than number 3")  
# else:
#   print("Both numbers are the same")




# zadání čísla 0-23

# number=int(input("vlož číslo v rozmezí 0-23\n"))

# if number <8:
#     print("TOO EARLY")
# elif number <=12:
#     print ("Good morning")
# elif number <18:
#     print ("Good Afternoon")    
# elif number ==18 :
#     print("Dinner time")   
# elif number<24:
#     print("Good night")    
# else:
#     print("Sorry I do not recognise that!")


# nespouštějte program!
# jaké 2 řetězce se podle vás vytisknou do konzole? a proč?
# vaši předpověď napište do komentářů níže
#
# #

# name = "Dave"
# homeTown = "Seattle"
# if name == "Dave" and homeTown == "Seattle":#vytiskne se tato hláška protož jsou obě podmínky pravdivé. 
#     print("Hi there Dave from Seattle!")
# else:
#     print("You're not Dave from Seattle!")

# if name == "Dave" or homeTown == "Seattle":#a také se vytiskne tato protže je minimálně jedna z podmínek pravdivá
#     print("You're either called Dave or you're from Seattle!")
# else:
#     print("You're not Dave, and you aren't from Seattle!")


# birthMonth = int(input("Enter the number of the month in which you were born. \n"))

# if birthMonth >= 1 and birthMonth <=12:
#     print("Thanks")
# else:
#     print("That's not a valid month!")

# # Jaký logický operátor je použit v tomto programu?
#     #and

# # Co by se stalo pokud bych and napsala velkými písmeny?
#     #python by jej neznal a vyhodil by to jako chybu

# # Co by se stalo, pokud bych místo >= 1 použila > 1? Nápověda: Upravte program a otestujte jej s hodnotou 0 a 1 a 2.
#     #počítalo by to od dvojiky a jedničku by to nevzalo

# # Co by ses stalo, pokud bych místo operátoru and použila operátor or? Nápověda: Upravte program a otestujte jej s různými číslicemi.
#     # v tomto programu by se nestalo nic , vytisklo by to stejně 


# print("Enter the hour in 24 hour clock (0 to 23)")
# hour = int(input())

# # if hour >=0  and hour<= 8:
# #     print("Too early!")
# # elif hour >=9 and hour<= 12:
# #     print("Good morning!")
# # elif hour >=13 and hour < 18:
# #     print("Good afternoon!")
# # elif hour == 18:
# #     print("Dinner time!")
# # elif hour >19 and hour <= 24:
# #     print("Good night!")
# # else:
# #     print("Sorry, I don’t recognise that!")

# # guess=input("hádej jakou mám barvu vlasů 'zadej barvu\n'")

# # if guess== "brown":
# #     print ("uhádl jsi barvu mých vlasu")
# # else: print("Bohužel ")    

# # guess2 = input("hádej barvu mých očí 'zadej barvu'\n")    
# # if guess == "brown"and guess2== "brown" :
# #     print("Jsi dobréj , uhadl jsi obě možnosti")
# # # elif guess2== "brown" :
# #     # print("uhádl jsi barvu mých očí")
# # elif guess=="brown"or guess2=="brown":
# #     print("Máš alespoň jeden bod")
# # else:

# #  print("Bohužel ,zkus to příště.")

# # nespouštějte program!
# # jaké řetězce se podle vás vytisknou do konzole? a proč?
# # vaši předpověď napište do komentářů níže
# #
# #
# # #
# # answer = "Berlin"

# # while answer != "Paris":
# #   print("Incorrect! Try again.")
# #   answer = "Paris"

# # print("Correct!")



# number = 1

# while number < 100:
#     print(number)
#     number = number * 2 # pro zopakování: hvězdička slouží k násobení

# # Kolik itera 6

# # Co by se stalo, pokud bych zapomněla zapsat příkaz na řádku 5 (tedy změnit hodnotu proměnné)?
#   #asi by příkaz bežel pořád dokolA

# # Co by se stalo, pokud bych zapomněla na dvojtečku na řádku 3?

#   #syntax error

# # Co by se stalo, pokud bych zapomněla odsadit příkaz za dvojtečkou (tedy např. řádek 4)?
#   #chyba odsazení

password1= ("proc")

name= input("vlož sve užicvatelské jmeno\n")
password2=input("vlož své heslo\n")

while password1 != password2:
    # print("try again")
    password=input()


    print("corect ")