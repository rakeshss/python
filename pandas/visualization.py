import pandas 
import numpy as np
import matplotlib.pyplot as plt

input1 = {
    'Name' : pandas.Series(['Rakesh','Sachin','Shashank','Amit']),
    'Marks': pandas.Series([44,48,75,45])

} 

df1 = pandas.DataFrame(input1)
df1.plot.bar()
plt.show()