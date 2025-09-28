# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String

def remove_nth_index(str,n):
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str


str = input("Enter string:")
n = int(input("Enter index to remove:"))
new_str = remove_nth_index(str,n)
print("New string after removing:",new_str)
