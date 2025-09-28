# 11. Python Program to replace every blank space with hyphen in a string.

def replace_space(str):
    new_str = ' '
    for i in str:
        if(i == ' '):
            new_str += '_'
        else:
            new_str += i
    return new_str

str = input("Enter string:")
res = replace_space(str)
print("After replacing space with hypen string is:",res)
