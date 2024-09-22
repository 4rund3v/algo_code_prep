from typing import List

def find_min_subarray(nums: List[int], target: int) -> int:
    if not nums:
        return 0
    min_subarray_length = len(nums)

    curr_sum = 0
    window_start = window_end = 0

    while window_end < len(nums):
        curr_num = nums[window_end]
        curr_sum += curr_num
        if curr_sum >= target:
            curr_length = window_end - window_start + 1
            min_subarray_length = min(curr_length, min_subarray_length)
            while curr_sum >= target:
                min_subarray_length = min(curr_length, min_subarray_length)
                num_popped = nums[window_start]
                curr_sum -= num_popped
                window_start -= 1
        window_end += 1
    return min_subarray_length

print(find_min_subarray(nums=[2,3,1,2,4,3], target=7))

