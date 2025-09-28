# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

def sort_word(word):
    char = []
    for c in word:
        char.append(c)
    # print(char)

    for i in range(1, len(char)):
        for j in range(0, len(char) - 1):
            if(char[j] > char[j + 1]):
                char[j], char[j + 1] = char[j + 1], char[j]
    # print(char)
    
    sorted_words = ""
    for c in char:
        sorted_words += c
    return sorted_words

def group_anagrams(words):
    groups = {}

    for word in words:
        key = sort_word(word)

        if key not in groups:
            groups[key] = set()
        groups[key].add(word)

    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)

print("Grouped Anagrams:")
for group in result:
    print(group)