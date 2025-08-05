### A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
#   for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
#   length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
#   cost of fencing the field.

radius = 20
length = 50
breadth = 40

perimeter_of_field = (length *2 )+ breadth + (3.14 * radius)

total_price = (perimeter_of_field * 35)*5

print(f"Total price is {total_price}")