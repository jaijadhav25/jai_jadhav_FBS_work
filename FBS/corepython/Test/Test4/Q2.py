def fact(num):
    if(num == 1):
        return 1
    else:
        return num * fact(num-1)

num = int(input("Enter number to find the factorial of number"))
res = fact(num)
print(res)