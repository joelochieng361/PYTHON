# Functions with parameters
# parameters - They are values that get passed as arguments given to a function inside a parenthesis.

def greetings(name):
    print(f"{name}, how are ypu? Hope everything is fine")
    
greetings("benerd")
greetings("mary")
greetings("joseph")

print("=================")
def message(names):
    print(f"Hello, We shall be having a meeting on date....Please avail yourself")

message("Joy")
message("Stephen")

print("======================")

# Create a function that accepts parameter to add two numbers

def addition (x , y):
    sum = x + y
    print(sum)