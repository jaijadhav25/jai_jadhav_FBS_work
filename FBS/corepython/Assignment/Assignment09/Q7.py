# Write a program to find sum of digits using recursion.

def sum_of_digits(num,sum=0):
    if(num == 0):
        return sum
    else:
        sum = sum +(num % 10)
        return sum_of_digits(num // 10, sum)

num = int(input("Enter number to find sum of digits"))
res=sum_of_digits(num)
print(f"Sum of digit of {num} is: {res}")