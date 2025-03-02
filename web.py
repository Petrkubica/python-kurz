# video_games = ["Mario", "Sonic", "Joust", "Zelda"]
# game_position= int(input("Zadej číslo mezi 0-3\n"))
# print ("hra na pozici " + str(game_position) + " je " + video_games[game_position])

# hra= input("vlož název hry\n")
# if hra in video_games:
#     print(hra + "byl již v seznamu ,již byl vymazán")

#     video_games.remove(hra)

# else:
#     print(hra + "hra ještě nebyla v seznamu tak byla přidána")    
#     video_games.append(hra)



# arms = ["samopal" , "nůž" , "meč" , "výbušnina"]
# zombie_weakness=("nůž")
# print ("setkal jsi se se zombie, měl by jsi se připravit na boj ")
# print ("tady je seznam zbraní které mužeš použít\n 'samopal','nůž', 'meč' , 'výbušnina' ")
# choos= input ("Jestli chete použít zbraň ze seznamu zadejte '1' , jestli chcete vlastní zbraň zadejte '2'\n" )
# zbrane=[]
# my_chose=[]
# vlastni_zbran=[]
# zbran=[]

# if choos == ("1"):
#     zbran = (input ("zadej svuj výběr\n"))
#     zombie_weakness== zbran("nůž")
#     print ("vyhrál jsi boj")
#     zbrane.append (zbran)
   
# elif zombie_weakness!="nůž"   :
#     print("zdárně bojuješ")






    



# elif choos==("2"):
#     vlastni_zbran=[input("zadej s jakou zbraní budes bojovat dle vlastního výběru\n")]
#     my_chose.append(vlastni_zbran)
#     #my_chose==zombie_weakness
#     print (f"tvuj výběr je " + str( my_chose) + "Hodně štěstí")

# # else:my_chose =="nůž"
# # print ("Vyhrál jsi boj ")
    

# shop_list=["káva", "víno", "kola" ]


# shop_list.append("kofola")

# shop_list.remove("víno")
# shop_list[0]= "caj"
# number=len(shop_list)
    
# print (shop_list)
# print(number)



# students=[["Frederik",1.5],["František", 2.3],["Lenka",1.2]]

# choos=input("Chces přidat nebo odebrat studenta ? \nPro přidání zadej 1,\n  pro odebrání zadej 2\n")


# if choos =="1":
#     new_students=[input("vlož jméno studenta a jeho známku\n")]
#     students .append(new_students)

# elif choos== "2" :
#     delete_student=[input("Zadej jméno žáka kterého chceš odstranit\n")]
#     students.remove(delete_student)

    

# print (students)


# Inicializace seznamu studentů
# studenti = [
#     ["Jan Novák", 1.5],
#     ["Eva Svobodová", 2.0],
#     ["Petr Dvořák", 1.0]
# ]

# def pridat_studenta():
#     jmeno = input("Zadejte jméno studenta: ")
#     znamka = float(input("Zadejte známku studenta: "))
#     studenti.append([jmeno, znamka])
#     print(f"Student {jmeno} byl přidán.")

# def odstranit_studenta():
#     jmeno = input("Zadejte jméno studenta k odstranění: ")
#     for student in studenti:
#         if student[0] == jmeno:
#             studenti.remove(student)
#             print(f"Student {jmeno} byl odstraněn.")
#             return
#     print(f"Student {jmeno} nebyl nalezen.")

# def vypsat_studenty():
#     for student in studenti:
#         print(f"{student[0]}: {student[1]}")

# def prumerna_znamka():
#     if not studenti:
#         print("Seznam studentů je prázdný.")
#         return
#     prumer = sum(student[1] for student in studenti) / len(studenti)
#     print(f"Průměrná známka: {prumer:.2f}")

# def nejlepsi_student():
#     if not studenti:
#         print("Seznam studentů je prázdný.")
#         return
#     nejlepsi = min(studenti, key=lambda x: x[1])
#     print(f"Nejlepší student: {nejlepsi[0]} se známkou {nejlepsi[1]}")

# while True:
#     print("\nVyberte operaci:")
#     print("1. Přidat studenta")
#     print("2. Odstranit studenta")
#     print("3. Vypsat studenty")
#     print("4. Vypočítat průměrnou známku")
#     print("5. Najít nejlepšího studenta")
#     print("6. Ukončit program")
    
#     volba = input("Zadejte číslo operace: ")
    
#     if volba == "1":
#         pridat_studenta()
#     elif volba == "2":
#         odstranit_studenta()
#     elif volba == "3":
#         vypsat_studenty()
#     elif volba == "4":
#         prumerna_znamka()
#     elif volba == "5":
#         nejlepsi_student()
#     elif volba == "6":
#         print("Program ukončen.")
#         break
#     else:
#         print("Neplatná volba. Zkuste to znovu.")




# studenti=[]

# def pridej_studenta ():
#     jmeno= input("zadej jmeno studenta")
#     znamka=input (float("zade známku"))
#     studenti.append([jmeno,znamka])
#     print(F"student {jmeno} byl přidán do seznamu")

# def vypsat_studenty ():
#     for jmeno , znamka in studenti:
#         print(f"{jmeno}:{znamka}")    

# def prumerná_známka ():
#     if not studenti:
#         print ("seznam studentu je prázdný")        

#         return
#     prumer= sum (znamka for _, znamka in studenti) / len (studenti)
#     print (f"Pruměrná známka: {prumer:.2f}")
     
# if  __name__ == "__mine__":
    
#     while True :
#         print("\n1 přidat studenta")
#         print("2 vypsat studenty")
#         print("3 Průměrná známka")
#         print("4 konec programu")

#         volba= input("zadej svuj výběr 1-4")


#         if volba == "1":
#             pridej_studenta()

#         elif volba == "2":
#             vypsat_studenty()    

#         elif volba == "3":
#             prumerná_známka()

#         elif volba =="4":
#           break

#         else:
#             print("neplatná volba")
                           





# studenti = []

# def pridat_studenta():
#     jmeno = input("Zadejte jméno studenta: ")
#     znamka = float(input("Zadejte známku studenta: "))
#     studenti.append((jmeno,[znamka]))
#     print(f"Student {jmeno} byl přidán.")

# def odebrat_studenta():
#     if not studenti:
#         print("Seznam studentu je prazdný")
#         return
#     jmeno = input("zadej jmeno studenta terého chceš ostranit\n")    
      
#     for student in studenti:
#         if student [0] == jmeno:
#             studenti.remove (student)
#         print (f"Student {jmeno} byl ostraněn ze seznamu")

#         return
#     print(f"student {jmeno} nebyl nalezen")  


# def vypsat_studenty():
#     if not studenti:
#         print("Seznam studentů je prázdný.")
#     else:
#         for jmeno, znamky in studenti:
#          print(f"{jmeno}: {','.join(map(str,znamky))}")
    


# def prumerna_znamka():
#     if not studenti:
#         print("Seznam studentů je prázdný.")
#         return
    
#     for jmeno ,znamky in studenti: (stud_jmeno , znamky)in enumerate (studenti):
#         prumer = sum(znamky) / len(znamky)
            
#         print(f"Pruměrná známka  {jmeno}:{prumer:. 2f} byla přidána studentovi {jmeno}")
            



# def pridat_znamku():
#     if not studenti:
#         print("Seznam studentů je prázdný.")
#         return
#     jmeno = input("Zadejte jméno studenta, kterému chcete přidat známku: ")
#     for i, (stud_jmeno, _) in enumerate(studenti):
#         if stud_jmeno == jmeno:
#             nova_znamka = float(input(f"Zadejte novou známku pro {jmeno}: "))
#             studenti[i] = (jmeno, nova_znamka)
#             print(f"Známka pro {jmeno} byla aktualizována na {nova_znamka}")
#             return
#     print(f"Student {jmeno} nebyl nalezen v seznamu.")


# # Hlavní část programu
# if __name__ == "__main__":
#     while True:
#         print("\n1. Přidat studenta")
#         print("2. odebrat studenta")
#         print("3. Vypsat studenty")
#         print("4. Průměrná známka")
#         print("5. přidat známku ")
#         print("6. Konec")
        
#         volba = input("Vyberte akci (1-6): ")
        
#         if volba == "1":
#             pridat_studenta()
#         elif volba== "2":
#             odebrat_studenta()    
#         elif volba == "3":
#             vypsat_studenty()
#         elif volba == "4":
#             prumerna_znamka()
#         elif volba == "5":
#             pridat_znamku()
#         elif volba == "6":
#             print("konec programu")    
#             break
#         else:
#             print("Neplatná volba.")




studenti = []

def pridat_studenta():
    jmeno = input("Zadejte jméno studenta: ")
    znamka = float(input("Zadejte známku studenta: "))
    studenti.append((jmeno, [znamka]))
    print(f"Student {jmeno} byl přidán.")

def odebrat_studenta():
    if not studenti:
        print("Seznam studentů je prázdný")
        return
    jmeno = input("Zadej jméno studenta, kterého chcete odstranit: ")    
    for student in studenti:
        if student[0] == jmeno:
            studenti.remove(student)
            print(f"Student {jmeno} byl odstraněn ze seznamu")
            return
    print(f"Student {jmeno} nebyl nalezen")  

def vypsat_studenty():
    if not studenti:
        print("Seznam studentů je prázdný.")
    else:
        for jmeno, znamky in studenti:
            print(f"{jmeno}: {', '.join(map(str, znamky))}")

def prumerna_znamka():
    if not studenti:
        print("Seznam studentů je prázdný.")
        return
    for jmeno, znamky in studenti:
        prumer = sum(znamky) / len(znamky)
        print(f"Průměrná známka {jmeno}: {prumer:.2f}")

def pridat_znamku():
    if not studenti:
        print("Seznam studentů je prázdný.")
        return
    jmeno = input("Zadejte jméno studenta, kterému chcete přidat známku: ")
    for i, (stud_jmeno, znamky) in enumerate(studenti):
        if stud_jmeno == jmeno:
            nova_znamka = float(input(f"Zadejte novou známku pro {jmeno}: "))
            znamky.append(nova_znamka)
            print(f"Známka {nova_znamka} byla přidána studentovi {jmeno}")
            return
    print(f"Student {jmeno} nebyl nalezen v seznamu.")

# Hlavní část programu
if __name__ == "__main__":
    while True:
        print("\n1. Přidat studenta")
        print("2. Odebrat studenta")
        print("3. Vypsat studenty")
        print("4. Průměrná známka")
        print("5. Přidat známku")
        print("6. Konec")
        
        volba = input("Vyberte akci (1-6): ")
        
        if volba == "1":
            pridat_studenta()
        elif volba == "2":
            odebrat_studenta()    
        elif volba == "3":
            vypsat_studenty()
        elif volba == "4":
            prumerna_znamka()
        elif volba == "5":
            pridat_znamku()
        elif volba == "6":
            print("Konec programu")    
            break
        else:
            print("Neplatná volba.")
