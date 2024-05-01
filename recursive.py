'''
Minimum edit distance using recursive approach
'''

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
    
    return 1 + min(med_recursive(s1[:m-1], s2[:n-1]), med_recursive(s1[:m-1], s2), med_recursive(s1, s2[:n-1]))



