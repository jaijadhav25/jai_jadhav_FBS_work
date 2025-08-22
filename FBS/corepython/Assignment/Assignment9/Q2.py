# Write a program to check if given number is Armstrong or not using recursive function.

def power(num):
    if(num == 0):
        return 0
    else:
        return 1 + power(num // 10)

def is_armstrong(num, pow, sum=0):
    if(num == 0):
        return 0
    else:
        digit= num % 10
        return (digit ** pow) + is_armstrong(num // 10 , pow)


def armstrong(num):
    pow = power(num)
    return is_armstrong(num, pow)

num = int(input("Enter number to check armstrong or not:"))
res = armstrong(num)
if(res == num):
    print("It's an armstrong number.")
else:
    print("It's not an armstrong.")