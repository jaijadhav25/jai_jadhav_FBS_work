### WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def digit_sepreation(num):
    count = 0
    while(num > 0):
        num = num // 10
        count += 1
    return count

def power_sum(num):
    sum = 0
    power = digit_sepreation(num)
    while(num > 0):
        digit = num % 10
        sum = sum + digit ** power
        num = num // 10
    return sum

def armstrong(num):
     arm = power_sum(num)
     if(arm == num):
         return True
     else:
         return False
    

num = int(input("Enter number to check armstrong or not :"))

res = armstrong(num)

if(res):
    print(f"{num} is armstrong.")
else:
    print(f"{num} is not armstrong.")