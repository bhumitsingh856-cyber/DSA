# Leetcode 206. Reverse Linked List
from implementation import LinkedList, Node, display

def reverseLinkedList(head):
    if not head:
        return None
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


ll = LinkedList().createLinkedList([1, 2, 3, 4, 5])
a = reverseLinkedList(ll)
display(a)
