### e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter the number :"))
n = int(input("Enter the number to fin the value till n terms:"))
sum = 0
j = 1 
for i in range(1,n+1):
    if(i % 2 == 0):
        sum = sum - ((x*i)/j)
    else:
        sum = sum + ((x*i)/j)
    j +=2 

print(sum)