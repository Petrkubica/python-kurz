# fruit = "apple"
# best_fruit = fruit
# fruit = "banana"

# print(best_fruit)

# best_Icecream= "vanilla"
# dont_like_icecream = "smurf"

# print(best_Icecream)

# print(dont_like_icecream)


##### Úkol - Prozkoumej kód

# Co by se stalo, pokud bych na řádku 1 zapoměla řetězec ohraničit uvozovkami?   
 # Odpověď: nevytiskl by se 

# Co by se stalo, pokud bych na řádku 5 chtěla vytisknout Best_fruit místo best_fruit?
 # Odpověď: nevytisklo by se to jelikož by ho python neznal .

# Proč je výstupem příkazu na řádku 5 apple a ne banana?
 # Odpověď:



# napište předpověď toho, co se stane, až se program spustí (do komentářů pod každý příkaz)
# print("Hello! What's your name?")
# # vytiskne řetězec
# name = input()
# #k proměnné name přiřadí vstup od uživatele
# print(name)
# #vytiskne co uživatel zadal
# print("Hi " + name + "! How are you today?")
# #vytiskne řetezec + vstup od uživatele tak aby celá vytištěná věta davala smysl




# # spustit kód, prozkoumat a odpovědět na otázky do komentáře
# # nezapomenout na Enter při vkládání textu do konzole
# print("Hi , how is your name ")
# name = input()

# print("Do you like programming,"  + name +" ?")
# like_programming = input()
# print("Great, " + name + ", you said " + like_programming + "!")

# more_programming = input("Do you want more programming, " + name + "? \n")
# print("Great, you said " + more_programming + " to more programming!")

# ##### Úkol - Prozkoumej kód

# # Jakému řetězci bude přiřazena proměnná name na řádku 4?



# print("Welcome!\nWelcome to our restaurant!")
# name = input("What's your name? \n")


# print("Vítejte v naší internetové restauraci\n co si budete přát?")
# print("mohu vám nabídnout hlavní menu \n pizza s feferonkami \nkuře na paprice\ntortila s kuřecím masem")
# print("prosím zadejte svou volbu")
# menu= str(input())

# print("Dáte si něco k pití? \n mohu vám nabídnout : \n ledový čaj \ncola\nfanta\n neperlivá voda")
# drink=str(input())
# print(f" zkontrolujte si vaší objednávku "+ menu + " " + drink)
# print ("Děkujeme za vaší objednávku ,ihned začneme na vaší objednávce pracovat")
# print ("Nakonec budeme potřebovat ještě váš telefon a  adresu")
# address= input("vlož adresu pro doručení")
# telephone= input("vlož telefonní kontakt")

# print("souhrn Vašší objednávky "+ menu + " ,"+ drink ) 
# print("dodací údaje "+address + " ," + telephone)
# print("Děkujeme za vaší objednávku")



# napište předpověď toho, co se stane, až se program spustí (do komentářů pod každý příkaz)

# print(6 + 2)
# # sečte a zobrazí výsledek
# print(6 - 2)
# #odečte  zobrazí výsledek
# print(6 * 2)
# #vynásobí a zobrazí výsledek
# print(10 / 4)
# #vydělí a zobrazí výsledek
# num = 20
# # vloží se do proměnné hodnota
# num2 = 5
# #vloží se do další proměnné přiřazená hodnota
# num = 10
# # první proměnná se změní na jinou hodnotu 
# result = num - num2
# #obě proměnné se uloží do nové proměnné jako výsledek 
# print(result)
# #vytiskne se nám výsledek proměnné num-num2
# print("6 + 2")
# # vytiskne se nám číslo 6+2 protože to počítač bere jako string a ne jako číslo



# # Spusťte program, vložte do konzole požadované vstupy a odpovězte na otázky níže!

# print("Enter a number:")
# num = int(input())  # vložte do konzole hodnotu 10
# num2 = float(input("Enter a number:\n"))  # vložte do konzole hodnotu 2

# result = num / num2
# result2 = 5 + 6 / 2
# print(result)
# print(result2)

# ##### Úkol - Prozkoumej kód
# # Co bude vytištěno do konzole po provedení příkazu na řádku 5? 
# # Odpověď:desetinné číslo 5.0


# (temperature - 32) * 5/9

# temperature= float(input("zadej stupně farhainta které chceš přepočítat na stupne celsia\n"))
# calculation= (temperature -32)*5/9
# print("výsledná teplota je " +str(calculation)+" stupně celsia")


# Kalkulačka


# value1=int(input("vlož číslo\n"))
# value2=int(input("vlož číslo\n"))

# součet= value1 + value2
# print(součet)
# minus= value1 - value2
# print(minus)
# součin= value1 * value2
# print(součin)
# dělení= value1 / value2
# print(dělení)ˇ


# výpočet BMI

# height=int(input("zadej svou výšku v centimetrech\n"))

# weight= float(input("zadej svou váhu\n"))

# height= height / 100
# BMI= weight/height**2
# # BMI= round(BMI,2)

# if BMI <= 18.5 :
#  print ("Tvé BMI je " + str(BMI) + "Máte podváhu ")


# elif BMI <=24.9:
#  print ("Tvé BMI je " + str(BMI) + "jste v normě ")

# elif BMI<= 29.9:
#  print ("Tvé BMI je " + str(BMI) + " Máte nadváhu" )

# elif BMI<=34.9:
#  print ("Tvé BMI je " + str(BMI) + "Máte obezitu prvního stupně")

# # print ("tvé bmi je " + str (BMI))


# # převod cm/m

# delka=float(input("zadej delku v centimetrech\n"))
# delka = delka/100
# print(delka)





# nespouštějte program!
# jaké tři řetězce se podle vás vytisknou do konzole? 
# vaši předpověď napište do komentářů níže


age = 18 

if age == 18:
    print("You are old enough!") 
    #  tento print se vytiskne

num1 = 1337
 
if num1 == 10: 
    print("This text is output because the condition was true!")    
else:
    print("This text is output because the condition was false!") 
    # vytiskne se false

print("This part is always printed!")
# toto se vytiskne vždy
