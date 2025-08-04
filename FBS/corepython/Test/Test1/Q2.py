### Write a program to calculate simple interest based on Principal, Rate and Time(SI = P*R*T/100)

principal = float(input("Enter the principal:"))
rate = float(input("Enter the rate:"))
time = float(input("Enter the time:"))

si = (principal * rate * time)/100

print(f"Simple interest is :{si}")