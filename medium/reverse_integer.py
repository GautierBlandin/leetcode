"""
Approach for the reverse integer problem

We want to reverse the digits of the 32-bit signed integer, and return 0 if this operation makes the integer go outside
[-2^31, 2^31 - 1] range.

Reversing the digits seems easy : take the string of the absolute value, reverse it, and put a minus sign in front if
necessary. How to deal with the bound ?

Take the string representation of 2^31-1, the string representation of the final number, and subtract digit by digit.
"""


def reverse(x):
    """
    Args:
        x: The integer to reverse

    Returns:
        x reversed (integer)
    """
    abs_x_string = str(abs(x))
    if not is_valid(abs_x_string[::-1], x >= 0):
        return 0
    else:
        if x < 0:
            return - int(abs_x_string[::-1])
        else:
            return int(abs_x_string[::-1])


def is_valid(x_string, x_sign):
    """

    Args:
        x_string: A string representing a positive integer
        x_sign: False for negative, True for positive

    Returns:
         True if the string represents an integer that is in the range [-2^31, 2^31 - 1]
    """
    max_valid_string = '2147483647' if x_sign else '2147483648'

    if len(x_string) < len(max_valid_string):
        return True
    elif len(x_string) > len(max_valid_string):
        return False
    else:
        for i in range(len(max_valid_string)):
            if int(x_string[i]) > int(max_valid_string[i]):
                return False
            elif int(x_string[i]) < int(max_valid_string[i]):
                return True
            else:
                continue
        return True
