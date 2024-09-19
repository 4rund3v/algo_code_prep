

"""
Find the duplicate number in an array of [1, n] items, with size n+1 ezactly one duplicate
try doing with constant space and linear time
 - constant space - no hash/ no set 
"""


def find_duplicate(nums: List) -> int:
    """
    Given a integer list
    return the duplicate number
    """
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break
    slow = nums[0]
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    return fast

