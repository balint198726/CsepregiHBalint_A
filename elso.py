#1.feladat:	Mértani sorozatnak nevezzük az olyan sorozatokat, amelyekben (a másodiktól kezdve) bármelyik tag és az azt megelőző tag hányadosa állandó. Ezt a hányadost idegen szóval kvóciensnek nevezzük. Jele: q. Legyen a sorozat n-edik tagja an. Ekkor:   alakban kiszámolható. A mértani sorozat első n tagjának összege
#Olvasd be a kvóciens(q) értékét, és az első elemet a felhasználótól, majd írd ki a mértani sorozat első 10 elemét!
#pl: a1=3 q=2
#Ki: 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536
def elso():
    a1=int(input("Adja meg a mértani sorozat első elemét: "))
    q = int(input("Adja meg a kvócienst: "))
    masodiktag=a1*q
    harmadiktag=masodiktag*q
    negyediktag=harmadiktag*q
    otodiktag=negyediktag*q
    hatodiktag=otodiktag*q
    hetediktag=hatodiktag*q
    nyolcadiktag=hetediktag*q
    kilencediktag=nyolcadiktag*q
    tizediktag=kilencediktag*q
    print(masodiktag,harmadiktag,negyediktag,otodiktag,hatodiktag,hetediktag,nyolcadiktag,kilencediktag,tizediktag)
