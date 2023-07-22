import unittest
from main.RecursiveExercise import RecursiveExercise


class RecursiveExerciseTest(unittest.TestCase):
    def setUp(self):
        self.test_object = RecursiveExercise()

    def test_fibonacci_recursive_normal_function(self):
        self.assertEqual(self.test_object.fibonacci_recursive(8), 21)

    def test_fibonacci_recursive_with_float(self):
        with self.assertRaises(TypeError):
            self.test_object.fibonacci_recursive(10.9)

    def test_fibonacci_recursive_with_negativ_number(self):
        with self.assertRaises(ValueError):
            self.test_object.fibonacci_recursive(-500)

    def test_fibonacci_iterativ_normal_function(self):
        self.assertEqual(self.test_object.fibonacci_iterativ(8), 13)

    def test_count_digits_normal_function(self):
        self.assertEqual(self.test_object.count_digits(123), 2)

    def test_count_digits_with_negativ_number(self):
        with self.assertRaises(ValueError):
            self.test_object.count_digits(-10)

    def test_calc_sum_of_digits_normal(self):
        self.assertEqual(self.test_object.calc_sum_of_digits(1234), 10)

    def test_calc_sum_of_digits_normal_large(self):
        self.assertEqual(self.test_object.calc_sum_of_digits(1234567), 28)

    def test_gcd_normally_function(self):
        self.assertEqual(self.test_object.gcd(42, 7), 7)

    def test_gcd_with_float(self):
        with self.assertRaises(TypeError):
            self.test_object.gcd(7.0, 1.0)

    def test_gcd_with_two_zero(self):
        self.assertTrue(self.test_object.gcd(0, 0) == 0)

    def test_gcd_iterativ_normally_function(self):
        self.assertEqual(self.test_object.gcd_iterativ(24, 18), 6)

    def test_lcm_normally_function(self):
        self.assertEqual(self.test_object.lcm(2, 7), 14)

    def test_reverse_string_normally_function(self):
        self.assertEqual(self.test_object.reverse_string("ABC"), "CBA")

    def test_reverse_string_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.test_object.reverse_string("")

    def test_sum_rec_normally_function(self):
        self.assertEqual(self.test_object.sum_rec([1, 2, 3, 4, 5]), 15)

    def test_min_rec_normally_function(self):
        self.assertEqual(self.test_object.min_rec([7, 2, 1, 9, 7, 1]), 1)

    def test_to_binary_normally_function(self):
        self.assertEqual(self.test_object.to_binary(5), "101")

    def test_to_binary_negative_number(self):
        with self.assertRaises(ValueError):
            self.test_object.to_binary(-100)

    def test_to_binary_with_huge_number(self):
        self.assertEqual(self.test_object.to_binary(256), "100000000")

    def test_to_octal_normally_function(self):
        self.assertEqual(self.test_object.to_octal(7), "07")

    def test_to_hex_normally_function(self):
        self.assertEqual(self.test_object.to_hex(15), "F")

    def test_is_power_of_2_normally_function(self):
        self.assertTrue(self.test_object.is_power_of_2(2))

    def test_to_power_of_normally_function(self):
        self.assertEqual(self.test_object.power_of(4, 2), 16)

    def test_to_power_of_iterativ_normally_function(self):
        self.assertEqual(self.test_object.power_of_iterativ(4, 2), 16)

    if __name__ == '__main__':
        unittest.main()
