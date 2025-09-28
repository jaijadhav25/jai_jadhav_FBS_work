### S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

num = int(input("Enter the number :"))
sum = 0
for i in range(1,11):
    a = (num * i)/i
    sum = sum + a
print(sum)