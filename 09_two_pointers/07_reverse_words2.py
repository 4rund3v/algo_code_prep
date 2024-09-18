"""
Reverse the words in a sentence, while maintaing the word order
"""

def reverse_word_chars(s: str) ->  str:
    def str_reverse(_s, start, stop):
        while start < stop:
            _s[start], _s[stop] = _s[stop], _s[start]
            start += 1
            stop -= 1
    start = 0
    s = list(s)
    for end in range(len(s)):
        if s[end] == " " or end == len(s) -1:
            end_idx = end if end == len(s) -1 else end - 1
            str_reverse(s, start, end_idx)
            start = end + 1
    return "".join(s)
