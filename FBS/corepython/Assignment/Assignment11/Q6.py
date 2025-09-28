# 6. Python Program to Find the Union of two Lists

def union(li1,li2):
    union_list = li1.copy()
    for i in li2:
        if i not in union_list:
            union_list.append(i)
    union_list.sort()
    return union_list


li1 = [1,4,5,2,3]
li2 = [2,3,7,8,4]
res = union(li1,li2)
print(li1)
print(li2)
print("Union of list is : ",res)