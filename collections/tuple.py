t = (5, 6)        # Create a tuple
print(type(t))

d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"