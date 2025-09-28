# 1. Python Program to Add a Key-Value Pair to the Dictionary

def add_key_value(num):
    dict = { }
    for i in range(num):
        key = input("Enter the key:")
        value = input("Enter the value:")
        dict[key]=value
    return dict

num = int(input("Enter the number of key-value pair you want to add:"))
dict = add_key_value(num)
print("Dictionary :",dict)