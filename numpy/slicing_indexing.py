import numpy as np

# Rank 2 array
# Shape(3,4)
a = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ])


# Answer the output
b = a[:2, 1:3]
print(b)

# Answer the output
print(a[0, 1])   

# Answer the output
print(a[0, 1])   
b[0, 0] = 77     
print(a[0, 1]) 

