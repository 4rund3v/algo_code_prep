def is_valid_brackets(s):
    """
    Check if the brackets are valid
    """
    if not s or len(s) % 2 == 1:
        return False

    # TODO implement a stack, onto which the opened brackets are added
    # later when encountering a closing bracket, pop it
    brackets_opened = list()
    bracket_mapping = {"}": "{",
                       ")":"(",
                       "]":"["}  
    for bracket in s:
        if bracket in bracket_mapping:
            opened_bracket = brackets_opened.pop() if brackets_opened else None
            if bracket_mapping[bracket] != opened_bracket:
                return False
        else:
            brackets_opened.append(bracket)
    if brackets_opened:
        return False
    return True

if __name__ == "__main__":
    print(is_valid_brackets(s="([])"))
    print(is_valid_brackets(s="([}}])"))

