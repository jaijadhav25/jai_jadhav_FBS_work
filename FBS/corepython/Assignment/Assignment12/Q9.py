# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

def count_word_char(str):
    count_words = 1
    count_chr = 0
    for i in str:
        if i == ' ':
            count_words += 1
        else:
            count_chr += 1
    print("Word count in string :",count_words)
    print("Character count in string :",count_chr)

str = input("Enter string:")
count_word_char(str)
