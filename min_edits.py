def min_edit_distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    # Create a matrix to store the edit distances
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
    ops = [["" for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]  # operations matrix

    # Initialize the first row and column
    for i in range(len_s1 + 1):
        dp[i][0] = i
        ops[i][0] = "d"  # deletion
    for j in range(len_s2 + 1):
        dp[0][j] = j
        ops[0][j] = "i"  # insertion

    # Fill the rest of the matrix
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            deletion = dp[i - 1][j] + 1
            insertion = dp[i][j - 1] + 1
            match = dp[i - 1][j - 1]
            substitution = match + 1
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = match
                ops[i][j] = "m"  # match
            else:
                choices = [deletion, insertion, substitution]
                dp[i][j] = min(choices)
                ops[i][j] = "d" if dp[i][j] == deletion else ("i" if dp[i][j] == insertion else "s")  # deletion, insertion, substitution

    
    i, j = len_s1, len_s2
    align_s1, align_s2, align_ops = "", "", ""
    while i > 0 or j > 0:
        if ops[i][j] == "m":
            align_s1 = s1[i - 1] + align_s1
            align_s2 = s2[j - 1] + align_s2
            align_ops = "|" + align_ops
            i -= 1
            j -= 1
        elif ops[i][j] == "s":
            align_s1 = s1[i - 1] + align_s1
            align_s2 = s2[j - 1] + align_s2
            align_ops = " " + align_ops
            i -= 1
            j -= 1
        elif ops[i][j] == "d":
            align_s1 = s1[i - 1] + align_s1
            align_s2 = "-" + align_s2
            align_ops = " " + align_ops
            i -= 1
        elif ops[i][j] == "i":
            align_s1 = "-" + align_s1
            align_s2 = s2[j - 1] + align_s2
            align_ops = " " + align_ops
            j -= 1
    return dp[len_s1][len_s2], align_s1, align_s2, align_ops


# def test_min_edit_distance():
#     # Test case 1
#     s1 = "AGTCT"
#     s2 = "AGCT"
#     distance, align_s1, align_s2, align_ops = min_edit_distance(s1, s2)
#     assert distance == 1
#     assert align_s1 == "AGTCT"
#     assert align_s2 == "AG-CT"
#     assert align_ops == "|| ||"

#     # Test case 2
#     s1 = "ACGTACGT"
#     s2 = "ACGACGT"
#     distance, align_s1, align_s2, align_ops = min_edit_distance(s1, s2)
#     assert distance == 1
#     assert align_s1 == "ACGTACGT"
#     assert align_s2 == "ACG-ACGT"
#     assert align_ops == "||| ||||"


#     # Test case 3
#     s1 = "AGTCT"
#     s2 = "AGCT"
#     distance, align_s1, align_s2, align_ops = min_edit_distance(s1, s2)
#     assert distance == 1
#     assert align_s1 == "AGTCT"
#     assert align_s2 == "AG-CT"
#     assert align_ops == "|| ||"


#     # Test case 4
#     s1 = "ACGTACGT"
#     s2 = "ACGACGT"
#     distance, align_s1, align_s2, align_ops = min_edit_distance(s1, s2)
#     assert distance == 1
#     assert align_s1 == "ACGTACGT"
#     assert align_s2 == "ACG-ACGT"
#     assert align_ops == "||| ||||"

#     # Test case 5
#     # all characters are different
#     s1 = "ACGTACGT"
#     s2 = "TGCA"
#     distance, align_s1, align_s2, align_ops = min_edit_distance(s1, s2)
    
#     assert distance == 6
#     assert align_s1 == "ACGTACGT"
#     assert align_s2 == "T-GCA---"
#     assert align_ops =="  | |   "

#     print("All tests passed")

# test_min_edit_distance()


# def min_edit_distance_dnc(s1, s2):
#     # If one string is empty, the minimum edit distance is the length of the other string
#     if len(s1) == 0:
#         return len(s2)
#     if len(s2) == 0:
#         return len(s1)

#     # If the last characters of the strings match
#     if s1[-1] == s2[-1]:
#         cost = 0
#     else:
#         cost = 1

#     # Return the minimum of deleting from s1, deleting from s2, and replacing a character
#     return min(min_edit_distance_dnc(s1[:-1], s2) + 1,
#                min_edit_distance_dnc(s1, s2[:-1]) + 1,
#                min_edit_distance_dnc(s1[:-1], s2[:-1]) + cost)





