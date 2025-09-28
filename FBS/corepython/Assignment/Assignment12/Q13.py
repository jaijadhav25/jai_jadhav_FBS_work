# 13. Python Program to count number of digits and letters in a string.

def count_digit_char(str1):
    digit = 0
    char = 0
    for i in str1:
        if('0' <= i <= '9'):
            digit += 1
        elif('a' <= i <= 'z' or 'A' <= i <= 'Z'):
            char += 1
    return char, digit
    

str1 = input("Enter string:")
char, digit=count_digit_char(str1)
print("Count of digits in string:",digit)
print("Count of character in string:",char)