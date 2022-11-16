from medium.add_two_numbers_linked_list.ListNode import ListNode


def test_list_node_from_array():
    array = [1, 2, 3]
    head = ListNode.from_array(array)
    assert head.val == 1
    cur = head.next
    assert cur.val == 2
    cur = cur.next
    assert cur.val == 3
    cur = cur.next
    assert cur is None


def test_list_node_to_list():
    array = [1, 2, 3]
    head = ListNode.from_array(array)
    assert head.to_list() == array
