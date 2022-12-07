#napíš program, ktorý bude V CYKLE načítavať mená a vypisvať ich dĺžku dovtedy, poikiaľ ako meno nezdáte reťazec "koniec"

x=str(input("napis meno: "))
print(len(x))
while x != "koniec":
    x = str(input("napis meno: "))
    print(len(x))


print("nacitavanie mien bolo ukoncene")

