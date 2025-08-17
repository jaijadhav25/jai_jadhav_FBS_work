### Write a program find reverse of a number

def reverse_number(num):
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10 
    return rev

num = int(input("Enter number to find reverse of number:"))

res = reverse_number(num)

print(f"Reverse of a {num} is {res}")