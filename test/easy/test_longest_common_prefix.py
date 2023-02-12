import easy.longest_common_prefix as prefix


def test_longest_common_prefix():
    assert prefix.longest_common_prefix(["flower", "flow", "flight"]) == 'fl'
    assert prefix.longest_common_prefix(["dog", "racecar", "car"]) == ''
