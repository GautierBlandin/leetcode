import medium.three_sum as three_sum


def test_three_sum():
    triplets = three_sum.three_sum([-1, 0, 1, 2, -1, -4])
    assert triplets.__contains__([-1, -1, 2])
    assert triplets.__contains__([-1, 0, 1])
    assert len(triplets) == 2


def test_cleanup():
    nums = [0, 0, 0, 0, 1, 1, 1, -1, -1, -1, 2, 2, 2, 3, 4, 5]
    cleaned = three_sum.cleanup(nums)
    cleaned.sort()
    assert cleaned == [-1, -1, 0, 0, 0, 1, 1, 2, 2, 3, 4, 5]
