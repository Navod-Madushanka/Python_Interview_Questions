def merge_alternately(word_1, word_2):
    string_parts = []

    length_1 = len(word_1)
    length_2 = len(word_2)
    i = 0

    while i < length_1 and i < length_2:
        string_parts.append(word_1[i])
        string_parts.append(word_2[i])
        i += 1

    if i < length_1:
        string_parts.append(word_1[i:])

    if i < length_2:
        string_parts.append(word_2[i:])

    return "".join(string_parts)


print(merge_alternately("abc", "pqr"))




