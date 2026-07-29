# Leetcode 876. Middle of the Linked List
from implementation import LinkedList, Node, display


def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


ll = LinkedList().createLinkedList([1, 2, 3, 4, 5, 6])
res=middleNode(ll)
display(res)
