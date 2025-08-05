### A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST

product1 = int(input("Enter the price of 1 product:"))
product2 = int(input("Enter the price of 2 product:"))
product3 = int(input("Enter the price of 3 product:"))
product4 = int(input("Enter the price of 4 product:"))
product5 = int(input("Enter the price of 5 product:"))

total_product = product1 + product2 + product3 + product4 + product5
cal_gst = total_product * (18/100)
gst = total_product + cal_gst

print(f'Total price with gst is {gst}')