
"""
Reverse words in a string
 1. reduce multiple spaces to single spaces
 2. revere each word
 3. try doing it in place ( reverse the entire string, then reverse the words
"""
import re

def reverse_words(s) -> str:
    def str_reverse(_s, start, stop):
        while start< stop:
            _s[start], _s[stop] = _s[stop], _s[start]
            start += 1
            stop -= 1

    # Strip the trailing spaces
    s = s.strip()
    s = re.sub(" +"," ", s)
    s = list(s)
    # Reverse the complete string
    str_reverse(s, 0, len(s)-1)
    print(s)
    start = 0
    for end in range(len(s)):
        if end == len(s)-1 or s[end] == " ":
            end_idx = end if end == len(s) - 1 else end - 1 
            str_reverse(s, start, end_idx)
            start = end + 1
    return "".join(s)



print(reverse_words("Hello there my good man!!"))
