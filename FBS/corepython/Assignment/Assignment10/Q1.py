# 1. Write a program to find sum of all elements of list

def sum_list(li):
    sum = 0
    for i in range(0, len(li)):
        sum = sum + li[i]
    return sum


li = [10, 20, 30, 78, 40, 80]
print("Sum of all elements of list is:",sum_list(li))