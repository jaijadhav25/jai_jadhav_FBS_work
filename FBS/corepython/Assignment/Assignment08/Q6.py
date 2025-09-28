### Write a program to find print the following Fibonacci series using functions:
#   1 1 2 3 5 8 n terms

def fibonacci(num):
    a = 1
    b = 0
    for i in range(1,num):
        c = a + b
        print(c,end=" ")
        a = b
        b = c

n = int(input("Enter number to find fibonacci series till n :"))

fibonacci(n)