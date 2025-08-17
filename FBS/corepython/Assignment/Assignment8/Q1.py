### Write a program to calculate area of rectangle

def rectangle(length,breadth):
    area = length * breadth
    return area


length = int(input("Enter the length of rectangle:"))
breadth = int(input("Enter the breadth of rectangle:"))

res = rectangle(length , breadth)

print(f"Area of rectangle is {res}")