'''
Minimum edit distance using dynamic programming Bottom up approach
'''

def min_edit_distance_dp(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    # Create a table to store results of subproblems
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
    ops = [["" for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    # Initialize the table
    for i in range(len_s1 + 1):
        dp[i][0] = i
        ops[i][0] = "delete"

    for j in range(len_s2 + 1):
        dp[0][j] = j
        ops[0][j] = "insert"

    # Fill in the table
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):

            # To delete a character from s1, the cost is 1 plus the minimum edit distance
            # for the substring s1[:i-1] and the full substring s2 up to position j.
            delete = dp[i - 1][j] + 1

            # To insert a character into s1, the cost is 1 plus the minimum edit distance
            # for the full substring s1 up to position i and the substring s2[:j-1].
            insert = dp[i][j - 1] + 1

            # If the characters at positions i and j in s1 and s2 are the same,
            # no operation is needed, so the cost is the minimum edit distance
            # for the substrings s1[:i-1] and s2[:j-1].
            match = dp[i - 1][j - 1]

            # If the characters at positions i and j in s1 and s2 are different,
            # the cost is 1 plus the minimum edit distance for the substrings
            # s1[:i-1] and s2[:j-1], as one substitution operation is required.
            mismatch = dp[i - 1][j - 1] + 1

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = match
                ops[i][j] = "match"
            else:
                dp[i][j] = min(delete, insert, mismatch)

                if dp[i][j] == delete:
                    ops[i][j] = "delete"
                elif dp[i][j] == insert:
                    ops[i][j] = "insert"
                else:
                    ops[i][j] = "replace"

    # Backtrack to get the operations
    # Backtrack to get the operations
    i, j = len_s1, len_s2
    align_s1, align_s2, operations = "", "", ""
    while i > 0 or j > 0:
        if ops[i][j] == "match":
            align_s1 = s1[i - 1] + align_s1
            align_s2 = s2[j - 1] + align_s2
            operations = "|" + operations
            i -= 1
            j -= 1
        elif ops[i][j] == "replace":
            align_s1 = s1[i - 1] + align_s1
            align_s2 = s2[j - 1] + align_s2
            operations = "*" + operations
            i -= 1
            j -= 1
        elif ops[i][j] == "insert":
            align_s1 = "-" + align_s1
            align_s2 = s2[j - 1] + align_s2
            operations = " " + operations
            j -= 1
        else:  # delete operation
            align_s1 = s1[i - 1] + align_s1
            align_s2 = "-" + align_s2
            operations = " " + operations
            i -= 1

    return dp[len_s1][len_s2], align_s1, operations, align_s2


# Test cases
s1 = "ATTCGCTCTTTAAGCTATATTTGTTTCTGATAGTCTCCAGAACAA"
s2 = "ACAAATATAACACAGGGAAGGTTAGGTATCTCTTTTTATTTGTAT"
distance, align_s1, operations, align_s2 = min_edit_distance_dp(s1, s2)
print(distance)
print(align_s1)
print(operations)
print(align_s2)



