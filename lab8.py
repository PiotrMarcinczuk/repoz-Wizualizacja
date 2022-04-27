import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(100))
ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.savefig('wykres.png')
# plt.show()

# dane = {'Kraj':['Belgia','Indie','Chiny','Rosja'],
#         'Stolica':['Bruksela','New Delhi','Pekin','Moskwa'],
#         'Populacja':[111190846, 1303171035,1201110343,134498991],
#         'Kontynent':['Europa','Azja','Azja','Europa']}
#
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
#
# grupa.plot(kind='bar', ylabel='Populacja w mld', xlabel='Kontynent', rot=0, legend=True, title='Populacja dla danego kontynentu', color='green')
# # plt.legend(loc='upper left') to nie ma sensu
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', y='Wartość zamówienia', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
# plt.savefig('wykreskolo.png')
# plt.show()

# ts = pd.Series(np.random.randn(100)) tu musi byc ten jest odkomentowane na gorze
# ts = ts.cumsum() tu musi byc ten jest odkomentowane na gorze

# df = pd.DataFrame(ts)
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# print(df)
# df.plot()
# plt.legend(['Wartość','Średnia krocząca'])
# plt.show()

# NIE MOJE WIEKSZOSC


ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.savefig('wykres.png')
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846, 13031171035, 207847528, 38675467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby('Kontynent').agg({'Populacja' : ['sum']})
# print(grupa)
#
# # grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja w mld',
# #            rot=0)
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja dla kontynentów')
# plt.savefig('wykres1.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg(
#     {'Wartość zamówienia': ['sum']})
# print(grupa)
#
# grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20,
#                figsize=(6, 6), legend=(0, 0))
# plt.show()

# df = pd.DataFrame(ts)
#
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# print(df)
# df.plot()
# plt.legend(['Wartości', 'Średnia krocząca'])
# plt.show()

# zad1
# df = pd.read_excel('imiona.xlsx', header=0)
# lista = df['Rok'].unique()
# grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
# wykres = grupa.plot(xticks=lista, figsize=(10, 6))
# wykres.tick_params(axis='x', labelrotation=0)
# plt.show()
# zad2
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)
print(df)
grupa = df.groupby('Plec').agg({'Liczba':['sum']})
plt.show()
nie koniec
