### Write a program to check if entered year is a leap year or not.

def leap_year(num):
    if(num % 4 == 0):
        if(num % 100 == 0):
            if(num % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
num = int(input("Enter year to check leap year:"))

res = leap_year(num)
if(res):
    print(f"{num} is leap year.")
else:
    print(f"{num} is not a leap year.")