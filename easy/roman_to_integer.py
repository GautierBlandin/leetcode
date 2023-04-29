def roman_to_integer(roman_string):
    combinations = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    normal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    if len(roman_string) == 0:
        return ''

    index = len(roman_string) - 1
    value = 0

    while index >= 0:
        if index - 1 >= 0 and (roman_string[index - 1] + roman_string[index]) in combinations:
            value += combinations[roman_string[index - 1] + roman_string[index]]
            index -= 2
        else:
            value += normal[roman_string[index]]
            index -= 1
    return value
