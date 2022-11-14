import two_sum


def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum.two_sum(nums, target) == [0, 1]

    assert two_sum.two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum.two_sum([3, 3], 6) == [0, 1]


def test_merge():
    l1 = [3, 6]
    l2 = [4, 5]
    i_1 = [10, 15]
    i_2 = [20, 9]
    assert two_sum.merge(l1, l2, i_1, i_2) == ([3, 4, 5, 6], [10, 20, 9, 15])


def test_merge_sort():
    nums = [3, 2, 6, 7, 5]
    assert two_sum.merge_sort(nums) == ([2, 3, 5, 6, 7], [1, 0, 4, 2, 3])
