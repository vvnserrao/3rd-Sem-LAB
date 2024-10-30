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

addition = series1 + series2
subtraction = series1 - series2
multiplication = series1 * series2
division = series1 / series2

print("\nAddition of Series:")
print(addition)

print("\nSubtraction of Series:")
print(subtraction)

print("\nMultiplication of Series:")
print(multiplication)

print("\nDivision of Series:")
print(division)