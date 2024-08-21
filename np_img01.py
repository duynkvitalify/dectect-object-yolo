import numpy as np
x = np.arange(10)
y = x ** 2

np.savez('x_y.npz', x_axis=x, y_axis=y)
load_xy = np.load("x_y.npz")

print(load_xy.files)
x = load_xy["x_axis"]
y = load_xy["y_axis"]
print(x)
print(y)


array_out = np.block([x[:, np.newaxis], y[:, np.newaxis]])
print("the output array has shape ", array_out.shape, " with values:")
print(array_out)
np.savetxt('x_y.csv',  X=array_out, header="x, y", delimiter=",")

del x, y
load_xy = np.loadtxt("x_y.csv", delimiter=",")
load_xy.shape
x = load_xy[:, 0]
y = load_xy[:, 1]
print(x)
print(y)
