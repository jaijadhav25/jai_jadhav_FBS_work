### WAP to print all integers upto n that aren’t divisible by 2 and 3.
num1 = int(input("Enter the starting of number:"))
num2 = int(input("Enter the ending of number:"))

for i in range(num1,num2 + 1):
    if(i % 2 !=0 and i % 3 != 0):
        print(f"{i}",end=",")

print("All the integers that aren't divisible by 2 and 3.")