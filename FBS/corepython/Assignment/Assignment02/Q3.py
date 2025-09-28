### Convert distant given in feet and inches into meter and centimeter.

f = float(input("Enter the feet:"))
i = float(input("Enter the inches:"))

d = ((f * 30.48) + (i * 2.54)) / 100

e = d * 100

print(f"{d} meters")

print(f"{e} centimeters")
