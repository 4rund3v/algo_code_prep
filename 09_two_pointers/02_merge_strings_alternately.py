

def merge_strings_alternately(word1: str, word2: str) -> str:
    """
    Merge the strings alternately
    """
    max_length = max(len(word1), len(word2))
    new_word = []
    for i in range(max_length):
        if i < len(word1):
            new_word.append(word1[i])
        if i < len(word2):
            new_word.append(word2[i])
    return "".join(new_word)
