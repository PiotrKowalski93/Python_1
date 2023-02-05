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

# hstack - horizontall stack
# vstack - verticalstack
a1 = np.array([1,2,3])
a2 = np.array([1,2,3])
c1 = np.hstack((a1,a2))
print(c1)

c2 = np.vstack((a1,a2))
print(c2)