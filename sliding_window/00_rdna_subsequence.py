"""
Space optimization
 -> encode the characters 
"""


def repeated_dna_subsequence(sequence: str, k: int) -> str:
    """
	Keep moving through the string and find the sub strings of length k
	that keep repeating through the string.
    """
    dna_subsequences =  set()
    repeated_dna_subsequence = set()
    for window_start in range(len(sequence) - (k - 1)):
        window_end = window_start + k
        sub_string = sequence[window_start: window_end]
        if sub_string in dna_subsequences:
            repeated_dna_subsequence.add(sub_string)
        dna_subsequences.add(sub_string)
    return repeated_dna_subsequence



if __name__ == "__main__":
	sequence = "AAAAAAAAAAA"
	res = repeated_dna_subsequence	(sequence=sequence, k=10)
	print(f"Repeated subsequences are :: pattern: {sequence} \n\n {res}")
