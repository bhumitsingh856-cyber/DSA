# Leetcode 203. Remove Linked List Elements
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    curr = head
    temp = ListNode()
    temp.next = head
    prev = temp
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return temp.next
