# A set is an unordered collection of distinct elements

animals = {'cat', 'dog'}
print(animals)
animals.add('fish') 
animals.remove('cat')  
print(len(animals)) 
print(animals)

# how to loop sets?
animals = {'tiger','lion'}

for index,animal in enumerate(animals):
    print ('%d %s' %(index+1,animal))


# set conprrehensions:- 

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)  