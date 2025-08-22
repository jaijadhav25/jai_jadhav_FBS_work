# Write a program to find sum of n numbers using recursion.

def sum_of_series(num):
    if(num == 0):
        return 0
    else:
        return num + sum_of_series(num-1)

num = int(input("Enter number to find sum of n numbers:"))
res = sum_of_series(num)
print(f"Sum of series from 1 to {num} is: {res}")