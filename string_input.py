import re


class StringInput:
    DEFAULT_DELIMITER = ',|\n'

    def __init__(self, input_string):
        self.input_string = input_string
        self.delimiter, self.number_string = StringInput.parse(input_string)

    @staticmethod
    def change_operator_specified(input_string):
        return input_string.startswith('//') and '\n' in input_string

    @staticmethod
    def parse(input_string):
        if StringInput.change_operator_specified(input_string):
            def get_number_string():
                return input_string.split('\n')[-1]

            def get_delimiter():
                return input_string.split('\n')[0].replace('//', '')

            return (get_delimiter(), get_number_string())
        return (StringInput.DEFAULT_DELIMITER, input_string)

    def split(self):
        return re.split(self.delimiter, self.number_string)
