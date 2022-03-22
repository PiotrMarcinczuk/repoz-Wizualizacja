import random
#zadanie1
A=[1-x for x in range(1, 11)]
print(A)
B=[4**x for x in range(0, 8)]
print(B)
C=[x for x in B if x%2==0]
print(C)

#zadanie2
lista=[]
for x in range(11):
    lista.append(random.randrange(1, 50))
print(lista)
lista2=[x for x in lista if x%2==0]
print(lista2)

#zadanie3
produkty={'Pszenica':"Tony", "Batonik":"Sztuki", "Cukierki":"Kilogramy","Ziemniaki":"Kilogramy"}
print(produkty)
produkty2={key:value for key, value in produkty.items() if value=="Sztuki"}
print(produkty2)

#zadanie4
def czyProstokatny(a, b, c):
    if pow(a, 2)+pow(b, 2)==pow(c, 2):
        print("Jest prostokątny")
    else:
        print("Nie jest prostokątny")
czyProstokatny(3,4,5)

#zadanie5
def poleTrapezu(a=5, b=6, h=3):
    pole=((a+b)*h)/2
    return pole
print(poleTrapezu())

#zadanie6
def ciag(a1=1,b=4,ile=10):
    for x in range(ile):
        a1=a1*b
    return a1
print(ciag())

#zadanie 7
def ciag2(*liczba):
    if len(liczba)==0:
        return 0
    else:
        iloczyn = 1
        for x in liczba:
            iloczyn=iloczyn*x
    return iloczyn
print(ciag2(1,2,3,4,5))

#zadanie 8
def zakupy(**a):
    ile=len(a.items())
    wartosc = 0
    for key, value in a.items():
        wartosc+=value
    return ile,wartosc


print(zakupy(kapusta=10,marchew=11))

