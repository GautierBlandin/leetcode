def match_regex(s, p):
    """
    Match a string against a pattern
    Args:
        s: The string to match
        p: The regex pattern
        i: The index to start at in the string
        j: The index to start at in the pattern

    Returns:
        True if the pattern matches, False otherwise
    """
    if p == '':
        if s == '':
            return True
        else:
            return False

    is_char_first_match = False
    if len(s) > 0:
        is_char_first_match = match_single_character(s[0], p[0])

    if len(p) >= 2 and p[1] == '*':
        if is_char_first_match:
            return match_regex(s[1:], p) or match_regex(s, p[2:])
        else:
            return match_regex(s, p[2:])
    else:
        if is_char_first_match:
            return match_regex(s[1:], p[1:])
        else:
            return False


def match_single_character(s_c, p_c):
    if p_c == '.':
        return True
    else:
        return s_c == p_c


class MemoizedRegex:
    def __init__(self, s, p):
        self.s = s
        self.p = p
        self.n = len(s)
        self.m = len(p)
        self.memo_table = [[None for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]

    def match_regex(self, s, p):
        i = len(p)
        j = len(s)
        if self.memo_table[i][j] is not None:
            return self.memo_table[i][j]

        if p == '':
            if s == '':
                self.memo_table[i][j] = True
                return True
            else:
                self.memo_table[i][j] = False
                return False

        is_char_first_match = False
        if len(s) > 0:
            is_char_first_match = match_single_character(s[0], p[0])

        if len(p) >= 2 and p[1] == '*':
            if is_char_first_match:
                to_return = self.match_regex(s[1:], p) or self.match_regex(s, p[2:])
                self.memo_table[i][j] = to_return
                return to_return
            else:
                to_return = self.match_regex(s, p[2:])
                self.memo_table[i][j] = to_return
                return to_return
        else:
            if is_char_first_match:
                to_return = self.match_regex(s[1:], p[1:])
                self.memo_table[i][j] = to_return
                return to_return
            else:
                self.memo_table[i][j] = False
                return False
