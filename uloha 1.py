#načítavaj čísla dovtedy, pokiaľ nenačítaš číslo väčšie ako 100. Ak sa to stane, program skončí a vypíše celkový počet načítaných čísel
x = int(input('skok medzi pocitanim: '))
a = 0
b = 0

while a < 100:
    a+=x
    b+=1

print("pocet nacitanych cisiel je: ",b)
