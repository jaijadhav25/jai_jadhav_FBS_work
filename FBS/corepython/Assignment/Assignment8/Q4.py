### Sum of all odd numbers between 1 to n

def odd(num):
    sum = 0
    for i in range(1,num+1):
        if(i % 2 != 0):
            sum += i
    return sum

n = int(input("Enter number to find sum the series of odd number till n :"))
res = odd(n)
print(f"Sum of all odd numbers between 1 to {n} is {res}")