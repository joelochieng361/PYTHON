# python functions.
# They are a block of code/ statements that perform a given task/ action
# They can be reused throughout the program to perform different tasks
# Functions are defined using the "def" keyword.
# We have two main types ;
# 1. In-built functions - They come pre-installed with the interpreter i.e print(), pop()
# 2. User-defined functions - They are created by a programmer to solve a given task
# To define a function you need to give a name followed by parenthesis
# For the function, it is usually indented and to invoke a function, we use a function name

def greetings():
    print("hello, How are you")
  
# Below we call this a function by name  
greetings()

print("===================")
#addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)
addition()

print("=================")

# Create a funtion thst is able to multiply three values

def product():
    num3 = 10
    num4 = 7
    num5 = 14
    product = num3 * num4 * num5
    print("The product of the numbers is: ", product)
product()

#division
def division():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The quotient is: ", quotient)
for function in range(3):
    division()