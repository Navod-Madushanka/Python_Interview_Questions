def longest_common_subsequence(sequence1, sequence2):
    length1 = len(sequence1)
    length2 = len(sequence2)

    dp_table = [[0] * (length2 + 1) for _ in range(length1 + 1)]

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
    return dp_table[length1][length2]


sequence1 = "AGGTAB"
sequence2 = "GXTXAYB"
print(f"Length of LCS: {longest_common_subsequence(sequence1, sequence2)}")
