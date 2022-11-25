from binary_search.BinarySearcher import BinarySearcher


def test_binary_searcher():
    test_list = [True, True, True, False, False]
    bs = BinarySearcher(test_list, lambda l, i: l[i])
    bs.search()
    assert bs.result_index == 2

    test_list = [True, True, True, True, True, True, True]
    bs = BinarySearcher(test_list, lambda l, i: l[i])
    bs.search()
    assert bs.result_index == 6

    test_list = [False, False, False, False, False]
    bs = BinarySearcher(test_list, lambda l, i: l[i])
    bs.search()
    assert bs.result_index == -1

    test_list = [True, True, True, False, False, False]
    bs = BinarySearcher(test_list, lambda l, i: l[i])
    bs.search()
    assert bs.result_index == 2
