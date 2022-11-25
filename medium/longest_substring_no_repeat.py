def longest_substring_no_repeat(string: str):
    n = len(string)
    index = 0
    longest_substring_length = 0
    current_substring_length = 0
    letter_index_dict: dict[str, int] = dict()
    while index < n:
        if not string[index] in letter_index_dict:
            letter_index_dict[string[index]] = index
            current_substring_length += 1
            longest_substring_length = max(longest_substring_length, current_substring_length)
            index += 1
        elif string[index] in letter_index_dict:
            repeat_index = letter_index_dict[string[index]]
            keys_to_pop = []
            for letter, letter_index in letter_index_dict.items():
                if letter_index <= repeat_index:
                    keys_to_pop.append(letter)
                    current_substring_length -= 1
            for key in keys_to_pop:
                letter_index_dict.pop(key)
    return longest_substring_length
