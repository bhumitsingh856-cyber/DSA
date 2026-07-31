# Leetcode 2114. Maximum Number of Words Found in Sentences
def mostWordsFound(sentences):
    max_len = 0
    for i in sentences:
        arr = i.split()
        max_len = max(max_len, len(arr))
    return max_len


print(
    mostWordsFound(
        [
            "alice and bob love leetcode",
            "i love eating vanilla ice cream",
            "sybil fischer ate a slice of pizza",
        ]
    )
)
print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))
