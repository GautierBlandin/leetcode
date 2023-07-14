from hard.merge_k_sorted_lists import SortedListMerger
from utils.ListNode import ListNode


def test_merge_two_sorted_lists():
    assert merge_list_helper([]) == []
    assert merge_list_helper([[]]) == []
    assert merge_list_helper([[], []]) == []
    assert merge_list_helper([[1, 3, 5], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6]
    assert merge_list_helper([[1, 3, 7, 9], [2, 4]]) == [1, 2, 3, 4, 7, 9]
    assert merge_list_helper([[1, 2, 3], []]) == [1, 2, 3]
    assert merge_list_helper([[], [1, 2, 3]]) == [1, 2, 3]
    assert merge_list_helper([[1], [7], [5]]) == [1, 5, 7]
    assert merge_list_helper([[1, 4, 7], [2, 5, 6], [3, 9, 10, 11, 13]]) == [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13]


def merge_list_helper(lists):
    merger = SortedListMerger()
    linked_lists = [ListNode.from_list(l) for l in lists]
    return ListNode.to_list(merger.merge(linked_lists))
