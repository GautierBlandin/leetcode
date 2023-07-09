from medium.remove_nth_node_end_of_list import remove_nth_node_end_lost_list
from utils.ListNode import ListNode, list_nodes_to_array


def test_remove_nth_node_end_of_list():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert list_nodes_to_array(remove_nth_node_end_lost_list(head, 2)) == [1, 2, 3, 5]

    head = ListNode(1)
    assert list_nodes_to_array(remove_nth_node_end_lost_list(head, 1)) == []

    head = ListNode(1, ListNode(2))
    assert list_nodes_to_array(remove_nth_node_end_lost_list(head, 1)) == [1]

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert list_nodes_to_array(remove_nth_node_end_lost_list(head, 5)) == [2, 3, 4, 5]
