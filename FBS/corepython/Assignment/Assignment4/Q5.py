### WAP to print Fibonacci series upto n.
num = int(input("Enter the number:"))
n1 = 0
n2 = 1
# for i in range(num):
#     print(n1, end=" ")
#     a = n1 + n2
#     n1 = n2
#     n2 = a
count = 0
while(count < num):
    print(f"{n1}",end=" ")
    a = n1 + n2
    n1 = n2
    n2 = a
    count += 1   