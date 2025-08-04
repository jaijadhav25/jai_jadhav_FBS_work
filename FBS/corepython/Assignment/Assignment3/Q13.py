### Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

units = int(input("Enter the electricity units:"))
bill = 0
if(units > 0):
    if(units <= 50 ):
        bill = units * 0.5
    elif(units <= 150):
        bill = (50 * 0.5)+(units - 50) * 0.75
    elif(units <= 250):
        bill = (50 * 0.5) + (100 * 0.75) + (units - 150) * 1.20
    else:
        bill = (50 * 0.5) + (100 * 0.75 ) +(100 * 1.20) + (units - 250) * 1.50
else:
    print("Invalid input")

subcharge = bill * (20/100)
total_bill = bill + subcharge

print(f'Total electricity bill is:{total_bill}')