### Calculate the cost of painting the following building’s walls (both interior andexterior). You need to accept area (one wall) and cost of both interior and exterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#2. It is upper view of building.)

area = float(input("Enter the area of wall:"))

interior_wall = int(input("Enter the no of interior wall:"))
exterior_wall = int(input("Enter the no of exterior wall:"))

interior_price = int(input("Enter the cost of interior wall painting:"))
exterior_price = int(input("Enter the cost of exterior wall painting:"))

area_of_all_interior_wall = area * interior_wall
area_of_all_exterior_wall = area * exterior_wall

interior_cost = area_of_all_interior_wall * interior_price
exterior_cost = area_of_all_exterior_wall * exterior_price

total_cost = interior_cost + exterior_cost

print(f"Interior cost is:{interior_cost} ")
print(f"Exterior cost is:{exterior_cost} ")

print(f"Total cost is:{total_cost}")