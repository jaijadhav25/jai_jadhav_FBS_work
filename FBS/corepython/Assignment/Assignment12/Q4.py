# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

def exchange(str):
    n = len(str)
    if n <= 1 :
        return str
    new_string = ''
    new_string = str[-1] + str[1:n-1] + str[0]
    return new_string
    

str = input("Enter string:")
res = exchange(str)
print("After exchanging first character with last character sting is:",res)