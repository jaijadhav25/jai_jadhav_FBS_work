# 4. Write a program to reverse the list.

def reverse(li):
    rev_li = []
    for i in range(len(li) - 1, -1, -1):
        rev_li.append(li[i])
    return rev_li

li = [50, 20, 30, 78, 40, 80, 10]
res = reverse(li)
print(f"Original list is {li}")
print(f"Reversed list is {res}")