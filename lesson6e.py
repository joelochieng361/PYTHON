# used to show possible errors
try:
    number = 100
    answer = number / 0
    print("The answer is: ", answer)
except Exception as e:
    print("division by zero error: ", e)