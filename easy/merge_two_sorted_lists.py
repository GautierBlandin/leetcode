class SortedListMerger:
    def merge(self, list1, list2):
        result = []
        list1_index = 0
        list2_index = 0
        while not self.lists_fully_iterated(list1_index, list2_index, list1, list2):
            if list1_index < len(list1) and list2_index < len(list2):
                if list1[list1_index] < list2[list2_index]:
                    result.append(list1[list1_index])
                    list1_index += 1
                else:
                    result.append(list2[list2_index])
                    list2_index += 1
            elif list1_index < len(list1):
                result.append(list1[list1_index])
                list1_index += 1
            elif list2_index < len(list2):
                result.append(list2[list2_index])
                list2_index += 1
        return result

    def lists_fully_iterated(self, i, j, list_i, list_j):
        return i >= len(list_i) and j >= len(list_j)
