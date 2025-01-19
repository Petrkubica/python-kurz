# import random

# names=input("napiš jména všech co budou platit a odděl je čarkou\n")

# list_people=names.split (",")
# random_number = random.randint(0, len(list_people)-1)

# print (f"{list_people[random_number]} bude dnes platit učet")


# def secti (a,b):
#  return  a+b
# resume=secti(5,3)
# print(resume)

# ˇ

# def sečti(a,b):
#     return a+b
# výsledek=8+7
# print(výsledek)


# def obsah_obdelníku(a,b):
#     return a*b
# delka=int(input("vlož délku obdelníku"))
# šířka=int(input("vlož šířku obdelníku"))
# výsledek= obsah_obdelníku (delka,šířka)
# print (f"obsah je {výsledek}")

a = (1, 2, 3, 4)  
b = (3, 4, 5, 6)  
c = (4, 6, 3, 8)  

 
společné_prvky = set(a) & set(b) & set(c)  

print("Přítomné prvky ve všech množinách:",společné_prvky)

a = (1, 2, 3, 4)  
b = (3, 4, 5, 6)  
c = (5, 6, 7, 8)  

jedinečne_cislo_a = set(a) - set(b) - set(c)  
jedinečne_cislo_b = set(b) - set(a) - set(c)  
jedinečne_cislo_c = set(c) - set(a) - set(b)  


print("Jedinečné číslo v a:", jedinečne_cislo_a)  
print("Jedinečné číslo v b:", jedinečne_cislo_b)  
print("Jedinečné číslo v c:", jedinečne_cislo_c)






množina1 = (1, 2, 3, 4, 5)  
množina2 = (1, 2, 0, 4, 5)  
množina3 = (1, 2, 3, 4, 0)  
 
stejné_číslo = []  
for i in range(len(množina1)):  
    if množina1[i] == množina2[i] == množina3[i]:  
       stejné_číslo.append(množina1[i])  

print("Stejné čísla na stejné pozici:", stejné_číslo)