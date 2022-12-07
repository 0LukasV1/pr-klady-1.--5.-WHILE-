#načítavaj čísla dovtedy, pokiaľ ich súčet nepresiahne hodnotu 100. Program vypíše hodnotu tohto súčtu a aj počet čísel

x=0
a=0
b=-1

while a < 100:
    x+=1
    a+=x
    b+=1

c=a-x

print("pocet cisiel je ",b,"ich sucet je",c)

