### Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

print("Enter for Male = m or M and for Female = f or F")
gender = input("Enter the gender:")
age = int(input("Enter the age:"))

if(((gender == 'm'or 'M') and (age >= 21)) or ((gender == 'f' or 'F' )and (age >= 18))):
    print("Eligible for marriage.")
else:
    print("Not Eligible for marriage")