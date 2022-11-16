from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_array(array: list[int]):
        head = None
        prev = None
        for index, value in enumerate(array):
            cur = ListNode(value)

            if prev is not None:
                prev.next = cur
            else:
                head = cur

            prev = cur
        return head

    def to_list(self, parent_list=None):
        if parent_list is None:
            parent_list = []

        parent_list.append(self.val)
        if self.next is None:
            return parent_list
        else:
            return self.next.to_list(parent_list)

    def __eq__(self, other):
        cur_self = self
        cur_other = other

        while cur_self is not None and cur_other is not None:
            if not cur_self.val == cur_other.val:
                return False
            cur_self = cur_self.next
            cur_other = cur_other.next

        if cur_other is None and cur_self is None:
            return True

        return False
