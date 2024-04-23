'''
Minimum edit distance using dynamic programming Bottom up approach
'''

def min_edit_distance_dp(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    # Create a table to store results of subproblems
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    # Initialize the table
    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j

    # Fill in the table
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)

    return dp[len_s1][len_s2]

