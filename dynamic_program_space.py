def min_edit_distance_space_optimized(s, t):
        
        n = len(s)
        m = len(t)

        prev = [j for j in range(m+1)]
        curr = [0] * (m+1)


        for i in range(1, n+1):
            curr[0] = i
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1]
                else:
                    mn = min(1 + prev[j], 1 + curr[j-1])
                    curr[j] = min(mn, 1 + prev[j-1])
            prev = curr.copy()

        return prev[m]


# Path: dynamic_program_space.py
s1 = "kitten"
s2 = "sitting"

print(min_edit_distance_space_optimized(s1, s2)) # 3


 
