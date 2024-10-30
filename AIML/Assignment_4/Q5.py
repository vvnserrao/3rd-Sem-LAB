import pandas as pd
value=input("Enter the values for the series by giving space: ").split()
list1=[]
for i in value:
    list1.append(i)
    
series=pd.Series(list1)
print("Pandas Series:")
print(series)