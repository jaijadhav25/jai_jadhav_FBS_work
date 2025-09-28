# 2. Write a program to find maximum and minimum element in a list.

def max_min(li):
    max = li[0]
    min = li[0]
    for i in range(1, len(li)):
        if(li[i] > max):
            max = li[i]
    
    for j in range(1, len(li)):
        if(li[i] < min):
            min = li[i]
    return max,min


li = [50, 20, 30, 78, 40, 80, 10]
max , min = max_min(li)
print(f"Maximum number is {max}")
print(f"Minimum number is {min}")