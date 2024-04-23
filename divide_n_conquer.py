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



# def test_min_edit_distance_dnc():
#     # Test case 1
#     s1 = "AGTCT"
#     s2 = "AGCT"
#     distance = min_edit_distance_dnc(s1, s2)
#     assert distance == 1

#     # Test case 2
#     s1 = "ACGTACGT"
#     s2 = "ACGACGT"
#     distance = min_edit_distance_dnc(s1, s2)
#     assert distance == 1

#     # Test case 3
#     s1 = "AGTCT"
#     s2 = "AGCT"
#     distance = min_edit_distance_dnc(s1, s2)
#     assert distance == 1

#     # Test case 4
#     s1 = "ACGTACGT"
#     s2 = "ACGACGT"
#     distance = min_edit_distance_dnc(s1, s2)
#     assert distance == 1

#     # Test case 5
#     # all characters are different
#     s1 = "ACGTACGT"
#     s2 = "TGCA"
#     distance = min_edit_distance_dnc(s1, s2)
#     assert distance == 6

#     print("All tests passed")


# test_min_edit_distance_dnc()
