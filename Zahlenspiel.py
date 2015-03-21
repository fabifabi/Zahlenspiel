#imports
import fractions
import random
import os
import sys

#Umwandeln in Integer
def toint(wert):
     print(wert)
     try:
         wert = int(wert) 
     except:
        print("Sie muessen eine Numer eingeben")
        os.system("pause")
     print(wert)
     return(wert)

#Einstellungen Schwierigkeitsstufen
def eingabeauswerten(eingabe):
    if eingabe == 1 :
        e = 99 , 99 , 0 , 10
        return(e)
    if eingabe == 2 :
        m = 99 , 999 , 10 , 20
        return(m)
    if eingabe == 3 :
        s = 999 , 99 , 20 , 30
        return(s)
#Erstellung und loesen der Brueche        
def generator(eingabe,stufe):
     zmax,nmax,ifmin,ifmax=stufe
     anzahl = toint(eingabe)
     x = 1
     while x <= anzahl :
        
        z = random.randint(1,zmax)
        #pruefen des Schwierigkeitsgrades
        if z <= zmax :
               n = random.randint(1,99)
        else:
               n = random.randint(1,nmax)
        if z==n :
             continue
        b1 = fractions.Fraction(z, n)
        #pruefen des Schwierigkeitsgrades und kuerzen der Brueche
        bk = b1.numerator + b1.denominator
        if bk <= ifmax:
             if ifmin > bk:
                  continue
        else:
             continue
        if n == b1.denominator: #vor her: <  jetzt: >
             continue
        #Ausgabe der Brueche
        print ("Nr.",x," ",z,"/",n," Loesung: ", b1)
        x +=1
     #Neustart
     print("Program neu Starten J/N")
     pn = input()
     if pn == "J":
          start()
     if pn == "j":
          start()

        

#start
def start():
     
     print ("Wie viele Brueche sollen erstellt werden?")
     nutzer = input()
     eingabe = toint(nutzer)
     print ("Bitte waehle eine der folgenden Schwierigkeitsstufen :")
     print (" 1 fuer Einfach. 2 fuer Mittel. 3 fuer Schwer. ")
     nutzer2 = input()
     nutzer2 = toint(nutzer2)
     nutzer2 = eingabeauswerten(nutzer2)

     generator(nutzer,nutzer2)

start()
