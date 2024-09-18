
"""
AlgoFind:
    Ducth National Flag problem
    - Three pointers
       - swap with left when val is 0
          - move left when the value is 0
          - increment current
       - move current when the value is 1
       - swap with right when the val is 2
          - move right when the value is 2

    Also solved using the binary search based partition problem, 
     - Partition left zeros
     - Partition right 1s
"""

def sort_colors(nums: list) -> None:
    """
    Sort the oclors in place, 0 followed by 1 followed by 2
    """
    zero_pointer = 0
    two_pointer = len(nums) - 1
    current_pointer = 0
    while current_pointer <= two_pointer:
        val = nums[current_pointer]
        if val == 0:
            nums[zero_pointer], nums[current_pointer] = nums[current_pointer], nums[zero_pointer]
            zero_pointer += 1 
            current_pointer += 1
        elif val == 2:
            nums[two_pointer], nums[current_pointer] = nums[current_pointer], nums[two_pointer]
            two_pointer -= 1
            current_pointer += 1
        else:
            # indicates that the current_pointer is at 1
            current_pointer += 1
    return nums

        
