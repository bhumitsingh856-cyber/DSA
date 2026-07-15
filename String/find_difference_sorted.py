
def diff(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[-1]


print(diff(s="", t="y"))
