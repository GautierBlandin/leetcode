def merge(l_1: list[float], l_2: list[float], indices_1: list[int], indices_2: list[int]) -> tuple[list[float], list[int]]:
    """
    Merge two sorted lists into a sorted list (all ascending order)
    Args:
        l_1: first sorted list
        l_2: second sorted list
        indices_1: indices of the first sorted list
        indices_2: indices of the second sorted list
    """
    n = len(l_1)
    m = len(l_2)
    i = 0
    j = 0
    l = []
    indices = []
    while i < n and j < m:
        if l_1[i] <= l_2[j]:
            l.append(l_1[i])
            indices.append(indices_1[i])
            i += 1
        else:
            l.append(l_2[j])
            indices.append(indices_2[j])
            j += 1
    while i < n:
        l.append(l_1[i])
        indices.append(indices_1[i])
        i += 1
    while j < m:
        l.append(l_2[j])
        indices.append(indices_2[j])
        j += 1
    return l, indices


def split_and_merge(l: list[float], indices: list[int]) -> tuple[list[float], list[int]]:
    if len(l) == 1:
        return l, indices
    else:
        n = len(l)
        l_1, i_1 = split_and_merge(l[:n//2], indices[:n//2])
        l_2, i_2 = split_and_merge(l[n//2:], indices[n//2:])
        return merge(l_1, l_2, i_1, i_2)


def merge_sort(nums: list[float]) -> tuple[list[float], list[int]]:

    n = len(nums)
    indices = [i for i in range(n)]
    return split_and_merge(nums, indices)

