# python module
# A python module is a file that contains python definations, statements and functions.

def add():
    num1 = 20
    num2 = 30
    sum = num1+num2
    print("the answer is: ", sum)
    
def subtract():
    x = 45
    y = 30
    difference = x - y
    print("The difference is: ", difference)
    
# These functions can be called onto another file
print("Area of a rectangle")
def area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Area of the rectangle is: ", area)

area()