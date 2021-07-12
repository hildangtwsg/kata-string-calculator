import unittest

from string_input import StringInput


class StringInputTest(unittest.TestCase):
    def test_number_string_should_be_empty_for_empty_input(self):
        self.assertEqual('', StringInput('').number_string)

    def test_delimiter_should_be_defaulted_to_comma_or_newline_for_empty_input(self):
        self.assertEqual(StringInput.DEFAULT_DELIMITER, StringInput('').delimiter)

    def test_number_string_should_not_be_modified_from_input_string_if_input_not_following_format(self):
        self.assertEqual('1\n2,3', StringInput('1\n2,3').number_string)

    def test_delimiter_should_be_defaulted_to_comma_or_newline_if_input_not_following_format(self):
        self.assertEqual(StringInput.DEFAULT_DELIMITER, StringInput('1\n2,3').delimiter)

    def test_parse_should_identify_number_string_if_input_follows_format(self):
        self.assertEqual('1;2;3', StringInput('//;\n1;2;3').number_string)

    def test_parse_should_identify_delimiter_if_input_follows_format(self):
        self.assertEqual(';', StringInput('//;\n1;2;3').delimiter)

    def test_parse_should_return_delimiter_and_number_string_tuple(self):
        self.assertEqual((';', '1;2;3'), StringInput.parse('//;\n1;2;3'))

    def test_split_by_should_return_list_of_numbers_delimited_by_comma_or_newline_by_default_if_input_not_following_format(self):
        self.assertEqual(['1', '2', '3'], StringInput('1\n2,3').split())

    def test_split_by_should_return_list_of_numbers_delimited_if_input_following_format(self):
        self.assertEqual(['1', '2', '3'], StringInput('//;\n1;2;3').split())

    def test_split_by_should_handle_mismatched_delimiter(self):
        self.assertEqual(['1,2,3'], StringInput('//;\n1,2,3').split())
