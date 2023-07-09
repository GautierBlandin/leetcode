from utils.ListNode import ListNode


def remove_nth_node_end_lost_list(head: ListNode, n: int) -> ListNode | None:
    list_size = count_linked_list_size(head)
    # Handle special case where the element to remove is the head
    if list_size == n:
        return head.next
    # Go to the node before the node to remove. Set its next to the node to remove's next
    to_remove_predecessor_index = list_size - n - 1
    current = head
    for i in range(to_remove_predecessor_index):
        current = current.next
    current.next = current.next.next
    return head


def count_linked_list_size(head):
    list_size = 1
    current = head
    while current.next is not None:
        list_size += 1
        current = current.next
    return list_size


def access_nth_node(head, n):
    current = head
    for i in range(n):
        current = current.next
    return current
