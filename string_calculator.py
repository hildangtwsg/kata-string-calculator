class StringCalculator:
    def add(self, number_string):
        if not number_string:
            return 0
        return StringCalculator.sum(number_string.split(','))

    def sum(numbers):
        return sum(map(lambda num: int(num), numbers))
