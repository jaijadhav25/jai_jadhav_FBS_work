### Write a program to check if entered number is a palindrome or not.

def palindrome(num):
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

num = int(input("Enter number to check palindrome or not:"))

res = palindrome(num)

if(res == num):
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not palindrome.")