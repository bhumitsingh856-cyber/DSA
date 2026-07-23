# Leetcode 520
def detectCapitalUse(word):

    if word.isupper() or word.islower():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True
    else:
        return False

print(detectCapitalUse("FlaG"))
