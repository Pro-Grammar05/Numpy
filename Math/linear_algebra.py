import numpy as np

# multiply matrices
a = np.ones((2, 3))
b = np.full((3, 2), 2)
print(np.matmul(a, b))

# find determinant of a matrix
c = np.identity(3)
print(np.linalg.det(c))