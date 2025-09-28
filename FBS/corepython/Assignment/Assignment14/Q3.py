# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

def get_word(li):
    words = []
    for line in li:
        for word in line.split():
            words.append(word)
    return words

def frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


lines = [
    "apple orange banana",
    "apple mango banana",
    "grape orange apple"
]


words = get_word(lines)
unique_words = set(words)
frequency_words = frequency(words)

print("All words:",words)
print("Unique words:",unique_words)
print("Frequency of words:",frequency_words)