### WAP to print factorial of a number .
num = int(input("Enter the number to find the factorial of number:"))
fact = 1
for i in range(1, num + 1 ):
    fact = fact * i

print(f"Factorial of a {num} is {fact}")