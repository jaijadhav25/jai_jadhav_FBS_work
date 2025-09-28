# 6. Python Program to Multiply All the Items in a Dictionary

def multiply_items(dict):
    mul = 1
    for i in dict.values():
        mul *= i

    return mul

dict = {'a': 10, 'b': 20, 'c': 30}
res = multiply_items(dict)
print("Multiplication of items in dictionary is :",res)