# cw1
sporty = ['pilka_nozna','koszykowka','tenis','hokej']
sporty.reverse()
sporty.append('Rugby')
print(sporty)

# cw2
slownik = {'Aten':'Ateneum', 'Arch':'Archiwum', 'Bibl':'Biblioteka'}
print(slownik['Aten'])

# cw3
slo = {'Wiedzmin_3':'10', 'Gothic':'9', 'Tibia':'3'}
print (len(slo))

# cw4
napis = input("Wprowadz napis: ")
i=0
for x in napis:
    if x=='a':
        i+=1
print(i)


# cw5
import sys as system
system.stdout.write("Podaj pierwsza liczbe: ")
a = system.stdin.readline()
system.stdout.write("Podaj drugą liczbe: ")
b = system.stdin.readline()
system.stdout.write("Podaj trzecią liczbe: ")
c = system.stdin.readline()
a=int(a)
b=int(b)
c=int(c)
wynik=pow(a, b)+c
wynik=str(wynik)
system.stdout.write(wynik)

# cw6
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj druga liczbę: ")
c = input("Podaj trzecią liczbę: ")

a=int(a)
b=int(b)
c=int(c)

if a>b & a>c:
    print(str(a) + " jest największa liczba")
if b>a & b>c:
    print(str(b) + " jest najwieksza liczba")
if c>a & c>b:
    print(str(c) + " jest najwieksza liczba")

    import math

    # cw7
    lista = [1, 4, 5.4, 2.3, 7, 6.5]
    for x in lista:
        x = pow(x, 2)
        print(x)
    # cw8
    i = 0
    lista2 = []
    while (i < 11):
        x = input("Podaj liczbe: ")
        x = int(x)
        if (x % 2 == 0):
            lista2.append(x)
        i += 1
    print(lista2)
    # cw9
    a = input("Podaj liczbe")
    a = int(a)
    try:
        if (a < 1):
            raise ValueError
        pierwiastek = math.sqrt(a)
        print(pierwiastek)
    except ValueError:
        print("Podaj prawdiłową liczbe")