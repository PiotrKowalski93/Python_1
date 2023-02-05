import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a)
print(a.shape)

# Slicing
# All rows, but only column 0
print(a[:,0])
print(a[0,:])

# Transpose
#print(a.T)

# Diagonal
print(np.diag(a))

# More Slicing
print(a[0,0:2])
print(a[1,0:2])