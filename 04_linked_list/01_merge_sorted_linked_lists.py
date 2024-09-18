class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_two_sorted_lists(list1, list2):
    """
    Merge the sorted lists and return the sorted list
    """

    left_previous = None
    left_head = list1
    right_head = list2
    head = left_head
    while right_head:
        current_head_value = left_head.val
        if current_head_value > right_head.val:
            temp = right_head.next
            right_head.next = left_head
            left_head.next = temp
        
