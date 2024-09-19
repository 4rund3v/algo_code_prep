
class LinkedListNode():
    def __init__(self, val=0, next: LinedListNode=None):
        self.val = val
        self.next = next

def middle_linked_list(head: LinkedListNode) -> LinkedListNode:
    slow = head
    fast = head
    # fast = head.next # if you want the first middle node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

