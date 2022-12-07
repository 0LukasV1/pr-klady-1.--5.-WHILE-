#napíš program, ktorý bude načítavať čísla dovtedy pokiiaľ nezadáte nulu. Na záver program vypíše aritmetický priemer týchto čísel. Nulu do priemeru nezahrňte

x=int(input("zadaj cislo: "))
a=x
b=0
c=0
while x != 0:
    x = int(input("zadaj cislo: "))
    a+=x
    b+=1
c=a/b
print("aritmeticky priemer je: ",c)
