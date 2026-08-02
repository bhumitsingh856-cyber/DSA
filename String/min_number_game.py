#  Leetcode 2974. Minimum Number Game

def numberGame(nums):
    arr = []
    while len(nums)>0:
        alice=nums.pop(nums.index(min(nums)))
        bob = nums.pop(nums.index(min(nums)))
        arr.append(bob)
        arr.append(alice)
    return arr