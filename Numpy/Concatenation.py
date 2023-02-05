import numpy as np

a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6]])

c = np.concatenate((a,b), axis=0)
print(c)
d = np.concatenate((a,b), axis=None)
print(d)
e = np.concatenate((a,b.T), axis=1)
print(e)