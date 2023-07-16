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
