from binary_search.BinarySearcher import BinarySearcher


def find_median(array_1: list[int], array_2: list[int]):
    bs = BinarySearcher(array_1, lambda _, i: is_index_greater(array_1, array_2, i))
    bs.search()
    candidate_median = bs.get_result_index()
    if candidate_median is None or not is_median(array_1, array_2, candidate_median):
        pass


def is_index_greater(array_1: list[int], array_2: list[int], index: int):
    """
    Args:
        array_1: a sorted array
        array_2: a sorted array
        index: the index of the median candidate in array_1

    Returns:
        True if the median is at index or at a greater index
        False if the median is at a strictly lower index
    """
    n = len(array_1)
    m = len(array_2)

    if (n + m) % 2 == 0:
        number_of_lower_elements = (n + m) // 2
    else:
        number_of_lower_elements = (n + m - 1) // 2

    array_2_lower_index = number_of_lower_elements - index - 1
    array_2_higher_index = number_of_lower_elements - index
    test_median_element = array_1[index]
    if number_of_lower_elements - index >= len(array_2):
        return True
    if array_2[array_2_lower_index] > test_median_element:
        return True
    else:
        if array_2[array_2_higher_index] < test_median_element:
            return False
        else:
            return True


def is_median(array_1, array_2, index):
    """
    Args:
        array_1: a sorted array
        array_2: a sorted
        index: the index of the median candidate in array_1

    Returns:
        True if the index corresponds to the median, False otherwise
    """
    n = len(array_1)
    m = len(array_2)

    if (n + m) % 2 == 0:
        number_of_lower_elements = (n + m) // 2
    else:
        number_of_lower_elements = (n + m - 1) // 2

    array_2_lower_index = number_of_lower_elements - index - 1
    array_2_higher_index = number_of_lower_elements - index
    test_median_element = array_1[index]

    if array_2_lower_index >= len(array_2):
        return False
    if array_2[array_2_lower_index] <= test_median_element <= array_2[array_2_higher_index]:
        return True
    else:
        return False
