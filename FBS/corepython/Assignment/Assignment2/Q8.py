### Write a program to swap two numbers using third variable.

x = int(input("Enter the number:"))
y = int(input("Enter the number:"))

print(f"Before swapping {x} , {y}")


z = x
x = y
y = z

print(f"After swapping {x} , {y}")