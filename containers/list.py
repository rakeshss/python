#  A list is the Python equivalent of an array, but is resizeable and can contain elements of different types:

xs = [3, 1, 2]    # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [3, 1, 'foo']"


# slicing: you can access more than one element at a time!! can create sublist et al

nums = list(range(5))
print(nums)  # prints:- [0, 1, 2, 3, 4]
print(nums[2:4]) # prints:-  gets the slice [2, 3] , here index 4 is excluded
print(nums[2:])  # prints:-  gets the slice [2, 3, 4] , here index 2 is included till the end

# few other operations on slices..
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"


