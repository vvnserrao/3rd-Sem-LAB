import pandas as pd
import numpy as np

list1=[]
print("Enter 5 Elements: ")
for i in range(5):
    element=input()
    list1.append(element)
    
arr=np.array(list1)
series=pd.Series(arr)

print("\nPandas Series:")
print(series)