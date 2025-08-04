### Write a program to check if given 3 digit number is a palindrome or not.

number = int(input("Enter the three digit number:"))

temp = number

number1 = temp % 10
temp = temp // 10

number2 = temp % 10 
temp = temp // 10

number3 = temp % 10
temp = temp // 10 

reverse_number = number1 * 100 + number2 *10 + number3

if (number == reverse_number):
    print(f"{number} is palindrome")
else:
    print(f"{number} is not palindrome")