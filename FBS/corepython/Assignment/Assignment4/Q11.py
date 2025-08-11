### WAP to check if given number Strong Number.


num1 = int(input("Enter the number to check strong number:"))
temp = num1
sum = 0 
while(temp > 0):
    digit1 = temp % 10
    temp = temp // 10
    fact = 1
    for i in range(1,digit1 + 1):
        fact *= i
    sum += fact

if(sum == num1):
    print(f"{num1} is a strong numbe:")
else:
    print(f"{num1} is not a strong number:")