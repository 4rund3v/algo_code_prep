


def check_pattern_exists(s, p):
    PRIME = 3
    print(s)
    def calculate_hash(p, exp=0):
        print(f"\t\t Calculating the hash for :[{p}] and exp:{exp}")
        temp_hash = 0
        for char in p:
            temp_hash += ord(char)*pow(PRIME, exp)
            exp += 1
        return temp_hash

    def calculate_rolling_hash(leaving_char_pos, new_char_pos, current_hash, _s):
        print(f"Provided hash: {current_hash}")
        print(f"\t Calculating the rolling hash for :: -[{_s[leaving_char_pos]}] +[{_s[new_char_pos]}] --> {current_hash}")
        temp_hash = current_hash - ord(_s[leaving_char_pos])
        temp_hash = temp_hash // PRIME
        temp_hash += calculate_hash(_s[new_char_pos], exp=2)
        print(f"\tNew Roll Hash generated :: {temp_hash}")
        return temp_hash

    pattern_len = len(p)
    p_hash = calculate_hash(p)
    print(f"Pattern Hash:  {p} is {p_hash}")

    window_start = 0
    window_end = pattern_len
    curr_word_hash = calculate_hash(s[window_start:window_end])
    print(f"Word hash:  {s[:pattern_len]} is {curr_word_hash}")    
    while window_end < len(s)-1:
        curr_word = s[window_start: window_end]
        curr_hash = calculate_hash(curr_word)
        print(f"The current word:: [{curr_word}] is {curr_hash}")
        if curr_word_hash == p_hash and s[window_start: window_end] == p:
            print(f"The pattern matches with the string in the sentence")
            print(f"The word: {curr_word} --> {p}")
            return True
        curr_word_hash = calculate_rolling_hash(window_start,
                                                window_end,
                                                curr_word_hash,
                                                s)
        print(f"The rolling hash calculated is:: {curr_word_hash}")
        window_start += 1
        window_end += 1
    return False

check_pattern_exists(s="sesller, She sells sea shells at the sea shore", p="sea")




























