### Write a program to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter the cost price:"))
dicount = int(input("Enter the discount:"))

selling_price = (cost_price + (cost_price * (dicount/100)))

print(f'Selling price is:{selling_price}')

