"""
Given two sentences, find the uncommon words
"""
def uncommon_words_from_sentences(sentence1, sentence2):
    words_from_sentence1 = {}
    words_from_sentence2 = {}
    for word in s1.split():
        if word not in words_from_sentence1:
            words_from_sentence1[word] = 0
        words_from_sentence1[word] += 1
    for word in s2.split():
        if word not in words_from_sentence2:
            words_from_sentence2[word] = 0
        words_from_sentence2[word] += 1
    unique_words_from_sentence1 = set([key for key,val in words_from_sentence1.items() if val == 1 and key not in words_from_sentence2 ])
    unique_words_from_sentence2 = set([key for key,val in words_from_sentence2.items() if val == 1 and key not in words_from_sentence1])
    unique_words = unique_words_from_sentence1.symmetric_difference(unique_words_from_sentence2)
    # unique_words = words_from_sentence1 ^ words_from_sentence2

    return unique_words

def uncommon_words_from_sentences_alt(sentence1, sentence2):
    from collections import Counter
    all_words = sentence1.split() + sentence2.split()
    word_count = Counter(all_words)
    unique_words = [word for word in word_count if word_count[word] == 1]
    return unique_words

