"""
https://leetcode.com/problems/valid-palindrome/description/
"""

def check_valid_palindrome(s: str) -> bool:
    """
    Check if the given string is a valid palindrome
    """
    import string

    left_pointer = 0
    right_pointer = len(s) - 1
    s = s.lower()
    valid_chars = string.ascii_lowercase
    while left_pointer < right_pointer:
        left_char = s[left_pointer]
        while left_char not in valid_chars and left_pointer < right_pointer:
            left_pointer += 1
            continue
        right_char = s[right_pointer]
        while right_char not in valid_chars and left_pointer < right_pointer:
            if right_char not in valid_chars:
                right_pointer -= 1
                continue
        if left_char != right_char:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True

