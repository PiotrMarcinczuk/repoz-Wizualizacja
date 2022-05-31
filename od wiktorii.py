import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PIL as Image

# ZESTAW B

# # Zadanie 1
# Za pomocą bibliotek matplotlib utwórz wykres liniowy funkcji
# 𝑓(𝑥)=sin(𝑥)+ √𝑥 dla 50 wartości x z przedziału [1, 16]. Dodaj
# odpowiednie etykiety do osi wykresu (‘x’, f(x)), dodaj zakresy
# na osiach odpowiednio na osi x (1,16), na osi y (1,6). Dodaj
# styl do linii oraz tytuł wykresu.

# x = np.arange(1, 16, (16-1)/50)
# fx = np.sin(x)+np.sqrt(x)
# plt.plot(x, fx, 'r--')
# plt.title('Wykres funkcji f(x)=sin(x)+ x^(1/2)')
# plt.xticks(np.arange(1,16.1))
# plt.yticks(np.arange(1,6.1))
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.show()


# # Zadanie 2
# Za pomocą matplotlib odwzoruj siatkę wykresów z poniższego
# zdjęcia. Siatkę zapisz do pliku(imie_nazwisko_zad2.png)

# fig, axs = plt.subplots(3, 1, )
#
# z2x1 = np.arange(-1, 1.1, 0.25)
# z2fx1p = np.cos(z2x1)-np.tan(z2x1)
# z2fx1n = np.cos(z2x1)*np.sin(z2x1)
# axs[0].plot(z2x1, z2fx1n, label='cos(x)*sin(x)')
# axs[0].plot(z2x1, z2fx1p, label='cos(x)-tan(x)')
# axs[0].set_yticks([0,2])
# axs[0].set_xticks(np.arange(-1, 1.1, 0.25))
# axs[0].set_title('Wykres dwoch funkcji')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('wyniki funkcji')
# axs[0].legend()
# fig.delaxes(axs[1])
#
# z2x2 = np.arange(1, 4.1, 1)
# z2fx2 = z2x2**2/np.sqrt(z2x2)
# axs[2].plot(z2x2, z2fx2, 'g^',label='x^2/sqrt(x)')
# axs[2].set_title('Wykres funkcji')
# axs[2].set_yticks([2.5, 5.0, 7.5])
# axs[2].set_xticks(np.arange(1, 4.1, 0.5))
# axs[2].set_xlabel('x')
# axs[2].set_ylabel('wyniki funkcji')
# axs[2].legend()
# plt.savefig('karolina_talarek_zad2.png')
# plt.show()


# # Zadanie 3
# Używając biblioteki pandas wczytaj zawartość pliku „automobile.csv”
# do ramki danych i wykonaj następujące kroki:
# • Z 50 ostatnich wierszy utwórz nową ramkę danych.
# • Na nowej ramce danych dokonaj grupowania danych po kolumnie ‘Car model’
# • Na wykresie słupkowym przedstaw średnią ilość koni mechanicznych
#   (kolumna ‘Horsepower) dla każdej z grup. Dodaj nazwy etykiet do wykresu oraz tytuł.

# dane = pd.read_csv('automobile.csv', header=0, sep=";", decimal=".")
# df = pd.DataFrame(dane)
#
# df50 = df.tail(50)
# print(df50)
#
# grupy = df50.groupby(['Car model'])
# print(grupy)
#
# grupy = df50.groupby(['Car model']).agg({'Horsepower':['mean']})
# grupy.plot(kind='bar', xlabel='Car model', ylabel='Horsepower',
#            rot=0, legend=False, title='Średnia ilość koni mechanicznych dla danego modelu auta')
# plt.show()


# 

# dane = pd.read_csv('automobile.csv',header=0,sep=";",decimal='.')
# df = pd.DataFrame(dane)
# df = df.groupby(["Num-of-dors"]).count()
# df = df['Car model']
# df.plot(kind='pie',subplots=True,autopct='%.0f %%',figsize=(10, 10),fontsize=14)
# plt.xlabel("Liczba drzwi")
# plt.ylabel("Liczba drzwi")
# plt.title('Wykres')
# plt.show()
