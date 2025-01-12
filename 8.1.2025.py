def proverb ():
    sentence="""Don't compare yourself with anyone in this world… you do so, you are insulting yourself."""
    print (sentence)
proverb ()


# def zobraz_suda_cisla(a, b):
#     suda = a
#     lycha = b
    
#     for i in range(suda, lycha +1):
#         if i % 2 == 0:  # Zkontrolujeme, zda je číslo sudé
#             print(i)

# zobraz_suda_cisla(3, 10)


# def vytiskni_ctverec(delka, symbol, plny):
#     if plny:
#         # Vytiskni plný čtverec
#         for i in range(delka):
#             print(symbol * delka)
#     else:
#         # Vytiskni prázdný čtverec
#         for i in range(delka):
#             if i == 0 or i == delka - 1:
#                 print(symbol * delka)  # Horní a dolní řádek
#             else:
#                 print(symbol + ' ' * (delka - 2) + symbol)  # Střední řádky

# # Příklad použití
# vytiskni_ctverec(5, '*', True)  # Plný čtverec
# print()  # Mezera mezi čtverci
# vytiskni_ctverec(5, '-', False)  # Prázdný čtverec


# def cislo(a, b, c, d, e, ):
#     return min(a, b, c, d, e )

# # Příklad použití
# nejmensi_cislo = cislo(5, 3, 9, 1, 7, )
# print(f"Nejmenší číslo je: {nejmensi_cislo}")





# def pocet_cislic(cislo):    
#     cislo= len(str(cislo))
#     return cislo

# cislo = (77864)

# print(f"Počet číslic v čísle {cislo} je: {pocet_cislic(cislo)}")



# def soucin_v_rozsahu(start, konec):
#     # Prohození hodnot, pokud je start větší než konec
#     if start > konec:
#         start, konec = konec, start
    
#     soucin = 1
#     for cislo in range(start, konec + 1):
#         soucin *= cislo
    
#     return soucin

# # Příklad použití
# print(soucin_v_rozsahu(5, 25))  # Vrátí součin čísel od 5 do 25
# print(soucin_v_rozsahu(25, 5))  # Také vrátí součin čísel od 5 do 25
# # S tímto ukolem jsem si nevěděl vubec rady musel jsem si na pomoc vzít AI :-)


# def palindrom(cislo):
#     cislo=str(cislo)
    
#     return cislo == cislo[::-1]


# print(palindrom(123321))  
# print(palindrom(421987))  






 







