'''
Minimum edit distance using dynamic programming with memoization
'''

def min_edit_distance_memo(s1, s2):

    # memoization dictionary
    memo = {}    
    
    n = len(s1)
    m = len(s2)

    # if one of the strings is empty, the minimum edit distance is the length of the other string
    if n == 0:
        return m
    
    if m == 0:
        return n

    if (n, m) in memo:
        return memo[(n, m)]
    
    # if the last characters are the same, we don't need to do anything move to the next characters
    if s1[n-1] == s2[m-1]:
        return min_edit_distance_memo(s1[:n-1], s2[:m-1])
    

    # if the last characters are different, we have three options:
    memo[(n, m)] = 1 + min(min_edit_distance_memo(s1[:n-1], s2),
                            min_edit_distance_memo(s1, s2[:m-1]), 
                            min_edit_distance_memo(s1[:n-1], s2[:m-1]))
    
    return memo[(n, m)]







    

