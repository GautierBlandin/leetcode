def longest_common_prefix(strings):
    prefix = ''
    prefix_index = 0

    if len(strings) == 0 or len(strings[0]) == 0:
        return ''

    while True:
        if len(strings[0]) > prefix_index:
            c = strings[0][prefix_index]
            if check_character_all(strings, c, prefix_index):
                prefix += c
                prefix_index += 1
            else:
                return prefix
        else:
            return prefix


def check_character_all(strings, c, c_index):
    for i, s in enumerate(strings):
        if len(s) <= c_index:
            return False
        if s[c_index] != c:
            return False
    return True
