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

    def test_join_normally_function(self):
        self.assertEqual(self.str_object.join(["hello", "world", "message"], "+++"), "hello+++world+++message")

    def test_join_with_empty_list_or_empty_delimiter(self):
        with self.assertRaises(ValueError):
            self.str_object.join([], "+++")
        with self.assertRaises(ValueError):
            self.str_object.join(["hello", "world", "message"], "")

    def test_reverse_normally_function(self):
        self.assertEqual(self.str_object.reverse("ABCD"), "DCBA")

    def test_reverse_with_one_char(self):
        self.assertEqual(self.str_object.reverse("A"), "A")

    def test_reverse_with_empty_str(self):
        with self.assertRaises(ValueError):
            self.str_object.reverse("")

    def test_is_palindrome_normally_function(self):
        self.assertTrue(self.str_object.is_palindrome("Otto"))

    def test_is_palindrome_with_not_palindrome_text(self):
        self.assertFalse(self.str_object.is_palindrome("diana"))

    def test_is_palindrome_with_empty_input(self):
        with self.assertRaises(ValueError):
            self.str_object.is_palindrome("")

    def test_is_palindrom_with_sentence(self):
        self.assertTrue(self.str_object.is_palindrome("Dreh mal am Herd."))

    def test_check_no_duplicate_normally_function(self):
        self.assertFalse(self.str_object.check_no_duplicate_chars("Otto"))

    def test_check_no_duplicate_with_one_char(self):
        self.assertTrue(self.str_object.check_no_duplicate_chars("Micha"))

    def test_check_no_duplicate_with_one_char_element(self):
        self.assertTrue(self.str_object.check_no_duplicate_chars("A"))


if __name__ == '__main__':
    unittest.main()
