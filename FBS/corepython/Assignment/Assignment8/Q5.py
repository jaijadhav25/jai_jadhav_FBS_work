### Sum of all prime numbers between 1 to n

def prime(num):
        for j in range(2,num//2 + 1):
            if(num % j == 0):
                return False
        else:
            return True
        
def series(num):
    sum = 0 
    for i in range(2,num+1):
        if prime(i):
            sum +=i
    return sum


n = int(input("Enter number to find Sum of prime number series till n :"))

res = series(n)

print(f"Sum of prime number series is {res}")