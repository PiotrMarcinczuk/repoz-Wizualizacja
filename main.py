# plik = open('tekst.txt', 'r')
# znaki = plik.read(10)
# linia = plik.readline()
# wiersze = plik.readline()
#
# plik.close()
#
# print(znaki)
# print(linia)
# print(wiersze)
# print(len(wiersze))

# import sys
# print('Podaj kierunek studiow, rok i specjalizacje')
# dane = sys.stdin.readline()
#
# plik = open('dane.txt', 'w+')
# plik.write(dane)
# plik.close()
# lista = []
# for x in range(0,7):
#     lista.append(x)
#
# plik = open('dane.txt', 'a+')
# plik.write(str(lista))
# plik.close()

# with open('tekst.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')

# class PierwszaKlasa:
#     """Pierwsza klasa pythona"""
#     atrybut = 54321
#     def pierwsa_metoda(selfself):
#         return 'pierwsza metoda'
#
# obiekt = PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# obiekt.tekst = 'aaa'
# print(obiekt.tekst)
# print(obiekt.pierwsa_metoda())

class Ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = 'To bedzie klasa'

    def pole(self):
        return self.x *

    def obowd(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

prostokat = Ksztalty(10, 30)
print(prostokat.pole())
print(prostokat.obwod())
print(prostokat.opis())
prostokat.dodaj_opis('Prostokat')
print(prostokat.opis)
prostokat.skalowanie(0.5)
print(prostokat.x)
print(prostokat.y)