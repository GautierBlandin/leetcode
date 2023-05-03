import medium.letter_combinations_phone_number as combination


def test_letter_combination_phone_number():
    assert set(combination.letter_combinations("23")) == {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
    assert combination.letter_combinations("") == []
    assert set(combination.letter_combinations("2")) == {"a", "b", "c"}
