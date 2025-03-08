print ("Vítejte v jednoduché kalkulačce spotřeby ")


vypocet= {}

def vypocitej_m2():
    sirka=float(input("Vlož šířku"))
    delka=float(input("Vlož délku"))
    m2=sirka*delka
    return m2

def vypocitej_m3():
    sirka=float(input("Vlož šířku"))    
    delka=float(input("Vlož délku"))
    výška=float(input("Vlož výšku 'hloubku'"))
    m3= sirka*delka*výška
    return m3

while True:
    
    choice=input("vyberte  m2 - m3\n ")
    if choice == "m2":
        výsledek_m2=vypocitej_m2()
        print(f"Plocha místnosti kterou chcete opravit má {výsledek_m2} m2. To je dobrý začátek pro výpočet spotřeby materiálu")
    elif choice== "m3":
        výsledek_m3=vypocitej_m3 ()
        print(f"{výsledek_m3}")

    else:
     print("neplatná volba")    
     break

dotaz =input("Co budete rekonstruovat")

def výmalba ():
  výmalba = input ("Budete požívat bílou standartní barvu nebo tonovanou barvu? \n zadej standartní / tonovanou \n doporučuji jak první nátěr zvolit penetraci ")
  
  
  výmalba == "standartni"
  if výmalba:
   výpočet= výsledek_m2* 0.12 #výpočet bílé bavy 
   výpočet_penetrace=výsledek_m2*0.13 # výpočet penetrace
   print (f"spotřeba standartní malířské barvy na vámi zadané hodnoty {výsledek_m2} m2 je {výpočet} l. Spotřeba je počítaná v jedné vrstvě ,avšak se vždy doporučeje vymalovat minimálně ve dvou vrstvách.spotřeba je tedy nutná vynásobit počtem vrstev\n Spotřeba penetrace {výpočet_penetrace}l ")

  elif výmalba =="tonovana":
   výpočet_barevne= výsledek_m2 *0.14 # výpočet tonované barvy
   výpočet_penetrace=výsledek_m2*0.13 # výpočet penetrace
   print(f"spotřeba standartní malířské barvy na vámi zadané hodnoty {výsledek_m2} m2 je {výpočet_barevne} l. Spotřeba je počítaná v jedné vrstvě ,avšak se vždy doporučeje vymalovat minimálně ve dvou vrstvách.spotřeba je tedy nutná vynásobit počtem vrstev\n Spotřeba penetrace {výpočet_penetrace}l ")

     
     
def jemná_omítka ():   
    jemna_omitka = výsledek_m2 * 7.5
    print (f"Na vámi zadané parametry {výsledek_m2} m2 je potřeba počítat se spotřebou {jemna_omitka} kg jemné vápenné omítky,podobná spotřeba je i u vápenocementové omítky spotřeba je počítaná na 0,5 cm na 1m2 ")


def hrubá_omítka ():
   jádrová_omítka = výsledek_m2 * 16.5
   print (f"Na vámi zadané arametry {výsledek_m2} m2 je spotřeba jádrové omítky {jádrová_omítka} kg. Spotřeba je počítáná na 1cm hrubé omítky na 1m2. V případě větší vrstvy je potřeba spotřebu znásobit ") 


def podlaha ():
    procenta = výsledek_m2 /100 *10
    pokladka= výsledek_m2 + procenta
    lišta1=input("zadejte délku jedné strany")
    lišta2=input("zadejte délku druhé strany ")
    obvodová_lišta= lišta1+lišta2+lišta1+lišta2


    print (f"na vámi zadané parametry je potřeba {pokladka} m2 podlahy. Podlaha je počítaná s 10 % podlahové krytiny navíc z důvodu prořezu'odpadu'.")
    print(f"Budete potřebovat {obvodová_lišta} m/b obvodové lišty.\n Obvodová lišta se většinou oridává po 2,5 m/b")


def sadrokarton_strop ():
   sdk= výsledek_m2 *0.10
   sdk1= sdk + výsledek_m2
   profil_cd= výsledek_m2*3.2
   profil_ud1=input("zadejte délku místnosti")  
   profil_ud2=input("zadejte šířku místnosti")
   profil_ud= profil_ud1+profil_ud2 #metry běžné
   šrouby_stropní = výsledek_m2 * 1.3
   tmel= výsledek_m2 * 1
   srouby_tn= výsledek_m2 * 18



   while True:

    print("\n1. Výmalba místnosti")
    print("2.výpočet pro jemné omítky ")
    print("3. výpočet pro hrubé omítky ")
    print("4. pokládka podlahy ")
    print("5. sadrokarton")
    

    choice= ("zadej výběr 1 - 5 ")

    





