class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l):
        if len(l) == 0:
            return None

        head = ListNode(l[0])
        current = head

        for i in range(1, len(l)):
            next_node = ListNode(l[i], None)
            current.next = next_node
            current = next_node

        return head

    @staticmethod
    def to_list(head):
        if head is None:
            return []

        result = [head.val]
        current = head
        while current.next is not None:
            current = current.next
            result.append(current.val)
        return result


def list_nodes_to_array(head: ListNode | None):
    if head is None:
        return []

    result = [head.val]
    current = head
    while current.next is not None:
        current = current.next
        result.append(current.val)
    return result
