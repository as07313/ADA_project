'''
Minimum edit distance using recursive approach
'''

def med_recursive(s1, s2):
    def _med_recursive(s1, s2, i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if s1[i - 1] == s2[j - 1]:
            cost = 0
        else:
            cost = 1
        return min(_med_recursive(s1, s2, i - 1, j) + 1,
                   _med_recursive(s1, s2, i, j - 1) + 1,
                   _med_recursive(s1, s2, i - 1, j - 1) + cost)

    return _med_recursive(s1, s2, len(s1), len(s2))


