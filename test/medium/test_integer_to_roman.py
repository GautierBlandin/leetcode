import medium.integer_to_roman as roman


def test_integer_to_roman():
    assert roman.integer_to_roman(3) == 'III'
    assert roman.integer_to_roman(58) == 'LVIII'
    assert roman.integer_to_roman(1994) == 'MCMXCIV'
