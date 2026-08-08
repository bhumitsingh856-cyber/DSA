# Leetcode 83. Remove Duplicates from Sorted List


def deleteDuplicates(head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
