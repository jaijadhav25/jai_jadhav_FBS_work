### Write a program to swap two numbers without using third variable.

x = int(input("Enter the number:"))
y = int(input("Enter the number:"))

print(f"Before swapping {x} , {y}")

##without using third variable

#x = x + y
#y = x - y
#x = x - y

##using python 
x, y = y, x


print(f"After swapping {x} , {y}")