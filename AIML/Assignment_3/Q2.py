password=input("Enter the Password: ")
upper=False
lower=False
numeric=False
if len(password)>=8:
    for i in password:
        if i.isupper():
            upper=True
        if i.islower():
            lower=True
        if i.isdigit():
            numeric=True
if lower==upper==numeric==True:
      print("Password is valid.")
else:
        print("Password is invalid.")
            