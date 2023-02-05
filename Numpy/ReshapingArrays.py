import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
print(a)
print(a.shape)
# Reshape
b = a.reshape((2,4))
print(b)

# New Axis
c = a[np.newaxis, :]
print(c)
