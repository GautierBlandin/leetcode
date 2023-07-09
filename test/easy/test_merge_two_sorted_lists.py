from easy.merge_two_sorted_lists import SortedListMerger


def test_merge_two_sorted_lists():
    merger = SortedListMerger()
    assert merger.merge([], []) == []
    assert merger.merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merger.merge([1, 3, 7, 9], [2, 4]) == [1, 2, 3, 4, 7, 9]
    assert merger.merge([1, 2, 3], []) == [1, 2, 3]
    assert merger.merge([], [1, 2, 3]) == [1, 2, 3]
