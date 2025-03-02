# class book:
#     def __init__(self ,název , autor, rok_vydání , počet_stran):
#         self.název = název
#         self.autor=autor
#         self.rok_vydání = rok_vydání
#         self.počet_stran = počet_stran

#     def info(self):
#         return f" {self.název} od {self.autor} ({self.rok_vydání}), {self.počet_stran} stran"
    
#     def __str__ (self):
#         return f" {self.název} od {self.autor} ({self.rok_vydání}), {self.počet_stran} stran"
    
#     def je_dlouha (self):
#         return self.počet_stran > 500
    
# moje_kniha = book  ("pán prstenu", "JRR . Tolkien",1945 , 1178)

# kniha1=book ("1984", "George Orwell", 1949, 328)


# print ("test metody info():")
# print (kniha1.info())
# print (moje_kniha.info())



# print("Test metody __str__")
# print (kniha1.info())
# print(moje_kniha.info())

# print ("\n Test metody je_dlouhá():")
# print (f" je 'pán prstenů' dlohá kniha? {kniha1.je_dlouha()} ")
# print (f"je 'malý princ'dlouhá kniha? {moje_kniha.je_dlouha()}")





# class bankovní_učet:
#     def __init__ (self,cislo_uctu , Jmeno_majitele , zustatek):
#         self.cislo_uctu = str(cislo_uctu)
#         self.Jmeno_majitele = str(Jmeno_majitele)
#         self.zustatek = float(zustatek)

#     def vklad (self, castka):
#         self.zustatek  += castka
        
    

#     def vyber (self ,castka):
#         if self.zustatek >= castka:
#             self.zustatek -= castka

#         else:
#             print("nedostatek finančních prostředku na účtu")        


#     def zustatek(self):
#         return self.zustatek


#     def __str__ (self):
#         return f"Účet číslo {self.cislo_uctu} patřící {self.Jmeno_majitele} má zustatek {self.zustatek} KČ"       



# muj_ucet = bankovní_učet("2074701001/5500" ,"Petr Kubica" , 25382 )
# print(muj_ucet)

# muj_ucet.vklad (500)
# print("Po vkladu 500 Kč")
# print(muj_ucet)

# muj_ucet.vyber (30000)
# print("Po výběru 30000 Kč")
# print(muj_ucet)

# import datetime

# class auto:
#     def   __init__(self,znacka, model, rok_výroby, najeto, spotreba):
#         self.znacka= str(znacka)
#         self.model=str(model)
#         self.rok_výroby=int(rok_výroby)
#         self.najeto=float(najeto)
#         self.spotreba=float(spotreba)

#     def jizda (self, vzdálenost):
#         self.najeto+= vzdálenost

#     def tankovaní (self,litry):
#          return (litry / self.spotreba) * 100 
    
#     def stari(self):
#         aktualni_rok = datetime.datetime.now().year
#         return aktualni_rok - self.rok_výroby

#     def __str__(self):

#         return f"Auto značky{self.znacka} modelové řady {self.model} rok výroby {self.rok_výroby} má najeto{self.najeto} km  spotřeba {self.spotreba} l/100km"  



# moje_auto = auto("Citroen", "Jumpy", 2015, 206879, 9.8)
# print(moje_auto)
# moje_auto.jizda(100)
# print(f"Po jízdě 100 km: {moje_auto.najeto} km")
# print(f"S 50 litry ujede: {moje_auto.tankovaní(50):.2f} km")
# print(f"Stáří auta: {moje_auto.stari()} let") 




# class Knihovna:
#     def __init__ (self, nazev_knihovny , seznam_knih):
#         self.nazev_knihovny=str(nazev_knihovny)
#         self.seznam_knih=[seznam_knih]

#     def pridat_knihu(self, nazev_knihy , autor) :
#         self.nazev_knihy=str(nazev_knihy)
#         self.autor=str(autor)


#     def odstranit_knihu(self,nazev):    
#         self.nazev=str(nazev)

#     def najit_knihu(self,nazev):
#         self.nazev=str(nazev)

#     def pocet_knih():
#         return
        
#     def __str__ (self):
#         return f"Jméno knihovny {self.nazev_knihovny} a seznam knih je {self.seznam_knih} "
    
# moje_knihovna=Knihovna("Jaromír Erben", "Kytice")
# print (moje_knihovna)



# class Kniha:
#     def __init__(self, nazev, autor):
#         self.nazev = nazev
#         self.autor = autor
#         self.vypujcena = False

#     def __str__(self):
#         return f"{self.nazev} od {self.autor}"

# class Knihovna:
#     def __init__(self, nazev_knihovny):
#         self.nazev_knihovny = nazev_knihovny
#         self.seznam_knih = []

#     def pridat_knihu(self, nazev, autor):
#         kniha = Kniha(nazev, autor)
#         self.seznam_knih.append(kniha)

#     def odstranit_knihu(self, nazev):
#         self.seznam_knih = [k for k in self.seznam_knih if k.nazev != nazev]

#     def najit_knihu(self, nazev):
#         for kniha in self.seznam_knih:
#             if kniha.nazev == nazev:
#                 return kniha
#         return None

#     def pocet_knih(self):
#         return len(self.seznam_knih)

#     def vypujcit_knihu(self, nazev):
#         kniha = self.najit_knihu(nazev)
#         if kniha and not kniha.vypujcena:
#             kniha.vypujcena = True
#             return True
#         return False

#     def __str__(self):
#         knihy = ", ".join(str(kniha) for kniha in self.seznam_knih)
#         return f"Knihovna {self.nazev_knihovny} obsahuje knihy: {knihy}"

# # Testování
# moje_knihovna = Knihovna("Městská knihovna")
# moje_knihovna.pridat_knihu("Kytice", "Karel Jaromír Erben")
# moje_knihovna.pridat_knihu("Babička", "Božena Němcová")
# print(moje_knihovna)
# print(f"Počet knih: {moje_knihovna.pocet_knih()}")
# moje_knihovna.vypujcit_knihu("Kytice")
# print(moje_knihovna.najit_knihu("Kytice"))
# moje_knihovna.odstranit_knihu("Babička")
# print(moje_knihovna)

import json

# Vytvoření slovníku (který bude převeden na JSON)
kniha = {
    "titul": "Hobit",
    "autor": "J.R.R. Tolkien",
    "rok_vydani": 1937,
    "postavy": ["Bilbo", "Gandalf", "Smaug"],
    "fantasy": True
}

# Serializace do JSON řetězce
json_string = json.dumps(kniha, indent=4)
print("JSON řetězec:")
print(json_string)

# Zápis do souboru
with open("kniha.json", "w") as f:
    json.dump(kniha, f, indent=4)
print("\nData byla zapsána do souboru 'kniha.json'")

# Čtení ze souboru
with open("kniha.json", "r") as f:
    nactena_kniha = json.load(f)

print("\nNačtená data ze souboru:")
print(json.dumps(nactena_kniha, indent=4))

# Přístup k datům
print(f"\nTitul knihy: {nactena_kniha['titul']}")
print(f"První postava: {nactena_kniha['postavy'][0]}")
