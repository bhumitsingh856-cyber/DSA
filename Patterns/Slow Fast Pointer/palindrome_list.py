# Leetcode 234. Palindrome Linked List
def isPalindrome(head):
 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
        
        curr = slow
        prev=None
        while curr:
            next = curr.next
            curr.next = prev
            prev=curr
            curr=next
        first=head
        while prev:
            if(first.val!=prev.val):
                return False
            first=first.next
            prev=prev.next
        return True