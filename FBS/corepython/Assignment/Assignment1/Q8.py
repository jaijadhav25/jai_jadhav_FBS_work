### Write a program to convert days into years weeks and days 

days = int(input("Enter the number of days"))

years = days // 365

weeks = (days % 365) // 7

days = (days % 365) % 7

print(f"{years} years {weeks} weeks {days} days")