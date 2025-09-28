### patterns 
#         1
#       1   1
#     1   2   1
#   1   3   3   1



coef = 1
for i in range(0,4):
    for j in range(0,4-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        if(j==0 or i==0):
            coef = 1
            print(coef,end="   ")
        else:
            coef = coef * (i-j+1)//j
            print(coef,end="   ")
    print()