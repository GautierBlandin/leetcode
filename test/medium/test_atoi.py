import medium.atoi as atoi


def test_atoi():
    assert atoi.my_atoi('') == 0
    assert atoi.my_atoi('1') == 1
    assert atoi.my_atoi('-') == 0
    assert atoi.my_atoi('-1') == -1
    assert atoi.my_atoi('99999999999999999999999') == 2147483647
    assert atoi.my_atoi('-999999999999999999999999999') == -2147483648
    assert atoi.my_atoi('dfsfas') == 0
    assert atoi.my_atoi('     -42') == -42
    assert atoi.my_atoi('-91283472332') == -2147483648


def test_extract_absolute_value_string():
    assert atoi.extract_absolute_value_string('-12345sdfdsfs') == '12345'


def test_get_sign():
    assert atoi.get_sign('-1') is False


def test_pad_with_zeros():
    assert atoi.pad_with_zeros('1', 5) == '00001'


def test_is_greater_than():
    assert atoi.is_greater_than('91283472332', '2147483648') is True
