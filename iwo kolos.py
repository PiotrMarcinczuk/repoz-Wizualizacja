import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
import seaborn as sns

#zad_1
# a = np.sin(np.arange(1,16,1/50))+np.sqrt(np.arange(1,16,1/50))
# plt.plot((np.arange(1,16,1/50)),(a),":")
# plt.xticks(np.arange(1,16))
# plt.yticks(np.arange(1,6))
# plt.ylabel("f(x)")
# plt.xlabel("x")
# plt.title('Wykres f(x)')
# plt.show()
# #zad_2
# #
# plt.subplot(3, 1, 1,)
# a = np.cos(np.arange(-1,1,1/50))*np.sin(np.arange(-1,1,1/50))
# b = np.cos(np.arange(-1,1,1/50)) - np.tan(np.arange(-1,1,1/50))
# plt.plot((np.arange(-1,1,1/50)),(a))
# plt.plot((np.arange(-1,1,1/50)),(b))
# plt.xticks(np.arange(-1,1.25,1/4))
# plt.yticks(np.arange(0,3,2))
# plt.legend(labels=['cos(x)*sin(x)', 'cos(x)-tg(x)'],loc="best")
# plt.title("Wykres dwóch funkcji")
# plt.ylabel("wykres funkcji")
# plt.xlabel("x")
# plt.subplot(3, 1, 3)
# b = np.power(np.arange(1,4,1/50),2) / np.sqrt(np.arange(1,4,1/50))
# plt.xticks(np.arange(1,7,0.5))
# plt.yticks(np.arange(0,8,2.5))
#
# plt.ylabel("wykres funkcji")
# plt.title("Wykres funkcji")
# plt.xlabel("x")
# plt.plot((np.arange(1,4,1/50)),(b),">",color="yellow")
# plt.legend(labels=['x^2/sqrt(x)'],loc="upper left")
# plt.show()
#plt.savefig('Iwo_Stanislawski.png')
#Zad_3
# xlsx = pd.read_csv('automobile.csv',header=0,sep=";",decimal='.')
# df = pd.DataFrame(xlsx)
# print(df)
# df2 = df[-50:]
# df2 = pd.DataFrame(df2)
# print(df2)
# df2 = df2.groupby(['Car model']).mean()
# a = df2['Horsepower']
# print(a)
# a.plot(kind='bar',rot=45,figsize=(10, 10))
# plt.ylabel('Ilość')
# plt.xlabel("Model")
# plt.title('Wykres')
# plt.show()
#Zad_4
# xlsx = pd.read_csv('automobile.csv',header=0,sep=";",decimal='.')
# df = pd.DataFrame(xlsx)
# df = df.groupby(["Num-of-dors"]).count()
# df = df['Car model']
# df.plot(kind='pie',subplots=True,autopct='%.0f %%',figsize=(10, 10),fontsize=14)
# plt.xlabel("Liczba drzwi")
# plt.ylabel("Liczba drzwi")
# plt.title('Wykresik')
# plt.show()
