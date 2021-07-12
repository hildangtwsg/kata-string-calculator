import unittest

from string_calculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):
    def test_add_should_sum_empty_string(self):
        sum = StringCalculator().add('')
        self.assertEqual(0, sum)

    def test_add_should_sum_single_number_input(self):
        sum = StringCalculator().add('1')
        self.assertEqual(1, sum)

    def test_add_should_sum_list_of_numbers_separated_by_comma(self):
        sum = StringCalculator().add('1,2,3,4,10')
        self.assertEqual(20, sum)

    def test_add_should_sum_list_of_numbers_separated_by_either_comma_or_newline(self):
        sum = StringCalculator().add('1\n2,3')
        self.assertEqual(6, sum)

    def test_add_should_sum_list_of_numbers_separated_by_delimiter_set_in_input(self):
        sum = StringCalculator().add('//;\n1;2;3')
        self.assertEqual(6, sum)