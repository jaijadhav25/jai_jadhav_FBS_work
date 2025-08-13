### Find the sum of a geometric series from 1 to n where the common ratio is 2.
### explaination with example
# The geometric series is calculated as follows:
# 1 + 2^1 + 2^2 + ... + 2^(n-1)
# For example, if n = 5, the series would be:
# 1 + 2 + 4 + 8 + 16 = 31

n = int(input("Enter the number:"))
gemotric_series=0
for i in range(0,n):
    sum = 2**i
    gemotric_series += sum
print(gemotric_series)