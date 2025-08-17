### Write a program to find sum of following series using functions :
#   a. 1+ 2 + 3 + 4+..... + n

def series(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

n = int(input("Enter number to find sum of series till n :"))

res = series(n)

print(f"Sum of the series is {res}.")