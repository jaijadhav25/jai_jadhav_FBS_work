# 2. Python Program to Concatenate Two Dictionaries Into One

def concatenate_dict(dict1, dict2):
    new_dict = {}
    for i in dict1:
        new_dict[i] = dict1[i]
    
    for j in dict2:
        new_dict[j] = dict2[j]

    return new_dict

dict1 = {1: "apple", 2: "banana"}
dict2 = {3: "cherry", 4: "date"}
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)
res = concatenate_dict(dict1, dict2)
print("After concatenate two dictionary result is:",res)