import medium.zigzag_conversion as zigzag_conversion


def test_add_substring_to_zigzag():
    assert zigzag_conversion.add_substring_to_zigzag('abcd', 3) == ['a', 'bd', 'c']
    assert zigzag_conversion.add_substring_to_zigzag('abc', 3) == ['a', 'b', 'c']
    assert zigzag_conversion.add_substring_to_zigzag('ab', 3) == ['a', 'b', '']

    assert zigzag_conversion.add_substring_to_zigzag('abcdef', 4) == ['a', 'bf', 'ce', 'd']
    assert zigzag_conversion.add_substring_to_zigzag('abcde', 4) == ['a', 'b', 'ce', 'd']

    assert zigzag_conversion.add_substring_to_zigzag('abcdefgh', 5) == ['a', 'bh', 'cg', 'df', 'e']


def test_zigzag_conversion():
    assert zigzag_conversion.zigzag_convert('abcd', 1) == 'abcd'
    assert zigzag_conversion.zigzag_convert('abcde', 2) == 'acebd'
    assert zigzag_conversion.zigzag_convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert zigzag_conversion.zigzag_convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
