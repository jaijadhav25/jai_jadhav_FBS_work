# 5. Python Program to Count the Number of Vowels in a String

def count(str):
    count = 0
    for i in str:
        if i in "AEIOUaeiou":
            count += 1
    print("Count of vowels in string is:",count)

str = input("Enter string:")
count(str)