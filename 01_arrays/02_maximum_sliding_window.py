


def get_max_sliding_window(nums, k):
    """
    So instead of calculating the max at each window,
    keep a queue which has always k items,
    use a monotonic deque
    """
    print(nums)
    from collections import deque

    dec_q = deque()
    results = []
    pos = 0
    while pos < len(nums):
        print(f"Pos[{pos}] --> deque[{dec_q}] -> {[nums[i] for i in dec_q]}") 
        val = nums[pos]
        while len(dec_q) and nums[dec_q[-1]] <= val:
            dec_q.pop()
        dec_q.append(pos)
        if dec_q[0] == pos-k:
            dec_q.popleft()
        if pos >= k-1:
            results.append(nums[dec_q[0]])
        pos += 1
    return results

print(get_max_sliding_window(nums=[1,3,-1,-3,5,2,11,3,6,7], k=3))
