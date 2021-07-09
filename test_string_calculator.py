import unittest

from string_calculator import StringCalculator


class StringCalculatorTest(unittest.TestCase):
    def test_add_should_sum_empty_string(self):
        sum = StringCalculator().add("")
        self.assertEqual(0, sum)

    def test_add_should_sum_single_number_input(self):
        sum = StringCalculator().add("1")
        self.assertEqual(1, sum)

    def test_add_should_sum_list_of_two_numbers(self):
        sum = StringCalculator().add("1,2")
        self.assertEqual(3, sum)

    def test_add_should_sum_list_of_more_than_two_numbers(self):
        sum = StringCalculator().add("1,2,3,4,10")
        self.assertEqual(20, sum)
