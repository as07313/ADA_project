def min_edit_distance_dnc(s1, s2):
    # If one string is empty, the minimum edit distance is the length of the other string
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # If the last characters of the strings match
    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    # Return the minimum of deleting from s1, deleting from s2, and replacing a character
    return min(min_edit_distance_dnc(s1[:-1], s2) + 1,
               min_edit_distance_dnc(s1, s2[:-1]) + 1,
               min_edit_distance_dnc(s1[:-1], s2[:-1]) + cost)


def med_recursive(s1, s2):

    m = len(s1)
    n = len(s2)
    op = []

    if m == 0:
        return n
    
    if n == 0:
 
        return m
    if s1[m-1] == s2[n-1]:
        return med_recursive(s1[:m-1], s2[:n-1])
    
    return 1 + min(med_recursive(s1[:m-1], s2[:n-1]), 
                   med_recursive(s1[:m-1], s2),
                   med_recursive(s1, s2[:n-1]))


