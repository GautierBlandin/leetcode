def integer_to_roman(number):
    if number < 0 or number > 3999:
        raise ValueError('Only integer in the 0 to 3999 range are supported')
    roman_string = ones_to_roman(number % 10)
    roman_string = tens_to_roman((number % 100) // 10) + roman_string
    roman_string = hundreds_to_roman((number % 1000) // 100) + roman_string
    roman_string = thousands_to_roman(number // 1000) + roman_string
    return roman_string


def ones_to_roman(number):
    """
    Convert a single digit in the 0 to 9 range to its roman representation
    Args:
        number: A digit from 0 to 9

    Returns:
        The roman representation of the digit
    """
    digit_to_roman = {
        0: '',
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
    }
    return digit_to_roman[number]


def tens_to_roman(number):
    """
    Convert a digit in the 0 to 9 range, representing a multiple of ten, to its roman representation
    Args:
        number: The digit

    Returns:
        The roman representation of the digit
    """
    digit_to_roman = {
        0: '',
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC',
    }
    return digit_to_roman[number]


def hundreds_to_roman(number):
    digit_to_roman = {
        0: '',
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DC',
        7: 'DCC',
        8: 'DCCC',
        9: 'CM',
    }
    return digit_to_roman[number]


def thousands_to_roman(number):
    digit_to_roman = {
        0: '',
        1: 'M',
        2: 'MM',
        3: 'MMM',
    }
    return digit_to_roman[number]
