def create_run_length_encoding(s):
    char_counts = []
    curr_char_count = 1
    for i in range(1, len(s)): 
        curr_char = s[i]
        previous_char = s[i-1]
        if curr_char_count == 9 or curr_char != previous_char:
            char_counts.append(str(curr_char_count))
            char_counts.append(previous_char)
            curr_char_count = 0
            print(curr_char_count, curr_char)

        curr_char_count += 1
    char_counts.append(str(curr_char_count))
    char_counts.append(s[-1])
    return "".join(char_counts)

print(create_run_length_encoding("baaaaaaaaaaaabcccsfvvvsdfdfgax"))
