import numpy as np
# PRZYKLAD 1
# a = np.array([0,1])
# print(a)
#
# a = np.arange(2)
# print(a)
#
# print(type(a))
# print(a.dtype)
#
# a = np.arange(2, dtype ='int64')
# print(a.dtype)
#
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)
# print(a.ndim)
#
# m = np.array([np.arange(2),np.arange(2)])
# print(m.shape)
#
# print(type(m))
# PRZYKLAD 2
# zera = np.zeros((5,5))
# jedynki = np.ones((4,4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2,2))
# print(pusta)
#
# poz_1 = pusta [1,1]
# poz_2 = pusta [0,1]
# print(poz_1)
# print(poz_2)
#
# macierz = np.array([[1,2],[3,4]])
# print(macierz)
#
# liczby = np.arange(1,2,0.1)
# print(liczby)
#
# liczby_lin = np.linspace(1,2,5)
# print(liczby_lin)
#
# z = np.indices((5,3))
# print(z)
#
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
#
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
#
# mat_diag_k = np.diag([a for a in range(5)],-1)
# print(mat_diag_k)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)
#
# marcin = b'Marcin'
# marcin = 'Marcin'
# mar_3 = np.array(list(marcin))
# mar_4 = np.array(list(marcin), dtype='S1')
# mar_5 = np.array(list(b'Marcin'))
# mar_6 = np.fromiter(marcin, dtype='S1')
# mar_7 = np.fromiter(marcin, dtype='U1')
# print(mar_3)
# print(mar_4)
# print(mar_5)
# print(mar_6)
# print(mar_7)
#
# mat = np.ones((2,2))
# mat_1 = np.ones((2,2))
# mat = mat + mat_1
# print(mat)
# print(mat - mat_1)
# print(mat*mat_1)
# print(mat/mat_1)
# PRZYKLAD 3
a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
s = range(2,7,2)
print(a[s])

print(a[2:7:2])
print(a[1:])
print(a[2:5])

mat = np.arange(25)

mat = mat.reshape((5,5))
print(mat)
print(mat[1:])
print(mat[:,1])
print(mat[:,-1:])
print(mat[2:6, 1:3])
print(mat[:, range(2,6,2)])
print('')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0,0], [3,3]])
cols = np.array([[0,2], [0,2]])
y = x[rows,cols]
print(y)
