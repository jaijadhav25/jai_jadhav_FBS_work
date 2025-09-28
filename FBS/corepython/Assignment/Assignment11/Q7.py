# 7. Python Program to Find the Intersection of Two Lists

def intersection(li1,li2):
    inter = []
    for i in li1:
        if i in li2 and i not in inter:
            inter.append(i)
    inter.sort()
    return inter

li1 = [1,4,5,2,3]
li2 = [2,3,7,8,4]
res = intersection(li1,li2)
print(li1)
print(li2)
print("Intersection of list is : ",res)