arr=[1,2,1,2,3,4,5,6,7,3,2,6,10,8]
arr=list(set(arr))
arr.sort()
print("Second Smallest Element: ",arr[1])
print("Second Largest Element: ",arr[-2])