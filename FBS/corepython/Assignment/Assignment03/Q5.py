### Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

ang1 = int(input("Enter the first angle:"))
ang2 = int(input("Enter the second angle:"))
ang3 = int(input("Enter the third angle:"))

if(ang1 == ang2 and ang2 == ang3 and ang1 == ang3 ):
    print("The triangle is equilateral triangle:")
elif(ang1 == ang2 or ang1 == ang3 or ang2 == ang3):
    print("The triangle is isosceles triangle:")
else:
    print("The triangle is scalene triangle:")
