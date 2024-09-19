
from typing import List

def calculate_maximum_subarray(nums: List[int]) -> int:
    n_size = len(nums)
    max_sum = nums[0]
    curr_sum = 0
    for i in range(n_size):
        curr_sum = max(curr_sum, 0) + nums[i]
        max_sum = max(max_sum, curr_sum)
        print(f" The iteration [{i}] the max sum is :: {max_sum}")
    return max_sum

print(calculate_maximum_subarray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4 ]))
