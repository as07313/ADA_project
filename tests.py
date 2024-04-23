from dynamic_program import min_edit_distance_dp
from recursive import med_recursive
from dynamic_program_memo import min_edit_distance_memo
from divide_n_conquer import min_edit_distance_dnc
from dynamic_program_space import min_edit_distance_space_optimized

def test_all_approaches():
    test_cases = [
        ("abc", "dc", 2),
        ("whgtdwhgtdg", "aswcfg", 9),
        ("kitten", "sitting", 3),
        ("rosettacode", "raisethysword", 8),
        ("", "", 0),
        ("abc", "", 3),
        ("", "abc", 3),
        ("same", "same", 0),
        ("ACGTACGT", "TGCA", 6),
        ("AGTCT", "AGCT", 1),
        ("ACGTACGT", "ACGACGT", 1)
    ]

    for s1, s2, expected in test_cases:
        assert min_edit_distance_dp(s1, s2) == expected
        assert med_recursive(s1, s2) == expected
        assert min_edit_distance_memo(s1, s2) == expected
        assert min_edit_distance_dnc(s1, s2) == expected
        assert min_edit_distance_space_optimized(s1, s2) == expected

    
    print("All tests passed")


if __name__ == "__main__":
    test_all_approaches()