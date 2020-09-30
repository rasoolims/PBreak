import random

# Tags: {'PUNC', 'Ne', 'INT', 'DETe', 'Pe', 'NUM', 'CONJ', 'CONJe', 'RESe', 'CL', 'POSTP', 'PROe', 'V', 'N', 'P', 'ADV', 'PRO', 'DET', 'NUMe', 'RES', 'AJ', 'AJe', 'ADVe'}


"""
Paper reference by Bakhshizadeh and Tabibzadeh (2018): https://bit.ly/30nXgCz
"""

semi_space = "‌"


def plural_breaker(word):
    """
    Page 10 of the paper
    Converts "HA" or "A" for plurals
    """

    if word.endswith("ها") or word.endswith("های"):
        ending = ""
        if word.endswith("های"):
            ending = "ی"
            word = word[:-1]

        subword = word[:-2]
        if subword[-1] == semi_space:
            subword = subword[:-1]
        if subword[-1] not in {"ا", "و", "ه"}:
            word = subword + "ا" + ending

    return word

def deterministic_break(word):
    if word == "اگر":
        return "اگه"
    if word == "مگر":
        return "مگه"
    if word == "دیگر":
        return "دیگه"
    if word == "آخر":
        return "آخه"
    return word

def break_words(words, tags):
    broken_words = []
    broken_tags = []
    for i, (word, tag) in enumerate(zip(words, tags)):
        if random.random() < 0.8:
            word = deterministic_break(word)
        if tag in {"N", "Ne"}:
            if random.random() < 0.5:
                word = plural_breaker(word)

        broken_words.append(word)
        broken_tags.append(tag)
    return broken_words, broken_tags
