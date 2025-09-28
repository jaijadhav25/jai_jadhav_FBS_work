# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def difference(a, b):
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

print("Elements in set1 but not in set2:",difference(set1, set2))
print("Elements in set2 but not in set1:",difference(set2, set1))