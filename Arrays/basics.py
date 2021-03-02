import numpy as np

a = np.array([1, 2, 3], dtype = 'int16')
b = np.array([[4, 2, 0], [0, 6, 9]])

print(a, a.ndim, a.shape, a.dtype, a.itemsize, a.size, a.nbytes, end = '\n\n')
print(b, b.ndim, b.shape, b.dtype, b.itemsize, b.size, b.nbytes)
# itemsize = dtype // 8
# nbytes = size * itemsize