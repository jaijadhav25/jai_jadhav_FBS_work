### Write a program to find sum of following series using functions :
#   c. 1^1 + 2^2 + 3^3+ ...... n^n

def series(num):
    sum = 0
    for i in range(1,num+1):
        sum += i ** i
    return sum

n = int(input("Enter number to find the sum of series till n : "))

res = series(n)

print(f"Sum of the series is {res}. ")