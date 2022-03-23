# # CZESC 1
class Ksztalty():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = 'To jest klasa dla ogolnych ksztaltow'

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, tekst):
        self.opis = tekst

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self,x):
        self.x = x
        self.y = x

class KwadratLiteryL(Kwadrat):
    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y


kwadrat = Kwadrat(5)

print(kwadrat.obwod())
print(kwadrat.pole())
kwadrat.dodaj_opis('To jest figura kwadrat')
kwadrat.skalowanie(0.4)
print(kwadrat.obwod())
print("")


litera = KwadratLiteryL(5)
print(litera.obwod())
print(litera.pole())
litera.dodaj_opis('To jest litera L')
litera.skalowanie(0.2)
print(litera.obwod())

# CZESC 2
class Kwadrat(Ksztalty):
    def __init__(self,x):
        self.x = x
        self.y = x
kwadrat = Kwadrat(7)
print(kwadrat)

class Kwadrat(Ksztalty):
    def __init__(self,x):
        self.x = x
        self.y = x
    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

kwadrat = Kwadrat(5)
print(kwadrat)


# CZESC 3
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return  "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)

class Menadzer(Pracownik):
    def przedstaw_sie(self):
     return "{} {} jestem menadzer i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

Sznycu = Pracownik('Wojtek', 'Szalow', 2500)
Szymon = Menadzer('Szymon', 'Dziezycon', 10001)

print(Sznycu.przedstaw_sie())
print(Szymon.przedstaw_sie())

class Osoba:
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return"{} {}".format(self.imie, self.nazwisko)

class Pracownik:
    def __init__(self, pensja):
        self.pensja = pensja

class Menadzer(Osoba, Pracownik):
    def __init__(self,imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {} jestem menadzer i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

    adrian = Menadzer("Adrian", "Mikulski", 12000)
    print(adrian.przedstaw_sie())

# CZESC 4
imie = 'Maks'
it = iter(imie)
print(it)
print(next(it)) #na wyjsciu M
print(next(it)) #na wyjsciu a
print(next(it)) #na wyjsciu k
print(next(it)) #na wyjsciu s


class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return  self.data[self.index]

napis = Wspak('Maks')
print(napis.__next__())
for a in napis:
    print(a)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

gen = reverse("Feliks")
print(next(gen))
print("Marek")
print(next(gen))

litery = (litera for lista in "Zdzislaw")
print(litery)
print(next(litery))
