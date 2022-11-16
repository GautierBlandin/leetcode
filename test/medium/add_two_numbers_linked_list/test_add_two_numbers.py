from medium.add_two_numbers_linked_list.ListNode import ListNode
import medium.add_two_numbers_linked_list.add_two_numbers as add_two_numbers


def test_add_two_numbers():
    l1 = ListNode.from_array([2, 4, 3])
    l2 = ListNode.from_array([5, 6, 4])
    result = ListNode.from_array([7, 0, 8])

    assert add_two_numbers.add_two_numbers(l1, l2) == result

    l1 = ListNode.from_array([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNode.from_array([9, 9, 9, 9])
    result = ListNode.from_array([8, 9, 9, 9, 0, 0, 0, 1])

    assert add_two_numbers.add_two_numbers(l1, l2) == result


