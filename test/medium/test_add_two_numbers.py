from typing import Callable

import medium.add_two_numbers


def abstract_two_number_test(add_two_numbers_callable: Callable[[list[int], list[int]], list[int]]):
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    assert add_two_numbers_callable(l1, l2) == [7, 0, 8]

    l1 = [0]
    l2 = [0]
    assert add_two_numbers_callable(l1, l2) == [0]

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    assert add_two_numbers_callable(l1, l2) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_add_two_number():
    abstract_two_number_test(medium.add_two_numbers.add_two_numbers)
