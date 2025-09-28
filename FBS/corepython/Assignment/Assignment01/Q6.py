### Write a program to input two angle from user and find third angle of the triangle

ang1 = float(input("Enter the first angle of triangle:"))
ang2 = float(input("Enter the second angle of triangle:"))

ang3 = 180 - ang1 - ang2

print(f"Third angle of triangle is {ang3}")