# Leetcode 347. Top K Frequent Elements

def topKFrequent( nums, k):
    hmap={}
    for i in nums:
        hmap[i]=hmap.get(i,0)+1
    return sorted(hmap, key=hmap.get,reverse=True)[:k]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(topKFrequent(nums = [1], k = 1))