import medium.longest_palindromic_substring as longest_palindromic_substring


def test_longest_palindromic_substring():
    result = longest_palindromic_substring.longest_palindromic_substring("babad")
    assert result == "bab" or result == "aba"
    assert longest_palindromic_substring.longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring.longest_palindromic_substring("a") == "a"
    result = longest_palindromic_substring.longest_palindromic_substring("ac")
    assert result == "a" or result == "c"


def test_find_longest_even_length_palindrome():
    assert longest_palindromic_substring.find_longest_even_length_palindrome("abccba", 2) == (6, "abccba")
    assert longest_palindromic_substring.find_longest_even_length_palindrome("abccba", 1) == (0, "")
    assert longest_palindromic_substring.find_longest_even_length_palindrome("abbc", 1) == (2, "bb")
    assert longest_palindromic_substring.find_longest_even_length_palindrome("ab", 0) == (0, "")


def test_find_longest_odd_length_palindrome():
    assert longest_palindromic_substring.find_longest_odd_length_palindrome("abcba", 2) == (5, "abcba")
    assert longest_palindromic_substring.find_longest_odd_length_palindrome("aa", 0) == (1, "a")
    assert longest_palindromic_substring.find_longest_odd_length_palindrome("aa", 1) == (1, "a")
    assert longest_palindromic_substring.find_longest_odd_length_palindrome("rewreter", 5) == (5, "reter")
