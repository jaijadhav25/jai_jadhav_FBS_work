# 11. Write a program to print all numbers which are divisible by m and n in the list.

def divisible(li,m,n):
    new_list = []
    for i in range(len(li)):
        if(li[i] % m == 0 and li[i] % n == 0):
            new_list.append(li[i])
    return new_list

li = [50, 20, 30, 78, 40, 80, 10, 58, 60, 50, 80]
print("Enter number to check divisible with m and n in list")
m = int(input("Enter first number"))
n = int(input("Enter second number"))
res = divisible(li,m,n)
print(f"Number that are divisable with {m,n} is {res}")