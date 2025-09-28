# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace(str):
    new_str = ''
    for i in str:
        if i == "a":
            new_str +="$"
        else:
            new_str += i
    print("After replacing occurances of 'a' with $ sting is:",new_str) 


str = input("Enter string:")
replace(str)