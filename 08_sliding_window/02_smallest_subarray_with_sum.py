"""
find the smallest subarray with the target sum or greater
"""

def get_smallest_subarray_with_target_sum(nums: list, target: int) -> int:
    """
    find the smallest subarray with the target sum or greater
    """
    min_arr_len = len(nums)
    running_sum = window_start = 0
    target_met = False
    for window_end in range(len(nums)):
        running_sum += nums[window_end]
        while running_sum >= target:
            target_met = True
            curr_len = (window_end - window_start) + 1
            if curr_len < min_arr_len:
                min_arr_len = curr_len
            running_sum -= nums[window_start]
            window_start += 1        
    return min_arr_len if target_met else 0

if __name__ == "__main__":
    res = get_smallest_subarray_with_target_sum(nums=[2, 1, 5, 2, 3, 2], target=7)
    print(f"The smallest subarray is :: {res}")