# Qn 4. Loop with arithmetics.
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
     sum += 1
    print("the sum of number when n is :",n," is: ", sum)
n = int(input("Enter n:"))
print(n)
sum_of_numbers