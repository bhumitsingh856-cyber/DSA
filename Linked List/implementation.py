class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def display(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return bool(not self.head)

    def createLinkedList(self, arr):
        dummy = Node(0)
        curr = dummy
        for val in arr:
            curr.next = Node(val)
            curr = curr.next
        self.head = dummy.next
        return self.head

    def append(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delhead(self):
        if self.isEmpty():
            return None
        del_val = self.head.val
        self.head = self.head.next
        return del_val

    def deltail(self):

        if self.isEmpty():
            return None
        if not self.head.next:
            del_val = self.head.val
            self.head = None
            return del_val
        curr = self.head
        while curr.next.next:
            curr = curr.next
        del_val = curr.next.val
        curr.next = None
        return del_val

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        return elements


# ll = LinkedList()

# ll.prepend(2)
# print(ll.display())
# ll.deltail()
# print(ll.display())

# l2 = LinkedList()
# l2.createLinkedList([1, 2, 3, 4, 5])
# print(l2.display())
