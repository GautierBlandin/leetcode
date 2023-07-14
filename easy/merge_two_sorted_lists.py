from utils.ListNode import ListNode


class SortedListMerger:
    def __init__(self):
        self.current_i = None
        self.current_j = None
        self.head_i = None
        self.head_j = None
        self.result_head = None
        self.result_current = None

    def merge(self, head_i, head_j):
        self.init_merge(head_i, head_j)

        while not self.lists_fully_iterated():
            if self.both_lists_active():
                self.append_minimum_and_increment()
            else:
                self.append_remaining_items()
        return self.result_head

    def init_merge(self, head_i, head_j):
        self.current_i = head_i
        self.current_j = head_j
        self.head_i = head_i
        self.head_j = head_j
        self.result_head = None
        self.result_current = None

    def lists_fully_iterated(self):
        return self.current_i is None and self.current_j is None

    def both_lists_active(self):
        return self.current_i is not None and self.current_j is not None

    def append_to_result(self, node):
        if self.result_head is None:
            self.result_head = ListNode(node.val)
            self.result_current = self.result_head
        else:
            new_node = ListNode(node.val)
            self.result_current.next = new_node
            self.result_current = new_node

    def append_minimum_and_increment(self):
        if self.current_i.val < self.current_j.val:
            self.append_to_result(self.current_i)
            self.current_i = self.current_i.next
        else:
            self.append_to_result(self.current_j)
            self.current_j = self.current_j.next

    def  append_remaining_items(self):
        while self.current_i is not None:
            self.append_to_result(self.current_i)
            self.current_i = self.current_i.next
        while self.current_j is not None:
            self.append_to_result(self.current_j)
            self.current_j = self.current_j.next
