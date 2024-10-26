def masodik():
    #2.feladat:	Egy fagylaltozó az év minden hónapjában akciót kínál. Minden hónapban annyi százalék kedvezményt adnak a fagyi árából, ahányadik hónap van.
    #Kivéve:
    #június, és július  hónapokat ilyenkor teljes árat fizetnek
    #decemberben  hónapban ilyenkor 10% kedvezményt kapnak
    #Egy honap nevű változóba tárolják az aktuális hónapot. Egy vegOsszeg nevű változóba a fizetendő teljes árat. Ezeket kérd be a felhasználótól! Az a feladatod, hogy kiírd a felhasználónak, hogy : pl.: november „Hónapos akció: november ” majd utána új sorba A fizetendő összeget. A fizetendő összeg kiszámítása: fizetendő összeg= teljesösszeg*kedvezmény/100
    #(19 pont)
    vegOsszeg=float(input("Adja meg a fagyi teljes árát forintban: "))
    honap=str(input("Adja meg a hónapot a kedvezményhez: "))
    if honap==("január"):
        print("A fizetendő összeg: ",vegOsszeg*0.99)
    elif honap == ("február"):
        print("A fizetendő összeg: ", vegOsszeg * 0.98)
    elif honap == ("március"):
        print("A fizetendő összeg: ", vegOsszeg * 0.97)
    elif honap == ("április"):
        print("A fizetendő összeg: ", vegOsszeg * 0.96)
    elif honap == ("május"):
        print("A fizetendő összeg: ", vegOsszeg * 0.95)
    elif honap == ("június"):
        print("A fizetendő összeg: ", vegOsszeg)
    elif honap == ("július"):
        print("A fizetendő összeg: ", vegOsszeg)
    elif honap == ("augusztus"):
        print("A fizetendő összeg: ",vegOsszeg*0.92)
    elif honap == ("szeptember"):
        print("A fizetendő összeg: ", vegOsszeg * 0.91)
    elif honap == ("október"):
        print("A fizetendő összeg: ", vegOsszeg * 0.90)
    elif honap == ("november"):
        print("A fizetendő összeg: ", vegOsszeg * 0.89)
    elif honap == ("december"):
        print("A fizetendő összeg: ", vegOsszeg * 0.90)
    else:
        print("Rossz input.")