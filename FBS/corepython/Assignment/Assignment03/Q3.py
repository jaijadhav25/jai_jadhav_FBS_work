### Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1 = int(input("Enter the first angle of triangle:"))
ang2 = int(input("Enter the second angle of triangle:"))
ang3 = int(input("Enter the third angle of triangle:"))

total_angle = ang1 + ang2 +ang3

if(total_angle == 180):
    print("It is a triangle")
else:
    print("It is not a triangle")