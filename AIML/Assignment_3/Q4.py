s1=input("Enter a String: ")
vowels=['a','e','i','o','u']
cnt=0
for i in s1:
    if i.lower() in vowels:
        cnt+=1
print("Number of vowels are:",cnt)
        