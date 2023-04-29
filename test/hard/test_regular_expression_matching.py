import hard.regular_expression_matching as regex


def test_regex():
    assert not regex.match_regex('aa', 'a')
    assert regex.match_regex('aa', 'a*')
    assert regex.match_regex('ab', '.*')
    assert regex.match_regex('aaa', '...')
    assert not regex.match_regex('aba', 'aaa')
    assert regex.match_regex('', '')
    assert regex.match_regex('a+a', 'a.a')
    assert regex.match_regex('aaabbbccc', 'a*b*c*')
    assert regex.match_regex('a', 'a*b*c*')
    assert regex.match_regex('', 'a*')
    assert regex.match_regex('aabbccdef', 'a*b*c*def')
    assert regex.match_regex('aabbccdef', 'a*b*c*def*')
    assert not regex.match_regex('aabbccdefg', 'a*')
    assert regex.match_regex('fdasfeawfdfas', '.*')
    assert not regex.match_regex('feqwfefea', '.*ddd')


def test_regex_class():
    memoized = regex.MemoizedRegex('aabbccdef', 'a*b*c*def')
    assert memoized.match_regex('aabbccdef', 'a*b*c*def')
    memoized = regex.MemoizedRegex('aa', 'a')
    assert not memoized.match_regex('aa', 'a')
    memoized = regex.MemoizedRegex('aa', 'a*')
    assert memoized.match_regex('aa', 'a*')
