# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

def get_shortest_word(words):
    shortest = words[0]
    for w in words:
        if(len(w) < len(shortest)):
            shortest = w
    return shortest

def longest_common_prefix(words):
    if len(words) == 0:
        return ""
    
    shortest = get_shortest_word(words)
    prefix = ""

    for i in range(len(shortest)):
        ch = shortest[i]

        same = True
        for w in words:
            if w[i] != ch:
                same = False
                break

        if same:
            prefix += ch
        else:
            break

    return prefix

words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(words))
li = ['gane','ganes','ganesh','gan']
print("Longest Common Prefix:", longest_common_prefix(li))