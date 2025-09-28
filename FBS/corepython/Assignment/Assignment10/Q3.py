# 3. Write a program to find the second largest element in the list.

def second_max(li):
    max = li[0]
    smax = 0
    for i in range(1, len(li)):
        if(li[i] > max):
            smax = max
            max = li[i]
        elif(li[i] > smax):
            smax = li[i]
    return smax


li = [50, 20, 30, 78, 40, 80, 10]
smax = second_max(li)
print(f"Second maximum number is {smax}")