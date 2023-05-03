def digit_to_letters(i: str):
    number_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    return number_map[i]


def letter_combinations(digits: str):
    if len(digits) == 0:
        return []

    permutation_list = []

    def recursive_letter_combination(remaining_digits: str, prefix: str):
        if len(remaining_digits) == 0:
            permutation_list.append(prefix)
        else:
            for letter in digit_to_letters(remaining_digits[0]):
                recursive_letter_combination(remaining_digits[1:], prefix + letter)

    recursive_letter_combination(digits, "")
    return permutation_list
