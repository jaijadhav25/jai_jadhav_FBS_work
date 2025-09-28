# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

def convert_words(text):
    words = [ ]
    word = ''
    for ch in text:
        if ch != " ":
            word += ch
        else:
            words.append(word)
            word = ''
    if word != " ":
        words.append(word)
    return words

def count_fq_words(words):
    freq_word = {}
    for char in words:
        if char in freq_word:
            freq_word[char] += 1
        else:
            freq_word[char] = 1
    return freq_word

text = "Python is great and Python is easy to learn"
words = convert_words(text)
dict = count_fq_words(words)
print(dict)