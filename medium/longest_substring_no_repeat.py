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


class BinarySearcher:
    def __init__(self, lower_limit: int, upper_limit: int):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.start_upper_limit = upper_limit
        self.start_lower_limit = lower_limit

    def get_value(self):
        return (self.upper_limit + self.lower_limit + 1) // 2

    def higher(self):
        new_low = (self.upper_limit + self.lower_limit + 1) // 2
        self.lower_limit = new_low

    def lower(self):
        new_high = (self.upper_limit + self.lower_limit + 1) // 2
        self.upper_limit = min(new_high, self.upper_limit - 1)
        self.upper_limit = new_high
