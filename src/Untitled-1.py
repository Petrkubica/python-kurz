# try:
#   pocet = 30
#   mnozstvi = int(float(input('zadej mnozstvi ')))
#   pomer = pocet/mnozstvi
# except ValueError:
#   print('zadej cislo jako int')
# except ZeroDivisionError:
#   print('deleni nulou nelze')

# # 
# name= input("zadej sve jmeno")
# print(name)

# print(" vítejte v aplikaci na generování vtipných jmen ")
# name= input("Jaké je tvé křestní jmeno\n")
# print("Jaká je tvá tipická vlastnost? Napiš ji Velkým písmem")
# vlastnost=input("")
# print("tvé vtipné jméno je" +" "+ name +" "+ vlastnost )


# dvoumístne_číslo=input("zadej dvoumístné číslo\n")
# first_number=int(dvoumístne_číslo[0])
# second_number=int(dvoumístne_číslo[1])
# print(first_number+second_number)
# print(type (first_number))
# print(type(dvoumístne_číslo))

# váha=input("zadej svoji váhu\n")
# výška=input("zadej svoji výšku v metrech\n")
# BMI=int(váha) / (float(výška)*float(výška))
# BMI=int(BMI)
# print("Vaše BMI je:" + str(BMI))

# print("vítejte v kalkulačce plateb")
# cena= int(input("kolik máte zaplatit? \n"))
# tuzer=int(input("kolik chcete dát spropitné v %\n"))
# rozdělení=int(input("mezi kolik lidí se má rozdělit částka? \n"))

# one_payment=(cena + (cena*tuzer/100)) / rozdělení
# print(f"Každý člověk musí zaplatit \n{one_payment}")

# zadane_slovo = input(f'zadej slovo ktere chces vypsat: ')
# for i in zadane_slovo:
#     print(i)
# multi=1
# sum = 0
# for _ in range(3):
#     vstup = int(input(f'zadej vstupni cislo: '))
#     sum +=vstup
#     sum = sum + vstup
#     multi *= vstup
# print(f'soucet vsech cisel je {sum} a jejich soucint je {multi}')


# y = 6

# z = 2

#     for x in range(4):

#     y = x + y + z

#      print(x, y, z)
 
#     for x in [3, 7, 10]:

#     print(x)

# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("nemužeš dělit nulou")
# else:
#     print(f"Výsledek:{result}")

# text =("Nesrovnávej se s nikým na tomto světě...\npokud tak učiníš, urážíš sám sebe.")
# autor = "Bill Gates"
    
# print=(text)
# print= (autor)
# Požádejte uživatele o zadání dvou celých čísel
# x = int(input("Zadejte celé číslo x: "))
# y = int(input("Zadejte celé číslo y: "))

# # Vypočítání x umocněného na y
# vysledek = x ** y

# # Vypsání výsledku
# print(f"Výsledek {x} umocněné na {y} je: {vysledek}")



# zadane_slovo = input(f'zadej slovo ktere chces vypsat: ')
# for _ in zadane_slovo:
#     print(_)
# multi=1
# sum = 0
# for _ in range(3):
#     vstup = int(input(f'zadej vstupni cislo: '))
#     sum +=vstup
#     sum = sum + vstup
#     multi *= vstup
# print(f'soucet vsech cisel je {sum} a jejich soucint je {multi}')
# multi2=1
# sum2 = 0
# answer='ano'
# while answer.lower()=='ano':
#     vstupni_cislo = int(input(f'zadej cislo na soucet/soucin: '))
#     sum2 +=vstupni_cislo
#     multi2 *= vstupni_cislo
#     answer = input(f'chces pokracovat (ano/ne) ')
# print(f'soucet vsech cisel je {sum2} a jejich soucint je {multi2}')




# # Výpočet počtu čísel v daném rozsahu
# end=11000
# start=100
# print end + start 

# # Výpis výsledku
# print(f"Počet čísel od {start} do {end} je: {pocet_cisel}")

# count = 0


# for number in range(100, 1000):
#     str_number = str(number)
    
#     a = str_number[0]  
#     b = str_number[1]  
#     c = str_number[2]  
    
#     if a == b or a == c or b == c:
#         count += 1

# print("Počet celých čísel v rozsahu od 100 do 999, která mají dvě stejné číslice: \n" , count)

car_speed = 100
if car_speed > 50:
    print("Car is faster than 50 km/h")