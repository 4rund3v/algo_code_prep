class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_node(head, n):
    dummy = ListNode(0)
    dummy.next = head
    
    fast_head = dummy
    slow_head = dummy

    for i in range(n+1):
        fast_head = fast_head.next
    while fast_head is not None:
        fast_head = fast_head.next
        slow_head = slow_head.next

    # Removal of the node
    slow_head.next = slow_head.next.next

    return dummy.next

def remove_nth_node_alt(head, n):
    right = head
    left = head

    for i in range(n):
        right = right.next
    
    if not right:
        return head.next
    
    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return head
