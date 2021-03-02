import numpy as np

# all 0s matrix
a = np.zeros((2, 3))
print(a, end = '\n\n')

# all 1s matrix
b = np.ones((4, 2, 2), dtype = 'int32')
print(b, end = '\n\n')

# any other number
c = np.full((2, 2), 69)
print(c, end = '\n\n')

# same shape of another array
A = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(np.full(A.shape, 4))
print(np.full_like(A.shape, 4), end = '\n\n')

''' 
    random decimal numbers
    random integer values from 'm' to 'n'
    same shape of another array
'''
print(np.random.rand(4, 2), end = '\n\n')
print(np.random.random_sample(A.shape), end = '\n\n')
print(np.random.randint(7, size = (3, 3)), end = '\n\n')
print(np.random.randint(-4, 7, size = (3, 3)), end = '\n\n')

# n*n identity matrix
print(np.identity(5), end = '\n\n')

# repeat an array 'n' times
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis = 0)
print(r1, end = '\n\n')

'''
    print:

    1 1 1 1 1
    1 0 0 0 1
    1 0 9 0 1
    1 0 0 0 1
    1 1 1 1 1
'''

output = np.ones((5, 5))
z = np.zeros((3, 3))

z[1, 1] = 9
output[1 : -1, 1 : -1] = z

print(output, end = '\n\n')