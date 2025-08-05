### Write a program to accept 3 digit number. If first digit is double of second digit and half of
#   third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
#    Eg : - 428 , 214 etc.

num = int(input("Enter the number:"))

temp = num

num3 = temp % 10
temp = temp // 10 

num2 = temp % 10
temp = temp // 10

num1 = temp % 10

if(num1 == 2 * num2 and num1 * 2 == num3):
    print("Yes, you have done it")
else:
    print("Please try next time.")
