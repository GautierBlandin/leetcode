from utils.ListNode import ListNode, list_nodes_to_array


def test_list_node_to_array():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert list_nodes_to_array(head) == [1, 2, 3, 4, 5]
    assert list_nodes_to_array(None) == []
