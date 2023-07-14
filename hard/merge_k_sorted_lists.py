from utils.ListNode import ListNode


class SortedListMerger:
    def __init__(self):
        self.currents = None
        self.heads = None
        self.result_head = None
        self.result_current = None
        self.not_finished_lists_indexes = None

    def merge(self, heads):
        self.divide_and_conquer(heads)

        while not self.lists_fully_iterated():
            self.append_minimum_and_increment()
        return self.result_head

    def divide_and_conquer(self, heads):
        if len(heads) > 3:
            midpoint = len(heads) // 2
            pre_merged_heads = [SortedListMerger().merge(heads[:midpoint]), SortedListMerger().merge(heads[midpoint:])]
            self.init_merge(pre_merged_heads)
        else:
            self.init_merge(heads)

    def init_merge(self, heads):
        self.currents = heads
        self.heads = heads
        self.result_head = None
        self.result_current = None
        self.not_finished_lists_indexes = set()
        for index, head in enumerate(heads):
            if head is not None:
                self.not_finished_lists_indexes.add(index)

    def lists_fully_iterated(self):
        if self.not_finished_lists_indexes:
            return False
        else:
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
        if min_node.next is None:
            self.not_finished_lists_indexes.remove(min_index)

    def find_minimum(self):
        min_index = -1
        min_value = float('inf')
        min_node = None
        for index in self.not_finished_lists_indexes:
            node = self.currents[index]
            if node.val < min_value:
                min_value = node.val
                min_index = index
                min_node = node
        return min_index, min_node
