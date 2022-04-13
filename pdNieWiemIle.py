import numpy as np

# a = np.array([20,30,40,50])
# b = np.arange(4)
# d = np.array([2.5,65.2,45.2,1.6])
#
# c = a+b
# print(c)
# e = d+a
# print(e)
# print(b**2)
# print(e.dtype)


# a = np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=1)) #parametr axis = 1 lub axis=0 okresla czy suma bedzie liczona w wierszach czy kolumnach
# print(a.sum(axis=0))
# print()
# print(a.cumsum(axis=1))

# a = np.arange(3)
# b = np.arange(3)
#
# print(a)
# print(b)
#
# c = a.dot(b)
# print(c)
#
# d = np.array([[1, 2, 4], [5,2,4]])
# e = np.array([[2,3],[6,8],[4,2]])
#
# print(e.dot(d))

# b = np.arange(5)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))

# a = np.arange(6).reshape((3,2))
# print(a)
# for b in a:
#     for c in b:
#         print(c)
#
# for b in a.flat:
#     print(b)

# a = np.arange(12)
# print(a)
# b = a.reshape(3,4)
# print(b)
# print()
# c = a.reshape(4,3)
# print(c)
# d = b.ravel() #funkcja splaszcza macierz do jednego wymiaru
# print(d)
# print()
# e = b.T
# print(e)

# 1
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# c = a + b
# print(c)
# print(b**2)
# print(np.exp(b))
# print(np.sqrt(b))
# d = np.sqrt(b)
# e = d + b
# print(e)
# # 2
# a = np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))


# 3
# a = np.arange(3)
# b = np.arange(3)
#
# print(a.dot(b))
#
# c = np.array([[2,3,6],[5,1,2]])
# d = np.array([[4,2],[5,6],[1,7]])
# e = c.dot(d)
# print(e)

# 4
# a = np.arange(6).reshape(3,2)
# print(a)
# for b in a:
#     for c in b:
#         print(c)

# 5
# a = np.arange(6)
# print(a)
# b = a.reshape((3,2))
# c = a.reshape((2,3))
# print(b)
# print(c)
# d = c.ravel()
# print(d)
#
# e = c.T
# print(e)

# Zadanie 1 i 3
a = np.arange(3,6).reshape((3))
b = np.arange(3).reshape((3))
c = a * b
print(c)

print(b.dot(a))

# Zadanie 2
[4,-2,3]
[4,5,13]
[3,2, 1]
a = np.array([[4, -2, 3], [4, 5, 13], [3, 2, 1]])
b = np.arange(16).reshape((4, 4))
print(a)
print()
print(b)
print()
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))

# Zadanie 4
a = np.arange(3).reshape((1,3))
b = np.array([2.5,65.2,45.2]).reshape((1,3))
print(a*b)

# Zadanie 5
a = np.arange(6).reshape((2,3))
b = np.sin(a)
print(b)

# Zadanie 6
a = np.arange(6).reshape((2,3))
b = np.cos(a)
print(b)

# Zadanie 7
wynik = a+b
print(wynik)

# Zadanie 8
a = np.arange(9).reshape((3,3))
print(a)
for i in a.T:
    print(i)

# Zadanie 9
a = np.arange(9).reshape((3,3))
print(a)
for i in a.flat:
    print(i)

# Zadanie 10
a = np.arange(81).reshape((9,9))
print(a)
m1 = a.reshape((3,27))
m2 = a.reshape((1,81))
print(m1)
print(m2)
#
