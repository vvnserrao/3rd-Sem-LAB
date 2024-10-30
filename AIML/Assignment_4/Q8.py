import pandas as pd

data1=input("Enter the values for First series by giving space:").split()
data2=input("Enter the values for Second series by giving space:").split()

series1=[]
for i in data1:
    series1.append(int(i))
series1=pd.Series(series1)

series2=[]
for i in data2:
    series2.append(int(i))
series2=pd.Series(series2)

equal = series1 == series2
greater = series1 > series2
less = series1 < series2

print("\nComparison (Equal):")
print(equal)

print("\nComparison (Greater):")
print(greater)

print("\nComparison (Less):")
print(less)