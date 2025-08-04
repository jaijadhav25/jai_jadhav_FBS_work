### Write a program to enter P, T, R and calculate simple interest.

p = float(input('Enter the principle:'))
t = float(input('Enter the time:'))
r = float(input('Enter the rate:'))

si = (p * t * r) / 100

print(f'Simple Interest is:{si}')