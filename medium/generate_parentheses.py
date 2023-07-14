class ParenthesesGenerator:
    def __init__(self):
        self.cache = dict()

    def generate_parentheses(self, n):
        if n in self.cache:
            return self.cache[n]

        if n == 1:
            return self.return_and_cache(1, ['()'])

        result_set = set()

        self.generate_wrapped_set(n - 1, result_set)
        self.generate_sub_length_assemblage(n, result_set)

        result = list(result_set)
        return self.return_and_cache(n, result)

    def return_and_cache(self, n, result):
        self.cache[n] = result
        return result

    def generate_wrapped_set(self, k, result_set):
        sub_parentheses = self.generate_parentheses(k)
        for sub_parenthesis in sub_parentheses:
            result_set.add('(' + sub_parenthesis + ')')

    def generate_sub_length_assemblage(self, n, result_set):
        for i in range(1, n):
            lefts = self.generate_parentheses(i)
            rights = self.generate_parentheses(n - i)
            for left in lefts:
                for right in rights:
                    result_set.add(left + right)
