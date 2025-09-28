### Write a program to check if given number is Armstrong number or not.
#   (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter the number:"))
temp1 = num
temp2 = num
power = 0
sum = 0
while(temp1 > 0):
    digit = temp1 % 10
    power = power + 1
    temp1 = temp1 // 10

while(temp2 > 0):
    digit = temp2 % 10
    sum = sum + digit ** power
    temp2 = temp2 // 10
if(sum == num):
    print(f"It is armstrong number {num} ")
else:
    print(f"It is not armstrong number {num}")