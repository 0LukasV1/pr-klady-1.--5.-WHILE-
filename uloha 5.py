#napíš program, ktorý bude v cykle načítavať slová dovtedy, pokiaľ nezadáte slovo začínajúce sa na písmeno "x". Program vypíše celkový počet znakov všetkých slov okrem posledného slova, začínajúceho sa na x

x=str(input("zadaj slovo: "))
a = 0
b = 0
c = len(x)

while a != True:
    x = str(input("zadaj slovo: "))
    b=len(x)
    c+=b
    a=x.startswith("x")
c-=b
print("celkovy pocet znakov slov je:",c)