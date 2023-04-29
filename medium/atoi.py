"""
Problem goal:
Implement the myAtoi(string s) function.

Algorithm steps:
- trim the input string
- check for +/- at the beginning of the number stirng
- read the digits one by one until either reaching the end of the string or a non-digit character
- if the resulting integer is greater than 2**31 - 1 or smaller than -2**31, clamp it to those numbers
"""


def my_atoi(s):
    # trim the string
    trimmed_s = s.strip()
    if len(trimmed_s) == 0:
        return 0

    # get the sign of the integer
    sign = get_sign(trimmed_s)

    # get the absolute value string of the integer
    absolute_value_string = extract_absolute_value_string(trimmed_s)

    # convert the sign and the absolute value string into an int, and return it
    return convert_with_clamp(absolute_value_string, sign)


def get_sign(s):
    """
    Get the sign of a trimmed string to convert to an integer
    Args:
        s: The string to convert. 1 <= len(s)

    Returns: True for positive, False for negative

    """
    if len(s) == 0:
        raise ValueError('The length of input string must be at least 1')
    if s[0] == '+':
        return True
    if s[0] == '-':
        return False
    return True


def extract_absolute_value_string(s):
    """
    Extract the absolute value string for a trimmed input string
    Args:
        s: The input string, e.g ('-12345jfewj')

    Returns:
        The absolute value string, e.g '12345'
    """
    index = 0
    absolute_value_string = ''
    digits = set('0123456789')

    if s[0] in '-+':
        index = 1

    while index < len(s):
        if s[index] in digits:
            absolute_value_string += s[index]
        else:
            break
        index += 1

    return absolute_value_string


def char_to_int(c):
    """
    Convert a single char to an integer
    Args:
        c: The char to convert

    Returns:
        The integer of the char
    """
    d = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    if c not in d:
        raise ValueError('invalid character, it must be a digit')
    else:
        return d[c]


def positive_string_to_int(s):
    """
    Convert a string representing a positive integer under the maximum integer limit to an int
    Args:
        s: The string to convert

    Returns:
        The integer represented by the string
    """
    reversed_s = s[::-1]
    integer = 0
    for index, c in enumerate(reversed_s):
        integer += char_to_int(c) * 10 ** index
    return integer


def pad_with_zeros(s, l):
    """
    pad s with zeros at the beginning of the string until it has length l.
    Args:
        s: The string to pad
        l: The desired length

    Returns:
        s padded with zeros at the beginning
    """
    if len(s) >= l:
        return s
    else:
        return '0' * (l - len(s)) + s


def is_greater_than(s_1, s_2):
    """
    Compute whether the integer represented by s_1 is greater than the integer represented by s_2. s_1 and s_2 are
    assumed to positive integers represented than ONLY contain digits.
    Args:
        s_1: The first integer as string
        s_2: The second integer as string

    Returns:
        s_1 >= s_2
    """
    if len(s_1) < len(s_2):
        s_1 = pad_with_zeros(s_1, len(s_2))
    elif len(s_2) < len(s_1):
        s_2 = pad_with_zeros(s_2, len(s_1))

    for i in range(len(s_1)):
        if char_to_int(s_1[i]) > char_to_int(s_2[i]):
            return True
        elif char_to_int(s_1[i]) < char_to_int(s_2[i]):
            return False
    return True


def convert_with_clamp(s, sign):
    """
    Convert a string and its sign to an integer.
    Args:
        s: An absolute value string, e.g '12345'. This string must be clean, i.e all characters must be digits.
        sign: The sign of the integer to return at the end. True for position, False for negative
    Returns: An integer in the range [-2**31, 2**31-1]. If the string is outside this interval, it will clamped to the
    interval
    """
    if sign:
        max_value_string = '2147483647'
    else:
        max_value_string = '2147483648'
    if is_greater_than(s, max_value_string):
        if sign:
            return 2147483647
        else:
            return -2147483648

    absolute_value = positive_string_to_int(s)

    if sign:
        return absolute_value
    else:
        return -absolute_value
