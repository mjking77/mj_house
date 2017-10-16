import numpy as np

a = np.array([[1,2,3], [4,5,6]])
dim_a = a.shape   # numpy shape = dim of array
b = np.array([[1,2], [3,4], [5,6]])
dim_b = b.shape

c = np.dot(a,b)

#x=np.array([1, 2])
# x.shape   #=(2,)

print dim_a, dim_b, c
