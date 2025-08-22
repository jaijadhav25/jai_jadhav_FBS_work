# Write a program to reverse a given number using recursive function.

def reverse(num, rev=0):
    if(num == 0):
        return rev
    else:
        rev = (rev * 10 ) + (num % 10)
        return reverse(num // 10 ,rev)


num = int(input("Enter number to find reverse:"))
res = reverse(num)
print(f"Reverse of {num} is {res}.")