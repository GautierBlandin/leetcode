import easy.roman_to_integer as roman


def test_roman_to_integer():
    assert roman.roman_to_integer('III') == 3
    assert roman.roman_to_integer('LVIII') == 58
    assert roman.roman_to_integer('MCMXCIV') == 1994
