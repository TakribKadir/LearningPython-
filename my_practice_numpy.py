import numpy as np
# Creating array
#1d array
a = np.array([1,2,3])
print("1D array:", a)

b = np.array([[1 ,2], [3, 4]])
print("2D Array:\n", b)

#array properties shape, ndim, dtype, size.
print("Shape:", a.shape) #
print("Dimensions:", a.ndim)
print("Data type:", a.dtype)
print("Total elements:", a.size)

# special array

print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((3, 3)))
print("Full with 7s:\n", np.full((2, 2), 7))
print("Identity Matrix:\n", np.eye(3))
print("Range with step:\n", np.arange(0, 10, 2))
print("Evenly spaced:\n", np.linspace(0, 1, 5))

