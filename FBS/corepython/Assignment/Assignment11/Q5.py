# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.

li = ["apple", "kiwi", "banana", "cherry", "fig", "grapes"]
print("Oirgnal list:",li)

li.sort(key=len)

print("Sorted list:",li)