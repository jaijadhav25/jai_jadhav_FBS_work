# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

def even_odd(li):
    even = []
    odd = []
    for i in range(0,len(li)):
        if(li[i] % 2 == 0):
            even.append(li[i])
        else:
            odd.append(li[i])
    print(f"Even list is {even}")
    print(f"Odd list is {odd}")

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Orignal list is {li}")
even_odd(li)