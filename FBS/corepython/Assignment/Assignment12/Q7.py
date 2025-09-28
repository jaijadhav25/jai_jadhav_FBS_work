# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

def length_string(str):
    count = 0
    for i in str:
        count += 1
    print("Length of string is: ",count)

str = input("Enter string:")
length_string(str)