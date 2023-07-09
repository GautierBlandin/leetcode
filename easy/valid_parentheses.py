def check_valid_parentheses(input_string):
    stack = []
    for char in input_string:
        if is_opening_sign(char):
            stack.append(char)
        if is_closing_sign(char):
            if is_empty(stack):
                return False
            last_sign = stack.pop()
            if last_sign != closing_sign_to_opening_sign(char):
                return False
    return is_empty(stack)


def is_empty(stack):
    return len(stack) == 0


def is_opening_sign(char):
    return char in {"(", "[", "{"}


def is_closing_sign(char):
    return char in {")", "}", "]"}


def closing_sign_to_opening_sign(char):
    sign_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    return sign_map[char]
