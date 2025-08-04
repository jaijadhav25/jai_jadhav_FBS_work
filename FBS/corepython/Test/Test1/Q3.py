### Write a program to accept distance in km and convert it into meters and centimeters both.

km = float(input("Enter the distance in km:"))

meters = km * 1000

centimeters = meters * 100

print(f"After converting km into meter is {meters}")
print(f"After converting km into centimeter is {centimeters}")