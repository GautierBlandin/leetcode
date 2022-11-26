import hard.median_of_two_sorted_lists as median_of_two_sorted_lists


def test_median_of_two_sorted_lists():
    a_1 = [1, 7, 10]
    a_2 = [4, 8]
    median_of_two_sorted_lists.find_median(a_1, a_2)

    a_1 = [1, 5, 9, 19]
    a_2 = [15, 21, 22, 23]
    median_of_two_sorted_lists.find_median(a_1, a_2)


def test_is_index_greater():
    a_1 = [1, 7, 10]
    a_2 = [4, 8]

    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 0)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 1)
    assert not median_of_two_sorted_lists.is_index_greater(a_1, a_2, 2)
    assert median_of_two_sorted_lists.is_index_greater(a_2, a_1, 0)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 1)

    a_1 = [1, 6, 10, 15]
    a_2 = [16, 17, 18, 19]

    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 0)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 1)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 2)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 3)

    assert median_of_two_sorted_lists.is_index_greater(a_2, a_1, 0)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 1)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 2)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 3)

    a_1 = [1, 5, 9, 19]
    a_2 = [15, 21, 22, 23]

    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 0)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 1)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 2)
    assert median_of_two_sorted_lists.is_index_greater(a_1, a_2, 3)

    assert median_of_two_sorted_lists.is_index_greater(a_2, a_1, 0)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 1)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 2)
    assert not median_of_two_sorted_lists.is_index_greater(a_2, a_1, 3)


def test_is_median():
    a_1 = [1, 5, 9, 19]
    a_2 = [15, 21, 22, 23]

    assert median_of_two_sorted_lists.is_median(a_1, a_2, 3)
    assert not median_of_two_sorted_lists.is_median(a_1, a_2, 2)
    assert not median_of_two_sorted_lists.is_median(a_1, a_2, 1)
    assert not median_of_two_sorted_lists.is_median(a_2, a_1, 0)
    assert not median_of_two_sorted_lists.is_median(a_2, a_1, 1)

    a_1 = [1, 6, 10, 15]
    a_2 = [16, 17, 18, 19]
    assert median_of_two_sorted_lists.is_median(a_2, a_1, 0)
    assert not median_of_two_sorted_lists.is_median(a_2, a_1, 1)
    assert not median_of_two_sorted_lists.is_median(a_1, a_2, 3)
