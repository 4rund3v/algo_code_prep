
"""
Palindrome in a linked list
"""
class LinkedListNode():
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next
    def __str__(self):
        return f"<Node val:{self.val} next:{ self.next} >"

def reverse_linked_list(_head):
    curr = _head
    prev = None
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def check_palindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # now slow is at the mid
    point_of_change = slow
    print(f"Mid point of the ll -> {slow}")
    new_head = reverse_linked_list(slow)
    print(f"New Head of the reveresed linked list -> {new_head}")
    check = compare_linked_lists(head, new_head)
    print(head)
    old_head = reverse_linked_list(new_head)
    print(head)
    point_of_change.next = old_head
    return check

def compare_linked_lists(head_a, head_b):
    curr_a = head_a
    curr_b = head_b
    while curr_a and curr_b:
        print(f"Comparing :: {curr_a.val} and {curr_b.val}")
        if curr_a.val != curr_b.val:
            return False
        curr_a = curr_a.next
        curr_b = curr_b.next
    return True

def create_ll(items):
    head = LinkedListNode(items[0])
    prev = head
    for i in range(1, len(items)):
        curr = LinkedListNode(items[i])
        prev.next = curr
        prev = curr
    return head

def print_ll(head):
    curr = head
    while curr:
        print(f"\t {curr.val}",)
        curr = curr.next
    return 


if __name__ == "__main__":
    a_head = create_ll(items=[10,2,7,6,7,2,10])
    check_palindrome(a_head)
    # print(f"Creating the base linked list")
    # print_ll(a_head)
    # ra_head = reverse_linked_list(a_head)
    # print_ll(ra_head)

