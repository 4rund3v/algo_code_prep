

def crystal_ball_breaks(arr: List) -> int:
    """
    given a array of positions where the crystal ball breaks ( True/False)
    return the position at which it breaks
    """
    jump_amount = math.floor(mat.sqrt(len(arr)))

    for i in range(jump_amount, len(arr), jump_amount):
        if arr[i]:
            # Indicating the crystal ball breaks here
            break
    i -= jump_amount

    for j in range(jump_amount):
        if i >= len(arr):
            break
        if arr[i]:
            return i
        i += 1

    return -1

