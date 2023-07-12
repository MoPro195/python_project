import unittest

from main.main import BasicCalculationTypes


class TestBasicCalculationTypes(unittest.TestCase):
    def setUp(self):
        self.calculator = BasicCalculationTypes()

    def test_calculator_with_positive_numbers(self):
        result = self.calculator.calculator(6, 7)
        self.assertEqual(result, 0)

    def test_calculator_with_negatives_numbers(self):
        result = self.calculator.calculator(-5, -5)
        self.assertEqual(result, 5)

    def test_calculator_with_float_numbers(self):
        with self.assertRaises(TypeError):
            self.calculator.calculator(9.0, 8.0)

    def test_calc_sum_and_count_all_numbers_div_by_2_or_7(self):
        expected_output = "Count: 6, Sum: 30"
        self.assertEqual(self.calculator.calc_sum_and_count_all_numbers_div_by_2_or_7(10), expected_output)

    def test_calc_sum_and_count_all_numbers_with_float_number(self):
        with self.assertRaises(TypeError):
            self.calculator.calc_sum_and_count_all_numbers_div_by_2_or_7(5.0)

    def test_failure_calc_sum_and_count_all(self):
        expected_output = "Count: 6, Sum: 890"
        self.assertFalse(self.calculator.calc_sum_and_count_all_numbers_div_by_2_or_7(10) == expected_output)

    def test_normal_is_even(self):
        self.assertTrue(self.calculator.is_even(10))

    def test_normal_is_odd(self):
        self.assertTrue(self.calculator.is_odd(7))

    def test_number_as_text_normality(self):
        expected_output = "FOUR TWO"
        self.assertEqual(self.calculator.number_as_text(42), expected_output)

    def test_calculation_perfect_numbers_function(self):
        expected_output = [6, 28, 496]
        self.assertEqual(self.calculator.calculation_perfect_numbers(1000), expected_output)

    def test_failure_calculation_perfect_numbers_function(self):
        with self.assertRaises(ValueError):
            self.calculator.calculation_perfect_numbers(-100)

    def test_calc_primes_up_to(self):
        expected_output = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(expected_output, self.calculator.calc_primes_up_to(20))

    def test_normal_function_calculation_checksum(self):
        self.assertEqual(self.calculator.calculation_checksum("11111"), 5)

    def test_wrong_type_calculation_checksum(self):
        with self.assertRaises(TypeError):
            self.calculator.calculation_checksum(100)

    def test_empty_input_calculation_checksum(self):
        with self.assertRaises(ValueError):
            self.calculator.calculation_checksum("")

    def test_roman_to_decimal_functionality(self):
        self.assertEqual(self.calculator.roman_to_decimal("XIV"), 14)

    def test_roman_to_decimal_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.calculator.roman_to_decimal("")

    def test_roman_to_decimal_with_integer(self):
        with self.assertRaises(TypeError):
            self.calculator.roman_to_decimal(10)

    def test_roman_to_decimal_with_german_alphabet(self):
        with self.assertRaises(KeyError):
            self.calculator.roman_to_decimal("Gustav")


if __name__ == '__main__':
    unittest.main()
