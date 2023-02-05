import numpy as np
from timeit import default_timer as timer

a = np.array([1,2,3])

print(a)
# Dimentions
print(a.shape)
print(a.dtype)
# NUmber of dimentions
print(a.ndim)
print(a.size)
# Bit size of element
print(a.itemsize)

A = np.random.randn(1000)
B = np.random.randn(1000)

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot

def dot2():
    return np.dot(A, B)

T = 1000

start = timer()
for i in range(T):
    dot1()
end = timer()

t1 = end - start

start = timer()
for i in range(T):
    dot2()
end = timer()

t2 = end - start

print('List: ',t1)
print('np.dot: ',t2)


