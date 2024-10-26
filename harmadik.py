def harmadik():
    #3.feladat:	Írd ki  50-900-ig a páros számokat, amik oszthatók 11-el, egy sorba  álló függőleges vonallal (|)  elválasztva. (ne egyesével gépeld be őket, az nem jó megoldás!) A megoldásodat for-al és while-al is valósítsad meg! (19 pont)
    for i in range(50,901,2):
       if i%11==0:
           print(i,end=(' | '))
    n=50
    while n<900:
        if n%11==0:
            print(n,end=(' | '))
            n +=2