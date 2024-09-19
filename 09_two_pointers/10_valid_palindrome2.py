
"""
Given a palindrome, wheck if by removing one char its again a palindrome
"""

def check_valid_palindrome(s:str) -> bool:
    def check_palindrome(_s, i, j):
        while i < j:
            if _s[i] != _s[j]:
                return False
            i += 1
            j -= 1
        return True
    removal_count = 1
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j] :
            return check_palindrome(s, i+1, j) or check_palindrome(s, i, j-1)
        i += 1
        j -= 1
    return True

