# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

def find_pair(li, target):
    pair = []
    n = len(li)
    for i in range(n):
        for j in range(i, n):
            if li[i] + li[j] == target:
                pair.append((li[i],li[j]))
    return pair


set1 = {1,2,3,4,5,6,7,8,9}
li = list(set1)
target = int(input("Enter the target you want to achive:"))

pairs = find_pair(li, target)
print(f"Pairs with sum {target} are: {pairs}")