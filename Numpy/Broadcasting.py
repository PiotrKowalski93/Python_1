import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9]])
y = np.array([1,0,1])
a = x + y
print(a)

# Overall sum
print(a.sum(axis=None))
# Rows sum
print(a.sum(axis=1))
# Columns sum
print(a.sum(axis=0))
