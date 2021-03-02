import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a, end = '\n\n')

''' 
    access an element a[r, c]
    access 13 
'''
print(a[1, 5])

'''
    get a specific row a[r, :] or column a[:, c]
    access first row, first column
'''
print(a[0, :], a[:, 2])

'''
    get specific elements a[starindex : endindex : stepsize]
    get first 3 even elemnts
'''
print(a[0, 1 : 6 : 2])