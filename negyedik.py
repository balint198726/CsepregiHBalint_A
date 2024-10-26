import math
def negyedik():
    #4.feladat:	Kérj be a felhasználótól egy valósszámot. A programod számítsa ki a bekért érték felső egész részét(kerekítse felfele), ehhez a math csomag ceil() eljárását használd.
    #Pl1:
    #Be: Kérlek adj meg valós számot: 3.4
    #Ki: Kerekített értéke: 4
    #(19 pont)
    szam=float(input("Kérlek adj meg egy valós számot: "))
    print("Kerekített értéke: ",math.ceil(szam))
