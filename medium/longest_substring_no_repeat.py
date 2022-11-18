def longest_substring_no_repeat(string: str) -> int:
    n = len(string)
    max_len = 0
    for sub_len in range(1, n + 1):
        found_new_sub_length = False
        for sub_string in generate_all_substring_of_length_n(string, sub_len):
            if len(set(sub_string)) == len(sub_string):
                max_len = max(max_len, len(sub_string))
                found_new_sub_length = True
        if not found_new_sub_length:
            break
    return max_len
            
            
def generate_all_substring_of_length_n(string: str, n: int) -> list[str]:
    for start_index in range(len(string) - n + 1):
        yield string[start_index: start_index + n]
