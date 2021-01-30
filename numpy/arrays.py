import numpy as np

print("printing zero's using built-in function")
a = np.zeros((2,2))
print(a)


print("************************")
a = np.ones((1,2))  # last element defines rank, it's two dimensional with single slice.
print(a)
print("************************")

print("Identity matrix..")
b = np.eye(2)   # Create a 2x2 identity matrix
print(b)