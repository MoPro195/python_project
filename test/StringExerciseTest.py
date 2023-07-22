import unittest

from main.StringExercise import StringExercise


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.str_object = StringExercise()

    def test_is_binary_number_normal_function(self):
        self.assertTrue(self.str_object.is_binary_number("10101"))

    def test_is_binary_number_empty_input(self):
        with self.assertRaises(ValueError):
            self.str_object.is_binary_number("")

    def test_is_binary_number_wrong_input(self):
        self.assertFalse(self.str_object.is_binary_number("DFWQ!101"))

    def test_binary_to_decimal_normal_function(self):
        self.assertEqual(self.str_object.binary_to_decimal("101110"), 46)

    def test_binary_to_decimal_empty_string(self):
        with self.assertRaises(ValueError):
            self.str_object.binary_to_decimal("")

    def test_binary_to_decimal_input_not_binary(self):
        with self.assertRaises(ValueError):
            self.str_object.binary_to_decimal("AFRFAWEWGF")

    def test_hex_to_decimal_normally_function(self):
        self.assertEqual(self.str_object.hex_to_decimal("AB"), 171)

    def test_hex_to_decimal_with_wrong_input(self):
        with self.assertRaises(ValueError):
            self.str_object.hex_to_decimal("FNMBEWW")


if __name__ == '__main__':
    unittest.main()
