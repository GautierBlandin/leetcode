def add_two_numbers(digits_1: list[int], digits_2: list[int]) -> list[int]:
    """ Add the two numbers represented by their digits list

    Args:
        digits_1: The list of digits of the first number, in reverse order
        digits_2: The list of digits of the second number, in reverse order
    Returns:
        The list of digits of the sum of the two numbers, in reverse order
    """
    n = len(digits_1)
    m = len(digits_2)

    if n <= 0 or m <= 0:
        raise ValueError

    unfinished_digits = [digits_1, digits_2]
    max_length = max(n, m)

    i = 0

    carrying = False
    digits_result = []

    while i < max_length:
        digits = [digit_list[i] for digit_list in unfinished_digits]

        total_result = sum(digits)
        if carrying:
            total_result += 1

        if total_result >= 10:
            carrying = True
        else:
            carrying = False

        d_result = total_result % 10
        digits_result.append(d_result)

        i += 1

        for digit_list in unfinished_digits:
            if len(digit_list) <= i:
                unfinished_digits.remove(digit_list)

    if carrying:
        digits_result.append(1)

    return digits_result
