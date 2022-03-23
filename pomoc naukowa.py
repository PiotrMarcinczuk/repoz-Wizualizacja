class Ciag():
    "Ciąg Arytmetyczny"

    def __init__(self, a1, n, r):
        self.a1 = a1
        self.n = n
        self.r = r
        self.ciag = (a1 + r * x for x in range(0, n))

    def wyświetl_dane(self):
        print(self.ciag)

    def pobierz_elementy(self, y):
        elementy = []
        for x in range(1, self.n + 1):
            x = self.a1 + (x - 1) + self.r
            elementy.append(x)
        print(elementy)

    def pobierz_parametry(self, a1, n ,r):
        self.a1 = a1
        self.n = n
        self.r = r
        print("a1: " + input())
        print("r: " + input(self.r))
        print("n: " + input(self.n))
    def policz_suma(self):
        suma = 0
        for i in range(0, self.n):
            suma += i
        return suma
    def policz_elementy(self, a1, r, n):
        elementy = []
        if (self.a1 != '') and (self.r != ''):
            return self.n
