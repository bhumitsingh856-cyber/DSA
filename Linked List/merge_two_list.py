# LeetCode 21. Merge Two Sorted Lists
from implementation import LinkedList, Node, display


def mergeTwoLists(list1, list2):
    new_list = Node(0)
    temp = new_list
    while list1 and list2:
        val1 = list1.val
        val2 = list2.val
        if val1 <= val2:
            temp.next = Node(val1)
            list1 = list1.next
        else:
            temp.next = Node(val2)
            list2 = list2.next
        temp = temp.next
    if list1:
        temp.next = list1
    else:
        temp.next = list2
    return new_list.next


l1 = LinkedList().createLinkedList([1, 2, 2, 3, 4, 5])
l2 = LinkedList().createLinkedList([-1, 3, 5])
res = mergeTwoLists(l1, l2)
display(res)

print()

l1 = LinkedList().createLinkedList([1, 2, 4])
l2 = LinkedList().createLinkedList([1, 3, 4])
res = mergeTwoLists(l1, l2)
display(res)
