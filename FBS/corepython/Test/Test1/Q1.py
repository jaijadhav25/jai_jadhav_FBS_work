### Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:)

length = float(input("Enter the length of perimeter:"))
breadth = float(input("Enter the breadth of perimeter:"))
radius = float(input("Enter the radius of perimeter "))

area = (length * breadth) + (0.5 *3.14 * radius ** 2 )

perimeter = (length * 2) + breadth + (3.14 * radius)


print(f"Area is {area} ")
print(f'Perimeter is {perimeter}')