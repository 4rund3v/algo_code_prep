


def longest_palindrome(s:str):
    def get_longest_palindrome_substring(_s, left_idx, right_idx):
        while left_idx >= 0 and right_idx < len(_s):
            if _s[left_idx] != _s[right_idx]:
                break
            left_idx -= 1
            right_idx += 1
        return left_idx + 1, right_idx - 1

    max_longest_length = 1
    max_longest_indexes = 0,0
    
    for i in range(1, len(s)-1):
        # Consider that i is the center of the palindrome
        # go left and go right check if the current char is the center of the larger substring
        odd_ids = get_longest_palindrome_substring(s, i-1, i+1)
        even_ids = get_longest_palindrome_substring(s, i-1, i)
        longest = max(even_ids, odd_ids, key=lambda x: x[1] - x[0])
        max_longest_indexes = max(max_longest_indexes, longest, key=lambda x: x[1] - x[0])
    return s[max_longest_indexes[0]: max_longest_indexes[1]+1]

print(longest_palindrome("abaxyzzyxf"))

