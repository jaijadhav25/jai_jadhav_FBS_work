### Write a program to check if the given number is positive or negative.

num1 = int(input("Enter the number:"))

if(num1 == 0):
    print("The number is neutrel")
elif(num1 < 0):
    print("THe number is negative")
else:
    print("The number is positive")