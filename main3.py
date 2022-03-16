import math
# a = []
# for x in range(0,10):
#     a.append(x**2)
# print(a)
#
# a2 = [x**2 for x in range(0,10)]
# print(a2)

# b = []
# for x in range(0,6):
#     b.append(3**x)
# print(b)
#
# b2 = [3**x for x in range(0,6)]
# print(b2)

# c = []
# for x in a:
#     if(x % 2 == 1):
#         c.append(x)
# print(c)
#
# c2 = [x for x in a if x%2==1]
# print(c2)

# lista = []
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a,b))
#     print(lista)

# lista2 = [(a,b) for a in [1,2,3] for b in [4,5,6]]
# print(lista2)

# slownik = {'PZU': 'Panstwowy zaklad ubezpieczen',
#            'ZUS': 'Zaklad ubezpieczen spolecznych',
#            'PKO': 'Panstwowa kasa oszczednosci'}
#
# slownik_odwrocony = {}
# print(slownik)
# for key, value in slownik.items():
#     slownik_odwrocony[value] = key
# print(slownik_odwrocony)
#
# slownik2 = {value: key for key, value in slownik.items()}
# print(slownik2)

# def row_kwadratowe(a,b,c):
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print('Brak rozwiazane')
#         return -1
#     elif delta == 0:
#         print('Jedno rozwiazanie')
#         x = (-b)/(2*a)
#         return x
#     else:
#         print('Dwa rozwiazania')
#         x1 = ((-b)- math.sqrt(delta))/(2*a)
#         x2 = ((-b)+ math.sqrt(delta))/(2*a)
#         return x1, x2
#
# print(row_kwadratowe(6,-1,3))
# print(row_kwadratowe(4,2,3))
# print(row_kwadratowe(-1,7,1))

# def funkcja(a):
#     if a%2 == 0:
#         return('Liczba Parzysta')
#     else:
#         return('Liczba Nieparzysta')
#
# print(funkcja(1))

# def dlugosc_odcinka(x1=0, y1=2, x2=3, y2=4):
#     return math.sqrt((x2-x1)**2 +(y2-y1)**2)
# #domyslne
# print(dlugosc_odcinka())
# #pozycyjne
# print(dlugosc_odcinka(1,5,4,2))
# #pozycyjne, dwa okreslane
# print(dlugosc_odcinka(2,2,y2=7,x2=9))
# #argumenty po za kolejnoscia
# print(dlugosc_odcinka(x2=6,y2=2,x1=5,y1=2))
# #dwa argumenty domyslne, dwa z nowa wartoscia
# print(dlugosc_odcinka(x2=4, y2=7,))

# def ciag(* liczby):
#     if len(liczby) == 0:
#        return 0
#     else:
#        suma = 0
#        for i in liczby:
#            suma+=i
#        return suma
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8))

# def co_lubie(** rzeczy):
#     for cos in rzeczy:
#         print('to jest sznyc')
#         print(cos)
#         print('co lubie')
#         print(rzeczy[cos])
# co_lubie(gry=['planszowe','komputerowe'], slodycze='czekolada')