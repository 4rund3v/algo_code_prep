

def detect_cycle(head) -> bool:
    
    if not head:
        return False
    slow = fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
