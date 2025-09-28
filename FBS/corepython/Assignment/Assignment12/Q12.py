# 12. Python Program to count number of lowercase characters in a string.

def count_lower(str):
    count = 0
    for i in str:
        if('a'<= i <='z'):
            count += 1
    return count

str = input("Enter string:")
res = count_lower(str)
print("Number of lowercase characters in string:",res)