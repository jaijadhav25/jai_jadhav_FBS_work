# 7. Python Program to Remove the Given Key from a Dictionary

def remove(dict, key):
    new_dict = { }
    if key not in dict.keys():
        return "Key is not present in dictionary."
    else:
        for keys, values in dict.items():
            if(key != keys):
                new_dict[keys] = values
    return f"After removing given key dictionary is:{new_dict}"       

dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e':50}
key = input("Enter key you want to remove:")
dict2 = remove(dict, key)
print(dict2)