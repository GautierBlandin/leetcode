from typing import TypeVar, Callable


def longest_substring_no_repeat(string: str) -> int:
    n = len(string)
    lenghts = [i for i in range(n+1)]

    def len_is_valid(length: int) -> bool:
        index = 0
        while index + length <= n:
            substring = generate_substring(string, index, length)
            number_of_first_unique = number_of_first_unique_letters(substring)
            if number_of_first_unique == length:
                return True
            index += max(1, number_of_first_unique - 1)
        return False

    bs = BinarySearcher(lenghts, len_is_valid)
    bs.search()
    result_index = bs.get_result_index()
    print(f'result_index: {result_index}')
    if result_index >= 0:
        return lenghts[result_index]
    else:
        return 0


def number_of_first_unique_letters(string: str) -> int:
    s = set()
    for letter in string:
        if letter in s:
            return len(s)
        s.add(letter)
    return len(s)


def generate_all_substring_of_length_n(string: str, n: int) -> list[str]:
    for start_index in range(len(string) - n + 1):
        yield string[start_index: start_index + n]


def generate_substring(string: str, start_index: int, length: int) -> str:
    return string[start_index: start_index + length]


X = TypeVar('X')


class BinarySearcher:
    def __init__(self, sorted_list: list[X], key: Callable[[X], bool]):
        self.lower_limit = 0
        self.upper_limit = len(sorted_list) - 1
        self.sorted_list = sorted_list
        self.key = key
        self.binary_search_done = False
        self.result_index = None

    def search(self):
        while not self.binary_search_done:
            middle = (self.upper_limit + self.lower_limit + 1) // 2
            # print(f'middle: {middle}, lower_limit: {self.lower_limit}, upper_limit: {self.upper_limit}')
            if self.key(self.sorted_list[middle]):
                self.higher()
            else:
                self.lower()
        return self.lower_limit

    def get_result_index(self):
        if self.result_index is None:
            raise Exception("Result not found")
        return self.result_index

    def higher(self):
        new_low = (self.upper_limit + self.lower_limit + 1) // 2
        self.lower_limit = new_low
        if self.lower_limit == self.upper_limit:
            self.binary_search_done = True
            self.result_index = self.lower_limit

    def lower(self):
        new_high = (self.upper_limit + self.lower_limit) // 2
        self.upper_limit = new_high
        if self.lower_limit == self.upper_limit:
            self.binary_search_done = True
            if self.key(self.sorted_list[self.lower_limit]):
                self.result_index = self.lower_limit
            else:
                self.result_index = self.lower_limit - 1
