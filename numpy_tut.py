import numpy as np

a = np.array([1, 2, 3], dtype='int16')
b = np.array([[1.0, 2, 3], [4, 5, 6]])

# Print array
print(a)
print(b)

# Get dimension
print(f"Dimension of a is: {a.ndim}; Dimension of b is: {b.ndim}")

# Get Shape = Number of rows and columns
print(f"Shape of a is: {a.shape}; Shape of b is: {b.shape}")

# Nummber of elements
print(f"The no. of ele in a is: {a.size}; The no. of ele in b is: {b.size}")

# Get Type ('int64' => 64 bits or 8 byte)
print(f"The data type of a is: {a.dtype}; The data type of b is: {b.dtype}")

# Get Size of each element
print(f"The size of a is: {a.itemsize}; The size of b is: {b.itemsize}")

# Total number of bytes (8 bits = 1 byte)
print(f"The size of a is: {a.nbytes}; The size of b is: {b.nbytes}")


zero = np.zeros((4, 4), dtype='int32')
one = np.ones((2, 2), dtype='int32')
print(zero)
print(one)

zero[1:3, 1:3] = one
print(zero)


# Access element: a[row, column]
# To get multiple elements: [start_index:end_index:steps]
# Array of all same number: np.full((row, col), number)
# Identity Matrix: np.identity(5) 5 x 5 dimension identity array
# To make a copy of an array: b = a.copy() # b = a => b and a both point towards same array
# Matrix multiplication: np.matmul(a.b)
# Determinant: np.linalg.det(a)
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html -> Linear Algebra of Matrix
