from typing import Callable

import medium.longest_substring_no_repeat as longest_substring_no_repeat
from medium.longest_substring_no_repeat import BinarySearcher


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


def test_binary_searcher():
    bs = BinarySearcher(5, 15)
    assert bs.get_value() == 10
    bs.lower()
    assert bs.get_value() == 8
    bs.higher()
    assert bs.get_value() == 9
    bs.higher()
    assert bs.get_value() == 10

    bs = BinarySearcher(5, 15)
    assert bs.get_value() == 10
    bs.lower()
    assert bs.get_value() == 8
    bs.lower()
    assert bs.get_value() == 7
    bs.lower()
    assert bs.get_value() == 6
    bs.lower()
    assert bs.get_value() == 5


