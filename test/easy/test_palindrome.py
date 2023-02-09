import easy.palindrome as palindrome


def test_palindrome():
    assert palindrome.palindrome(121)
    assert not palindrome.palindrome(-121)
    assert palindrome.palindrome(1221)
    assert not palindrome.palindrome(10)

