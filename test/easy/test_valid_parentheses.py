from easy.valid_parentheses import check_valid_parentheses


def test_valid_parentheses():
    assert(check_valid_parentheses("()"))
    assert(check_valid_parentheses("()[]{}"))
    assert(not check_valid_parentheses("(]"))
    assert(check_valid_parentheses("{([])}"))
    assert(check_valid_parentheses("()[{}[]][]"))
    assert(check_valid_parentheses(""))
    assert(not check_valid_parentheses("["))
