# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

def replace_space(str):
    new_str = " "
    for i in str:
        if i == ' ':
            new_str += '_'
        else:
            new_str += i
    print("After replacing space with hypen string is:",new_str)

str = input("Enter string:")
replace_space(str)
