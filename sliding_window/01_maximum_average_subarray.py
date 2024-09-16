"""
Concept of having a current window and moving the elements in and out as required
"""

def calculate_averages_subarray(nums: list, k: int) -> float:
    """
    Given a list of integers find the average of all the k subarrays
    """
    result_averages = []
    running_sum = window_start = 0
    for window_end in range(len(nums)):
        running_sum += nums[window_end]
        if window_end >= k - 1:
            result_averages.append(running_sum/k)
            running_sum -= nums[window_start]
            window_start += 1
    return result_averages


def calculate_max_average_subarray(nums: list, k: float) -> float:
    """
    Given the list of nums find the maximum average of the subarray of size k
    """
    windowstart = windowend = running_sum = 0
    max_sum = float("-inf")
    for windowend in range(len(nums)):
        running_sum += nums[windowend]
        if windowend >= k-1:
            if running_sum > max_sum:
                max_sum = running_sum
            running_sum -= nums[windowstart]
            windowstart += 1
    return max_sum/k


if __name__ == "__main__":
    print(f"The averages is :: ", calculate_averages_subarray(nums=[1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))
    print(f"The max average is :: ", calculate_max_average_subarray(nums=[1,12,-5,-6,50,3], k=4))