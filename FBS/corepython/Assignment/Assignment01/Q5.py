### Write a program to enter P, T, R and calculate compound interest.

p = float(input('Enter the principle:'))
t = float(input('Enter the time:'))
r = float(input('Enter the rate:'))

a = (p * ( 1 + ( r / 100 )) ** t ) - p

print(f'Compund Interest is:{a}')