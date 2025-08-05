### Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

length_wall = int(input("Enter the length of wall:"))
breadth_wall = int(input("Enter the breadth of wall:"))
interior_cost = (int(input("Enter the cost of painting:")))

area = (length_wall * breadth_wall) * 4 

total_cost_of_painting = area * interior_cost

print(f"Total cost for painting is {total_cost_of_painting}")