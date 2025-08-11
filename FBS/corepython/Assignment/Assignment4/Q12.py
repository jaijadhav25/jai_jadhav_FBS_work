### 12. WAP to print Armstrong number within a given range

start = int(input("Enter the starting number:"))
end = int(input("Enter the ending number:"))

for i in range(start , end + 1):
    temp = i
    digit_count = 0
    while(temp > 0):
        d = temp % 10
        digit_count += 1 
        temp = temp // 10
    sum = 0
    temp2 = i    
    while(temp2 > 0):
        d2 = temp2 % 10
        sum = sum + (d2 ** digit_count)
        temp2 = temp2 // 10
    if(sum == i):
        print(f"{i}",end=",") 
else:
    print("This are armstrong number.")