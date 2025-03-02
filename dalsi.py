# def soucin_prvku(seznam):  
#     soucin = 1  
#     for cislo in seznam:  
#         soucin *= cislo  
#     return soucin  

# seznam_cisle = [2, 4, 6, 8]  
# vysledek = soucin_prvku(seznam_cisle)  
# print(vysledek) 
print ("banana")
print ("pomerange")
print ("blue")
print ("grass")
print ("tree")
print ("market")

# def najdi_minimum(seznam):  
#     if not seznam:  
#         return None  

#     minimum = seznam[0]  
#     for cislo in seznam:  
#         if cislo < minimum:  
#             minimum = cislo 
#     return minimum  


# seznam_cisle = [5, 2, 9, 8, 6]  
# vysledek = najdi_minimum(seznam_cisle)  
# print(vysledek)  


# def odstran_cislo(seznam, cislo):  
#     pocet_odstranenych = 0 


#     while cislo in seznam:  
#         seznam.remove(cislo)  
#         pocet_odstranenych += 1  

#     return pocet_odstranenych  


# seznam_cisle = [5, 2, 3, 2, 6, 2]  
# cislo_k_odstraneni = 2
# vysledek = odstran_cislo(seznam_cisle, cislo_k_odstraneni)  
# print(vysledek)  
# print(seznam_cisle)  


# dictionary
animals = {
    "kocka": "cat",
    "pes": "dog",
    "kralik": "rabbit",
    "kun": "horse",
    "mys": "mouse"
}
# Animals with translation
# print("cz en Animals:")
for cz, en in animals.items():
    print(f"{cz} -> {en}")
# find animal
search = input("\nZadej český název zvířete: ").strip()
# proc strip() a pri vyvoji zda pouzit input
if search in animals.keys():
    print(f"Anglický překlad pro '{search}' je '{animals[search]}'.")
else:
    print(f"Zvíře '{search}' nebylo nalezeno.")