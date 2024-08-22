import  numpy as np
import scipy

a = np.array([1, 2, 3])
b = np.zeros((2,3,5))

print(a)
print(b)

tmp = np.loadtxt('csv/sample.csv', delimiter = ',', skiprows = 1)
print(tmp)

x = np.arange(10, 1, -1)
print(x)
y = x[np.array([3, 3, 1, 8])]
print(y)
z = x[np.array([3, 3, -3, 8])]
print(z)
print(np.array([3, 3, 1, 8]))

c = np.arange(20).shape
print('c=',c)

