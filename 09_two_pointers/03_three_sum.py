"""
given a integer array
return the triplets which have distinct numbers which sum up to the given target
"""
def three_sum(nums: list):
    triplets = []
    nums.sort()
    for i in range(len(nums)-2):
        curr_target = target - nums[i]
        j = i + 1
        k = len(nums) -1
        while j < k:
            curr_sum = nums[j] + nums[k]
            if curr_sum == curr_target:
                triplets.append([nums[i], nums[j], nums[k]])
                break
            if curr_sum < curr_target:
                j += 1
            else:
                k -= 1

    return triplets
