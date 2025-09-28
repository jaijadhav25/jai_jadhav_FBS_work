### Write a program to calculate profit or loss.


cp = int(input("Enter the cost price"))
sp = int(input("Enter the selling price"))

if(sp == cp):
    print("No profit no loss.")
elif(sp > cp):
    print("It is profit.")
else:
    print("It is loss.")