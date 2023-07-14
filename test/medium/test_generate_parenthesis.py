from medium.generate_parentheses import ParenthesesGenerator


def test_generate_parentheses():
    generator = ParenthesesGenerator()
    assert generator.generate_parentheses(1) == ['()']
    generator = ParenthesesGenerator()
    assert set(generator.generate_parentheses(2)) == {'(())', '()()'}
    generator = ParenthesesGenerator()
    assert set(generator.generate_parentheses(3)) == {'((()))', '(()())', '(())()', '()(())', '()()()'}
    generator = ParenthesesGenerator()
    assert set(generator.generate_parentheses(4)) == {'(()()())', '(()())()', '((()))()', '((())())', '()(())()', '(()(()))', '()()(())', '()((()))', '()(()())', '(((())))', '(())(())', '(())()()', '((()()))', '()()()()'}
