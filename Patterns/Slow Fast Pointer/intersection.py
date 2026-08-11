# Leetcode 160. Intersection of Two Linked Lists
def getIntersectionNode(headA, headB):
    pA , pB = headA , headB
    while pA!=pB:
        if pA:
            pA=pA.next
        else:
            pA=headB
        if pB:
            pB=pB.next
        else:
            pB=headA
    return pA