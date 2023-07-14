from easy.merge_two_sorted_lists import SortedListMerger
from utils.ListNode import ListNode


def test_merge_two_sorted_lists():
    assert merge_list_helper([], []) == []
    assert merge_list_helper([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_list_helper([1, 3, 7, 9], [2, 4]) == [1, 2, 3, 4, 7, 9]
    assert merge_list_helper([1, 2, 3], []) == [1, 2, 3]
    assert merge_list_helper([], [1, 2, 3]) == [1, 2, 3]


def merge_list_helper(list_1, list_2):
    merger = SortedListMerger()
    return ListNode.to_list(merger.merge(ListNode.from_list(list_1), ListNode.from_list(list_2)))
