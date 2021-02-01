import pandas as pd
import numpy as np
import sys

series1 = pd.Series([10,20,30,40])
print(series1) 

# create array using numpy then create series out of it
fruits = np.array(['apple','orange','mango','pear'])
series2 = pd.Series(fruits)
print(series2)

