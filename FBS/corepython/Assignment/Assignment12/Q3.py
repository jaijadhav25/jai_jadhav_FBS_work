# Python Program to Detect if Two Strings are Anagrams

def anagrams(str1, str2):
    if(len(str1) != len(str2)):
        print("string are not anagram")
    else:
        count1={}
        count2={}
        for ch in str1:
            if ch in count1:
                count1[ch]+=1
            else:
                count1[ch]=1
        for ch in str2:
            if ch in count2:
                count2[ch]+=1
            else:
                count2[ch]=1
    if(count1==count2):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")

str1=input("enter first string: ")
str2=input("enter second string: ")
anagrams(str1, str2)
