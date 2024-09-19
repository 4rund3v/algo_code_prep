
"""
We need to keep track of the frequencies of the letters in each string, and the frequencies of letters that the different strings have in common.
"""

def common_characters(words: str) -> str:
    from collections import Counter

    common_char_counter = Counter(words[0])
    result = []
    for word in words[1:]:
        current_char_counter = Counter(word)
        for letter in common_char_counter.keys():
            common_char_counter[letter] = min(current_char_counter[letter],
                                      common_char_counter[letter])
    for letter, count in common_char_counter.items():
        for _ in range(count):
            result.append(letter)
    return result


def common_characters_alt(words: str) -> str:
    common_char_counter = [2**31 - 1 ] * 26
    result = []
    for word in words[]:
        current_char_counter = [0]*26
        for char in word:
            current_char_counter[ord(char) - char('a')] += 1
        for i in range(26):
            common_char_counter[i] = min(current_char_counter[i],
                                         common_char_counter[i])
    for i in range(26):
        for _ in range(common_char_counter[i]):
            result.append(chr(i + ord('a')))
    return result
