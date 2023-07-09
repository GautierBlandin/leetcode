class SortedListMerger:
    def merge(self, list_i, list_j):
        result = []
        i = 0
        j = 0
        while not self.lists_fully_iterated(i, j, list_i, list_j):
            if self.both_lists_not_finished(i, j, list_i, list_j):
                i, j = self.append_minimum_and_increment_index(i, j, list_i, list_j, result)
            elif i < len(list_i):
                result.append(list_i[i])
                i += 1
            elif j < len(list_j):
                result.append(list_j[j])
                j += 1
        return result

    def lists_fully_iterated(self, i, j, list_i, list_j):
        return i >= len(list_i) and j >= len(list_j)

    def both_lists_not_finished(self, i, j, list_i, list_j):
        return i < len(list_i) and j < len(list_j)

    def append_minimum_and_increment_index(self, i, j, list_i, list_j, result):
        if list_i[i] < list_j[j]:
            result.append(list_i[i])
            i += 1
        else:
            result.append(list_j[j])
            j += 1
        return i, j
