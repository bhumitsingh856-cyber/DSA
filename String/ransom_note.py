# Leetcode 383. Ransom Note
def canConstruct(ransomNote, magazine):
        rmap={}
        mmap={}
        for i in ransomNote:
            rmap[i]=rmap.get(i,0)+1
        for i in magazine:
            mmap[i]=mmap.get(i,0)+1
       
        for i in rmap:
            if(not rmap.get(i) <= mmap.get(i)):
                return False
        return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aab", "baa"))