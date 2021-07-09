class StringCalculator:
    def add(self, number_string):
        if not number_string:
            return 0
        return sum(map(lambda num: int(num), number_string.split(',')))