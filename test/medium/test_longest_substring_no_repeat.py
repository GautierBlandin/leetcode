from typing import Callable

import medium.longest_substring_no_repeat as longest_substring_no_repeat


def longest_substring_no_repeat_tester(longest_substring_no_repeat_callable: Callable[[str], int], verbose=0):
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("dvdf", 3)
    ]

    for test in tests:
        assert longest_substring_no_repeat_callable(test[0]) == test[1]
        if verbose > 0:
            print(f"{test[0]} passed")


def test_longest_substring_no_repeat():
    longest_substring_no_repeat_tester(longest_substring_no_repeat.longest_substring_no_repeat, verbose=1)


def test_generate_all_substring_of_length_n():
    assert list(longest_substring_no_repeat.generate_all_substring_of_length_n("abcd",  2)) == ["ab", "bc", "cd"]
    assert list(longest_substring_no_repeat.generate_all_substring_of_length_n("", 0)) == [""]
    assert list(longest_substring_no_repeat.generate_all_substring_of_length_n(" ", 1)) == [" "]
    assert list(longest_substring_no_repeat.generate_all_substring_of_length_n("abcd", 1)) == ["a", "b", "c", "d"]
    assert list(longest_substring_no_repeat.generate_all_substring_of_length_n("abcd", 3)) == ["abc", "bcd"]
