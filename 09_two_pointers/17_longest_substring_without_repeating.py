

def longest_substring_without_repeating(s: str) -> int:
    window_start = 0
    window_end = 0
    curr_max = 0
    curr_char_set = set()
    while window_end < len(s):
        curr_char = s[window_end]
        print(f"considering char : {curr_char} character set : {curr_char_set}")
        if curr_char in curr_char_set:
            while curr_char in curr_char_set and window_start < window_end:
                curr_char_set.remove(s[window_start])
                window_start += 1
        curr_char_set.add(curr_char)
            
        curr_max = max(curr_max, window_end-window_start)
        print(f"The current max at iteration : [{window_end}] window:[{s[window_start: window_end+1]}] : {curr_max}")
        window_end += 1
    return curr_max+1


print(longest_substring_without_repeating(s="abcabcbb"))
