import random

names=input("zadej všechny jména oddělené čárkou\n")
seznam=names.split(",")
náhodné_jméno=random.randint(0, len(seznam)-1)
print(f"{seznam [náhodné_jméno] } bude ndes platit")


# import random
# names= input("Napiš seznam jmen oddělených čárkou\n")

# list_people = names.split(",")
# random_number= random.randint(0, len(list_people)-1)

# print(f"{list_people[random_number]} dnes bude platit")