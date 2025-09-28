### Write a program to calculate area of circle

def circle(radius):
    area = 3.14 * (radius ** 2)
    return area

radius = int(input("Enter radius of circle:"))

res = circle(radius)

print(f"Area of circle is {res}")