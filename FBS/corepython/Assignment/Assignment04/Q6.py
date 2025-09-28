### WAP to check if a given number is prime number or not.
num = int(input("Enter the number:"))

for i in range(2,num // 2 + 1):
    if(num % i == 0):
        print(f'It is not a prime number:{num}')
        break
else:
    print(f'It is prime number:{num}')