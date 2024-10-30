import pandas as pd

empno = int(input("Enter employee number: "))
ename = input("Enter employee name : ")
basic = float(input("Enter basic salary: "))

data = {
    'empno': empno,
    'ename': ename,
    'basic': basic
}
series=pd.Series(data)
print("\nPandas Series:")
print(series)