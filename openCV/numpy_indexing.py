import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#   |1  2  3  4|
#   |5  6  7  8| 
#   |9 10 11 12|

#   a[ x , y ]
b = a[:2, 1:3]

#  :2 --- signifies all rows from start(0) to 1
# 1:3 --- signifies all columns from 1 to 2
# the resulting matrix is
#   |2 3|
#   |6 7|

print(a[0, 1])

b[0, 0] = 77

print(a[0, 1])

############################################################################

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

row_r1 = a[1, :]    # a[row , column]
row_r2 = a[1:2, :]  # [:] signifies all values from start to end 
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

############################################################################

a = np.array([[1, 2], [3, 4], [5, 6]])

print(a[[0, 1, 2], [0, 1, 0]])  # a[x_list, y_list]
# here [0, 1, 2] --> x_list and [0, 1, 0] --> y_list
# represents the coordinates (0,0) (1,1) (2,0)

print(np.array([a[0, 0], a[1, 1], a[2, 0]]))

print(a[[0, 0], [1, 1]])

print(np.array([a[0, 1], a[0, 1]]))


############################################################################

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a)
b = np.array([0, 2, 0, 1])

print(a[np.arange(4), b])

a[np.arange(4), b] += 10

print(a)
