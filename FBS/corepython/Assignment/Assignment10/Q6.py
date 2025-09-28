# 6. Write a program to remove duplicates from the list.

def remove_duplicate(li):
    unique = []
    for i in li:
        if i not in unique:
            unique.append(i)
    return unique
    

li = [50, 20, 30, 78, 40, 80, 10, 58, 60, 50, 80]
print("Origanal list",li)
l1=remove_duplicate(li)
print("After removing duplicates:",l1)
