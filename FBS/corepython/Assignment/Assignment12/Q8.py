# 8. Python Program to Remove the Characters of Odd Index Values in a
# String

def remove_odd_index(str):
    new_str = ''
    for i in range(len(str)):
        if(i % 2 == 0):
            new_str += str[i]
    print("After removing characters of odd index string is:",new_str)

str = input("Enter string:")
remove_odd_index(str)
