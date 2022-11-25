from typing import Callable, TypeVar


X = TypeVar('X')


class BinarySearcher:
    """
    Attributes:
        sorted_list: The sorted list over which to run the binary search
        key: The comparator function, taking an index from the sorted list and returning True if the final element
             is higher or equal, False if the final element is lower
    """
    def __init__(self, sorted_list: list[X], key: Callable[[list[X], int], bool]):
        self.lower_limit = 0
        self.upper_limit = len(sorted_list) - 1
        self.sorted_list = sorted_list
        self.key = key
        self.binary_search_done = False
        self.result_index = None

    def search(self):
        while not self.binary_search_done:
            middle = (self.upper_limit + self.lower_limit + 1) // 2
            if self.key(self.sorted_list, middle):
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
            if self.key(self.sorted_list, self.lower_limit):
                self.result_index = self.lower_limit
            else:
                self.result_index = self.lower_limit - 1
