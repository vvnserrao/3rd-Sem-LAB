num1 = int(input("Enter First Number: "))
operation = input("Enter the Operation: ")
num2 = int(input("Enter Second Number: "))
if operation=="+":
    print("Answer is",num1+num2)
elif operation=="-":
    print("Answer is",num1-num2)
elif operation=="*":
    print("Answer is",num1*num2)
elif operation=="/":
    if num2 !=0:
        print("Answer is",num1/num2)
    else:
        print("Cannot devide it by zero")