# Leetcode 2. Add Two Numbers
from implementation import LinkedList, Node


def dislpay(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next


def addTwoNumbers(l1, l2):
    carry = 0
    node = Node(0)
    temp = node
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sm = val1 + val2 + carry
        carry = sm // 10
        temp.next = Node(sm % 10)
        temp = temp.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return node.next


l1 = LinkedList().createLinkedList([2, 4, 3])
l2 = LinkedList().createLinkedList([5, 6, 4])

a = addTwoNumbers(l1, l2)
dislpay(a)
l1 = LinkedList().createLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = LinkedList().createLinkedList([9, 9, 9, 9])

a = addTwoNumbers(l1, l2)
dislpay(a)
