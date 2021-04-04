import numpy as np

def softmax(L):
    expL = np.exp(L)
    print("Exponential of list is: ",expL)
    sumExpL = sum(expL)
    print("Sum of exponential is: ",sumExpL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())

numlist = [1,2,3,4]
print("softmax value is:",softmax(numlist))

