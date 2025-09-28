# Write a program to check whether a number is prime or not using recursion.

def prime(num, div=2):
    if(num <= 1):
        return False
    if(num == div):
        return True
    if(num % div == 0):
        return False
    else:
        return prime(num, div + 1)

num = int(input("Enter number to check prime or not :"))
res=prime(num)
if(res):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not prime number.")