'''
Minimum edit distance using dynamic programming with memoization
'''

def min_edit_distance_memo(s1, s2):
    # If one string is empty, the minimum edit distance is the length of the other string
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    memo = {}

    def helper(i, j):
        # If we've already solved this subproblem, return the stored result
        if (i, j) in memo:
            return memo[(i, j)]

        # If we've reached the end of one string, the minimum edit distance is the remaining length of the other string
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i

        # If the characters at the current indices are the same, the cost of substitution is 0. Otherwise, the cost is 1.
        if s1[i] == s2[j]:
            substitution_cost = 0
        else:
            substitution_cost = 1

        # Calculate the minimum edit distance by taking the minimum of three operations: deletion, insertion, and substitution
        memo[(i, j)] = min(
            helper(i + 1, j) + 1,  # deletion
            helper(i, j + 1) + 1,  # insertion
            helper(i + 1, j + 1) + substitution_cost  # substitution
        )

        return memo[(i, j)]

    return helper(0, 0)


# # Driver code
# def test_min_edit_distance_memo():
#     # Test case 1
#     assert min_edit_distance_memo("abc", "dc") == 2
#     assert (min_edit_distance_memo("whgtdwhgtdg", "aswcfg")) == 9
#     assert (min_edit_distance_memo("kitten", "sitting")) == 3
#     assert (min_edit_distance_memo("rosettacode", "raisethysword")) == 8
#     assert (min_edit_distance_memo("", "") == 0)
#     assert (min_edit_distance_memo("abc", "")) == 3
#     assert (min_edit_distance_memo("", "abc")) == 3
#     assert (min_edit_distance_memo("same", "same")) == 0

#     print("All tests passed")

# test_min_edit_distance_memo()
