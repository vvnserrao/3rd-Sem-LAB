n1 = int(input("Enter length of First List: "))
n2 = int(input("Enter Length of Second List: "))
list1=[]
list2=[]
print("Enter the First List Element")
for i in range(n1):
    list1.append(input())
print("Enter the Second List Element")
for i in range(n2):
    list2.append(input())    
list3=list1+list2
print("Merged List is:",list3)