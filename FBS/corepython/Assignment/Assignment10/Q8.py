# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

def duplicate(li):
    new_list = []
    for i in range(len(li)):
        new_list.append(li[i])
    return new_list

li = [50, 20, 30, 78, 40, 80, 10, 58, 60, 50, 80]
print("Orignal list",li)
new = duplicate(li)
print("Duplicate list",new)

# check for reference jai
li[0] = 99
print("Orignal list",li)
print("Duplicate list",new)