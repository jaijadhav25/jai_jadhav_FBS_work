# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

def display(str1, str2):
    count1 = 0
    count2 = 0
    for i in str1:
        count1 += 1
    
    for j in str2:
        count2 += 1
    
    if(count1 == count2):
        print(f"Both string having same length.\nstr1 = {str1}\nstr2 = {str2}")
    elif(count1 > count2):
        print("String first is larger:",str1)
    else:
        print("String second is larger:",str2)

str1 = input("Enter string 1 :")
str2 = input("Enter string 2 :")
display(str1, str2)
