import medium.reverse_integer as reverse_integer


def test_reverse():
    assert reverse_integer.reverse(1) == 1
    assert reverse_integer.reverse(123) == 321
    assert reverse_integer.reverse(-123) == -321
    assert reverse_integer.reverse(120) == 21
    assert reverse_integer.reverse(2**31 - 2) == 0
