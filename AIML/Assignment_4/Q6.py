import pandas as pd
#Create a Pandas Series
data = pd.Series([5,10,15,20,25])

# Convert the Pandas Series to a Python list
data_list=data.tolist()

print("Python list:",data_list)
print("Type of the list:",type(data_list))