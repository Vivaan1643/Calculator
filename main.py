def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))

print("SUM:", add(num1,num2))
print("Difference", subtract(num1,num2))
print("Product", multiply(num1,num2))
print("quotient", divide(num1,num2))