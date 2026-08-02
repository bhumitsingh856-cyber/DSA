# Leetcode 2942. Find Words Containing Character
def findWordsContaining(words, x):
    arr = []
    for i in range(len(words)):
        if x in words[i]:
            arr.append(i)
    return arr


print(findWordsContaining(words=["leet", "code"], x="e"))
print(findWordsContaining(words=["abc", "xyz", "wxy"], x="a"))
