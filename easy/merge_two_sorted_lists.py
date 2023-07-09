class SortedListMerger:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.list_i = []
        self.list_j = []
        self.result = []

    def merge(self, list_i, list_j):
        self.i = 0
        self.j = 0
        self.list_i = list_i
        self.list_j = list_j
        self.result = []
        while not self.lists_fully_iterated():
            if self.both_lists_active():
                self.append_minimum_and_increment_index()
            else:
                self.append_remaining_items()
        return self.result

    def lists_fully_iterated(self):
        return self.i >= len(self.list_i) and self.j >= len(self.list_j)

    def both_lists_active(self):
        return self.i < len(self.list_i) and self.j < len(self.list_j)

    def append_minimum_and_increment_index(self):
        if self.list_i[self.i] < self.list_j[self.j]:
            self.result.append(self.list_i[self.i])
            self.i += 1
        else:
            self.result.append(self.list_j[self.j])
            self.j += 1

    def  append_remaining_items(self):
        if self.i < len(self.list_i):
            self.result.extend(self.list_i[self.i:])
            self.i = len(self.list_i)
        elif self.j < len(self.list_j):
            self.result.extend(self.list_j[self.j:])
            self.j = len(self.list_j)