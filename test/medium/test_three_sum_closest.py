import medium.three_sum_closest as three_sum_closest


def test_three_sum_closest():
    assert three_sum_closest.three_sum_closest([-1, 2, 1, -4], 1) == 2
    assert three_sum_closest.three_sum_closest([0, 0, 0], 1) == 0
