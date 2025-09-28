# 5. Python Program to Sum All the Items in a Dictionary

def sum_item(dict):
    sum = 0
    for i in dict.values():
        sum += i
    
    return sum

dict = {'a': 10, 'b': 20, 'c': 30}
res = sum_item(dict)
print("Sum of all items in dictionary is:",res)