import numpy as np

a = np.array([1,2,3])
print(a)
b = a
b[0] = 42
print(a)
print(b)

# Those types are reference types
# We need to use .copy

c = a.copy()
c[0] = 100
print(a)
print(b)
print(c)