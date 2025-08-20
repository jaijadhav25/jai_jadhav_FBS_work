def reverse(num,rev=0):
    if(num == 0):
        return rev
    else: 
        rev = (rev * 10)+(num % 10) 
        return reverse(num // 10 , rev)
    
def pallindrome(num):
    if(num == reverse(num)):
        return True
    else:
        return False

num = int(input("Enter number to check pallindrome or not :"))
res = pallindrome(num)
if(res):
    print("It is pallindrome.")
else:
    print("It is not pallindrome.")
