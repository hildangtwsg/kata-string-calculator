from string_input import StringInput


class StringCalculator:
    def add(self, input_string):
        if not input_string:
            return 0

        parsed_input = StringInput(input_string)

        return StringCalculator.sum(parsed_input.split())

    def sum(numbers):
        return sum(map(lambda num: int(num), numbers))
