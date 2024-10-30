import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("LCM: ", lcm(a, b))
