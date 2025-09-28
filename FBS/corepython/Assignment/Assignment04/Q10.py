### WAP to check if given number is Perfect Number.
num1 = int(input("Enter the number to check the prefect number:"))
sum = 0
for i in range(1 , num1 // 2 + 1):
    if(num1 % i == 0):
        sum += i
if(num1 == sum):
    print(f'{num1} is perfect number:')
else:
    print(f'{num1} is not perfect number:')
