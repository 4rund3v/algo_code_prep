def two_sum(nums: list, target: int) -> list:
    """
    Given a list of integers
    find the pair of integers that add up to the target
    """
    # Cannot sort, since the indices are required
    # nums.sort()

    if not nums:
        return []

    current_value_positions = {}
    for pos, value in enumerate(nums):
        current_difference = target - value
        if current_difference in current_value_positions:
            return [pos, current_value_positions[current_difference]]
        current_value_positions[value] = pos
    return

"""
Time complexity of O(n)
Space Complexity of O(n)
"""
