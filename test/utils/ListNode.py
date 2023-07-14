from utils.ListNode import ListNode, list_nodes_to_array


def test_list_node_to_array():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert list_nodes_to_array(head) == [1, 2, 3, 4, 5]
    assert list_nodes_to_array(None) == []

def test_from_list():
    head = ListNode.from_list([1, 2, 3, 4])
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 3
    assert head.next.next.next.val == 4
    assert head.next.next.next.next is None

    head = ListNode.from_list([])
    assert head is None

    head = ListNode.from_list([0])
    assert head.val == 0
    assert head.next is None
