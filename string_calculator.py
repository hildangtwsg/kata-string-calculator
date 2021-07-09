import re


class StringCalculator:
    def add(self, number_string):
        if not number_string:
            return 0

        def split_by(delimiter):
            return re.split(delimiter, number_string)
        return StringCalculator.sum(split_by(',|\n'))

    def sum(numbers):
        return sum(map(lambda num: int(num), numbers))
