def zigzag_convert(to_zigzag, number_of_rows):
    # deal with trivial case
    if number_of_rows == 1:
        return to_zigzag

    # initialize variables
    start_index = 0
    string_rows = ['' for _ in range(number_of_rows)]

    # compute the substrings and add them to the string rows
    while start_index < len(to_zigzag):
        substring = to_zigzag[start_index: start_index + 2 * number_of_rows - 2]
        start_index += 2 * number_of_rows - 2
        substrings_to_add = add_substring_to_zigzag(substring, number_of_rows)
        for i in range(number_of_rows):
            string_rows[i] += substrings_to_add[i]

    # join the string rows and return the result
    return ''.join(string_rows)


def add_substring_to_zigzag(substring, n):
    """

    Args:
        substring: the substring to add to the zigzag arrays, of maximum length 2n - 2
        n: the number of rows over which to distribute the substring

    Returns:
        a list of substring with the letters added
    """
    strings = ['' for _ in range(n)]
    for index, character in enumerate(substring):
        if index < n:
            strings[index] += character
        else:
            strings[2 * n - index - 2] += character
    return strings
