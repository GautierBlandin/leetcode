import medium.container_water as container


def test_max_volume():
    assert container.max_amount_of_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
