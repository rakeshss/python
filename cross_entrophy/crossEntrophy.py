import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


x = [1, 1, 0]
y = [0.8,0.7,0.1]

a = [0,0,1]
b = [0.8,0.7,0.1]

CE = cross_entropy(x,y)  # should return arounf 0.69
print(CE)

CE = cross_entropy(a,b)  # should return arounf 5.12
print(CE)