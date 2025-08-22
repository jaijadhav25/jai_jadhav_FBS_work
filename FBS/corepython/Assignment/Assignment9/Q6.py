# Write a program to print Fibonacci series using recursion.
def fabo(num , a=0 ,b=0):
    if(num > 0):
        c = a + b
        print(c , end=" ")
        fabo(num-1, b, c)

num = int(input("Enter number to find fibonacci serise: "))
a = -1
b = 1
fabo(num , a, b)
