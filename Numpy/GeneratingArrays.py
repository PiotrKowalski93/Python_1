import numpy as np

a = np.zeros((2,3))
print(a)

a = np.ones((2,3))
print(a)
print(a.dtype)

a = np.full((2,3), 5.0)
print(a)

# 3x3 matrix with 1 in diagonal and 0 elsewhere
a = np.eye(3)
print(a)

# from 0....X
a = np.arange(20)
print(a)

# form X...Y with K number of elements
a = np.linspace(0,15,9)
print(a)