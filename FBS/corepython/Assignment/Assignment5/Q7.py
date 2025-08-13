### Write a program to print first n prime numbers.
num = int(input("Enter the number to print first n prime number:"))

for i in range(2,num+1):
    for j in range(2,(i//2 + 1)):
        if( i % j == 0 ):
            break
    else:
        print(i,end=",")
