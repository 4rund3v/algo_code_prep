
"""
Given the string input, try to move the characters by the provided k places
all lowercase
"""

def caeser_encryptor(s, k):
    """
    ascii value of a = 97 and z = 122
    """
    def get_new_char(_ch, k):
        new_ascii_val = ord(_ch) + k
        return chr((96+(new_ascii_val%122)) if new_ascii_val > 122 else new_ascii_val)
    k = k % 26
    cipher_text = []
    for ch in s:
        cipher_text.append(get_new_char(ch, k))
    return "".join(cipher_text)


print(caeser_encryptor("xyz", 2))
