### Write a program to find sum of following series using functions :
#   b. 1!+ 2! + 3! + 4!+..... + n!

def series(num):
    total_sum = 0
    for i in range(1,num+1):
        fact = 1
        for j in range(1,i+1):
            fact *= j
        total_sum += fact
    
    return total_sum

n = int(input("Enter number to find the sum of series till n : "))

res = series(n)

print(f"Sum of the sreies is {res}.")