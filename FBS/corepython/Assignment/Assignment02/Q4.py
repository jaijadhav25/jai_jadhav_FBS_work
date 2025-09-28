### Write a program to calculate area of triangle and rectangle

## area of triangle
height = float(input("Enter the height of triangle:"))
base = float(input("Enter the base of triangle:"))

area_triangle = 0.5 * base * height

## area of rectangle 
length = float(input("Enter the length of rectangle:"))
breadth = float(input("Enter the breadth of rectangle:"))

area_rectangle = length * breadth

print(f"Area of triangle is {area_triangle}")
print(f"Area of rectangle is {area_rectangle}")