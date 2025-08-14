n = int(input("Enter the number:"))
total_sum=0
total_sum_sequence = 0
for i in range(1,n+1):
    fact = 1
    # print(i)
    for j in range(1,i+1):
        fact = fact * j
    # print("factorial",fact)
    total_sum = i / fact
    total_sum_sequence += total_sum
    # print(total_sum)
print("Total sum of series is:",total_sum_sequence)
