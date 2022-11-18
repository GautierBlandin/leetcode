from typing import Callable


def longest_substring_no_repeat_tester(longest_substring_no_repeat_callable: Callable[[str], int]):
    assert longest_substring_no_repeat_callable("abcabcbb") == 3
    assert longest_substring_no_repeat_callable("bbbbb") == 1
    assert longest_substring_no_repeat_callable("pwwkew") == 3
    assert longest_substring_no_repeat_callable("") == 0
    assert longest_substring_no_repeat_callable(" ") == 1
    assert longest_substring_no_repeat_callable("dvdf") == 3
    assert longest_substring_no_repeat_callable("abba") == 2
    assert longest_substring_no_repeat_callable("aab") == 2
    assert longest_substring_no_repeat_callable("tmmzuxt") == 5
    assert longest_substring_no_repeat_callable("ohvhjdml") == 6
    assert longest_substring_no_repeat_callable("anviaj") == 5
