# 2. Write a Python program to remove the intersection of a second set
# with a first set.

def remove_intersection(a, b):
    result = set()
    for i in a:
        found = False
        for j in b:
            if(i == j):
                found = True
                break
        if not found:
            result.add(i)
    return result
        
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}
print("set1:",set1)
print("set2",set2)
res = remove_intersection(set1, set2)

print("set1 after removing intersection with set2:", res)