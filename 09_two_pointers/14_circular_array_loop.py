
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def move_to_pos(start, steps, size):
            move_by = (start + steps) % size
            if move_by < 0:
                return move_by + size
            return move_by

        def check_cycle(nums, pos, previous_direction):
            curr_direction = nums[pos] >= 0
            if curr_direction != previous_direction or (abs(nums[pos]%len(nums)) == 0):
                return False
            return True

        nums_size = len(nums)
        for curr_pos in range(nums_size):
            direction_forward = nums[curr_pos] > 0
            slow = fast = curr_pos
            while True:
                slow = move_to_pos(slow, nums[slow], nums_size)
                if not check_cycle(nums, slow, direction_forward):
                    break
            
                fast = move_to_pos(fast, nums[fast], nums_size)
                if not check_cycle(nums, fast, direction_forward):
                    break
                fast = move_to_pos(fast, nums[fast], nums_size)
                if not check_cycle(nums, fast, direction_forward):
                    break

                if slow == fast:
                    return True
        return False
