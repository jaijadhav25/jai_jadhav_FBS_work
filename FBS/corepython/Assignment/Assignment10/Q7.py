# Write a program to create a new list from existing list which contains cube of each number of list.

def cube_list(li):
    new_list = []
    for i in range(len(li)):
        n = li[i] ** 3
        new_list.append(n)
    return new_list

li = [50, 20, 30, 78, 40, 80, 10, 58, 60, 50, 80]
print("Orignal list",li)
new = cube_list(li)
print("Cube of orignal list",new)