def longest_palindromic_substring(s):
    """
    Method for finding the longest palindromic substring ?
    Naive approach: try every length or substrings. Complexity O(n^2)
    Better approach: use intermediate information through the run of the program.


    Args:
        s:

    Returns:

    """
    n = len(s)
    if n == 0:
        return 0
    longest_palindrome_length = 0
    longest_palindrome = ""
    for i in range(n):
        palindrome_length, palindrome = find_longest_even_length_palindrome(s, i)
        if palindrome_length > longest_palindrome_length:
            longest_palindrome_length = palindrome_length
            longest_palindrome = palindrome
        palindrome_length, palindrome = find_longest_odd_length_palindrome(s, i)
        if palindrome_length > longest_palindrome_length:
            longest_palindrome_length = palindrome_length
            longest_palindrome = palindrome
    return longest_palindrome


def find_longest_even_length_palindrome(s, start_index):
    """
    Find the longest even length palindrome centered at the end of start_index

    Args:
        s: the string
        start_index: start index for the palindrome search

    Returns:
        the length of the longest even length palindrome
    """
    palindrome_length = 0
    palindrome = ""
    n = len(s)
    increment = 0
    while start_index - increment >= 0 and start_index + increment + 1 < n:
        if s[start_index - increment] == s[start_index + increment + 1]:
            palindrome = s[start_index - increment] + palindrome + s[start_index + increment + 1]
            palindrome_length += 2
            increment += 1
        else:
            break
    return palindrome_length, palindrome


def find_longest_odd_length_palindrome(s, start_index):
    """
    Find the longest odd length palindrome centered on start_index

    Args:
        s: The string to search
        start_index: The index on which the palindrome is centered

    Returns:
        The length of the palindrome
    """
    palindrome_length = 1
    palindrome = s[start_index]
    increment = 1
    n = len(s)
    while start_index - increment >= 0 and start_index + increment < n:
        if s[start_index - increment] == s[start_index + increment]:
            palindrome_length += 2
            palindrome = s[start_index - increment] + palindrome + s[start_index + increment]
            increment += 1
        else:
            break
    return palindrome_length, palindrome
