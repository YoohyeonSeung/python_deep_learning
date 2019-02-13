import numpy as np

a = np.array([1, 2])
b = np.array([ [1,2,3], [4,5,6]])
c = np.dot(a, b)


print(a)
print(a.shape)
print(np.sum(a, axis = 0))
print(b)
print(b.shape)
print(c)
