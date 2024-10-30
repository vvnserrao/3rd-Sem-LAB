s1=input("Enter a String: ")
upper=0
lower=0
digits=0
for i in s1:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
        if i.isdigit():
            digits+=1
print("Number of UpperCase Letters are:",upper)
print("Number of LowerCase Letters are:",lower)
print("Number of Digits are:",digits)
