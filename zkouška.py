# výška = input("zadej svou výšku v metrech\n")
# hmotnost = input("zadej svou váhu\n")

# bmi = int(hmotnost) / float(výška)**2
# bmi = int(bmi)
# print("Váš BMI je: " + str(bmi))


# age=int(input("kolik je ti let?\n"))
# remain = 90 - age
# months = 12 * remain
# weeks = 52 * remain
# days = 365 * remain
# print(f"Dokonce tvého života ti zbývá\n  {remain} let\n {months} měsíců\n  {weeks} týdnů\n {days} dnů\n")

# check=int(input("Kolik máte zaplatit?\n"))
# tip=int(input ("kolik chcete dát dýško v %\n"))
# people=int(input("Mezi kolik lidí se má platba rozdělit?\n"))
# sum=(check/100) 
# price=(sum*tip)
# together=(price + check)
# partition=(together/people)
# finaly_payment="{:.2f}".format(partition ,2)
# print (f"každý máte zaplatit {finaly_payment} kč")ˇ

# age=int(input("Zadej svůj věk "))

# if age >= 18:
#     print("mužete řídit auto a pít alkohol")

# else:
#     print(" je mi líto ,jste jestě dítě")

# print ("Vítejte v online nákupu lístku do kina")
# print("Lístek pro dospělého stojí 150 Kč")
# print("lístek pro studenta sojí 120 kč")
# ticket=(input("jste student?\n"))

# if ticket == "ano":
#    print("tvuj lístek stojí 120 kč")

# else: 
    #  print("tvuj lístek stojí 150 kč")

# Podmínky - normal, smart, extrasmart
# type = input("Jaký chcete typ mobilního telefonu? Možnosti: normal, smart, extrasmart\n")


# if type != "normal":
#     print(f"Cena telefonu typu {type} je 25.000 Kč")
# else:
#     print(f"Cena telefonu typu {type} je 15.000 Kč")

# height=int(input("zadej svou váhu\n"))
# if height >= 87:
#     print('Můžete jet na horské dráze.')

#     age = int(input('Jaký je váš věk?\n'))
#     if age < 12:
#         print('Cena vašeho lístku je 50 Kč.')
#     elif age >=12 and age <=18:
#         print('Cena vašeho lístku je 100 Kč.')
#     else:

#         print('Cena vašeho lístku je 150 Kč.')
        
#     weight = int(input('Jaká je váše váha?\n'))
#     if weight >= 100:
#         print('Lístek ti prodáme, ale seš MACEK a na horskou dráhu nemůžeš!')
#     else:
#         print('Lístek ti prodáme, a na horskou dráhu můžeš!')
    
# else:
# #     print('Omlouváme se, ale na horské dráze jet nemůžete.')


# print(len("násobení je prima"))

# print("Vítejte na horské dráze")
# height=int(input("zadejte vaši výšku v cm\n"))
# bill=0

# if height >85:
#    print("vítej na horské dráze")

#    weight=int(input("Zadej svoji váhu\n"))

#    if weight>100:
#       print("Vítej ,ale bohužel nemužeš jet")
#    print("Vítej ale bohužel nemužeš jet")
#    age=int(input("zadej svuj věk\n"))
#    if age<12:
#       bill=50
#    print("máš dětskou vstupenku za 50 kč")

   
# elif  age <18:
     
# bill=100
# print("maš studentskou vstupenku za 100 kč")
# else
# bill=150
# print("tvá vstupenka stojí 150 kč")

# photo=input("Chces vyfotit na horské dráze? odpověz ano nebo ne\n")
# if photo=="ano":
#    bill+=50
#    print(f"(Tvá celková cena je {bill} kč")


# else:print('Omlouváme se, ale na horské dráze jet nemůžete.')
    
# print("Vítejte na horské dráze")
# height=int(input("zadej svou výšku\n"))
# bill=0

# if height >85:
#     print("užij si svou jízdu" )


#     weight=int(input("zadej svou váhu\n"))
#     if weight <120:
#         print("pokračuj dále")
#     else:
#         print("Lístek si koupit mužeš ale nemužeš s námi jet. Sory")

#     age=int(input("zadej svuj věk\n"))    
#     if age <12:
#          bill=50
#          print("Tvuj lístek stojí 50 Kč")
#     elif age<18:
#          bill=100
#          print("tvuj lístek stojí 100 kč")
#     else:
#          bill=150
#          print("Tvuj lístek stojí 150 kč") 

#     photo= input("Chces se vyfotit? odpověz ano nebo ne\n ")
#     if photo == "ano":
#         bill+=50
#         print("Máš to o pade dražší")
#         print(f"celková cena je {bill} kč")
#     else:
#         print(f"právě jsi ušetřil pade\n tvá cena je {bill}kč")
# else:
#  print("Bohužel nemužeš jet")


# Výpočet BMI

# height=int(input("zadej svou výšku v centimetrech\n"))
# weight=int(input("zadej svou váhu\n"))
# height=height/100
# BMI= weight/height**2
# # BMI ="{:.1f}".format(BMI)
# BMI= (round(BMI ,1))


# # if BMI <=18.5: 
# #  print (f"tvé BMI je  {BMI}")
# #  print ("nezdravá váha")

# # elif BMI  <=24.9:
# #     print (f"tvé BMI je {BMI}")
# #     print ("tvá váha je v normě")

# # elif BMI  <=29.9:
# #    print (f"Tvé BMI je {BMI}")
# #    print(" Máš nadváhu")
    


# # else: 
# #    print(f"tvé BMI je {BMI}")
# #    print("Nebezpečná nadváha")
 


# # year =int(input("zadej rok"))
# # if year % 4 == 0:
# #     print("přestupný  rok")
# #     if year % 100==0:
# #         print("přestupný rok")
# #         if year % 400==0:
# #          print ("přestupný rok" )

# # else:
# #     print("rok přestupný není")    


# print("vítejte v aplikaci na objednání pizzi")
# print(input("jakou pizu chceš?  S , M , L\n"))
# bill=0
# if "S":
  
#   print ("tvá pizza stojí 100 kč")
# elif M:
     
#      print("Tvá piza stojí 150 kč")
# else:
#          bill=200
#          print ("Tvá pizza stojí 200 kč")

# print(input("chceš feferonky naví? ano / ne "))
# if "ano":
#     bill+=40
#     print(f"máš to o 40 kč dražší")
# else:
#     print(f" ušetřil jsi 40 kč")

# print("Chces navíc sýr ? ano / ne ")  
# if "ano":  
#     bill+=15
#     print (f"To bude dalších 15 kč")
# else:
#     print("zase jsi ušetřil")

# print(f"Tvá celková cena je {bill} kč")    

    


# print("vítej v objednávkové aplikaci \nJakou chceš pizzu S, M , L")
# pizza=(input("zadej velikost "))
# bill=0
# if pizza =="S":
#     print("Tvá pizza stojí 100 kč")
#     bill=100
# elif pizza =="M":
#     print("Tvá pizza stojí 150 kč")
#     bill=150
# elif pizza=="L":
#     bill=200
#     print("Tvá pizza stojí 200 kč")

# print("chceš k tomu papričky navíc? ano / ne ")
# papričky=(input(""))
# if papričky == "ano":
#     if pizza =="S":
#      bill+=20
#      print(f"máš to o 20 kč dražší")
    
#     elif pizza=="M":
#         bill+=30

#         print(f"máš to o 30 kč dražší")
#     elif pizza=="L":
#          bill+=30
#          print(f"máš to o 30 kč dražší")
# else:
#     papričky=="ne"
#     print("právě jsi ušetřil")

# print("cheš k tomu porci sýra navíc? ano / ne  ") 
# sýr= (input(""))   
# if sýr=="ano":
#     bill+=15
#     print("Dalších 15 kč")
# else:
#     sýr=="ne"
#     print("zase jsi ušetřil")

# print(f"Tvá celková cena je {bill} kč")    


# číslo=(int(input("zadej cislo")))
# if číslo %2==0:
#     print ("print sudé číslo")
# else:
#     print("liché číslo")

 
# txt = "vítej v džungli"

# x = txt.split()

# print(x)




# fruits = ["apple", "banana", "cherry"]

# x = fruits.count("cherry")

# print(x)ˇ
# def soucin_prvku(seznam):
#     if not seznam:  # Pokud je seznam prázdný
#         return 0  # nebo můžete vrátit 1, podle toho, co preferujete
#     soucin = 1
#     for cislo in seznam:
#         soucin *= cislo
#     return soucin

# vstup = input(f'zadej cisla oddelena mezerou:')
# list_cisel =vstup.split(" ")
# sum=0
# for _ in list_cisel:
#  print(_)
#  sum+=int(_)
# print(f'celkovy soucet cisel je {sum}')

# def vrat_max(*args):
#     print(args)
#     sum = 0
#     counter = 0
#     for _ in args:
#         sum +=_
#         counter+=1
#     print(f'prumer cisel je {sum/counter}')
# ˇ

# jak bohatí ledé platí v restauraci
# generování náhodné platby
import random

# pay_method=(random.randint(1,5))
# if pay_method==1:
#  print("dnes platí MILAN")
# elif pay_method==2:
#  print("Dnes platí PETR")
# elif pay_method==3:
#  print("Dnes platí DAVID")
# elif pay_method==4:
#  print("dnes platí MAREK") 
# else:
#  print("dnes platí KAREL")

