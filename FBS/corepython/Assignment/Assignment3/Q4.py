### Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side:"))
side3 = int(input("Enter the third side:"))

if((side1+side2) > side3 and (side2+side3) > side1 and (side1+side3) > side2):
    print("It is a triangle.")
else:
    print("It is not a triangle") 