class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_nodes_to_array(head: ListNode | None):
    if head is None:
        return []

    result = [head.val]
    current = head
    while current.next is not None:
        current = current.next
        result.append(current.val)
    return result
