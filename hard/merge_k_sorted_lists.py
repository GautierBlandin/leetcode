from utils.ListNode import ListNode


class SortedListMerger:
    def __init__(self):
        self.currents = []
        self.heads = []
        self.result_head = None
        self.result_current = None

    def merge(self, heads):
        self.init_merge(heads)

        while not self.lists_fully_iterated():
            self.append_minimum_and_increment()
        return self.result_head

    def init_merge(self, heads):
        self.currents = heads
        self.heads = heads
        self.result_head = None
        self.result_current = None

    def lists_fully_iterated(self):
        for node in self.currents:
            if node is not None:
                return False
        return True

    def append_to_result(self, node):
        if self.result_head is None:
            self.result_head = ListNode(node.val)
            self.result_current = self.result_head
        else:
            new_node = ListNode(node.val)
            self.result_current.next = new_node
            self.result_current = new_node

    def append_minimum_and_increment(self):
        min_index, min_node = self.find_minimum()
        self.append_to_result(min_node)
        self.currents[min_index] = min_node.next

    def find_minimum(self):
        min_index = -1
        min_value = float('inf')
        min_node = None
        for index, node in enumerate(self.currents):
            if node is not None and node.val < min_value:
                min_value = node.val
                min_index = index
                min_node = node
        return min_index, min_node
