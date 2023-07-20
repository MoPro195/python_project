import sys


class RecursiveExercise:
    """
    Calculates the n-th Fibonacci number recursively.
    Args:
        n (int): The position of the Fibonacci number to calculate.
    Returns:
        int: The calculated Fibonacci number.

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is not a positive number.
    """

    @staticmethod
    def fibonacci_recursive(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("Number must be integer")
        if n < 1:
            raise ValueError("Number must be a postive number")
        if n <= 2:
            return 1
        return RecursiveExercise.fibonacci_recursive(n - 1) + RecursiveExercise.fibonacci_recursive(n - 2)

    """
    Computes the n-th Fibonacci number iteratively.

    Parameters:
    - n (int): The position of the Fibonacci number in the sequence (n must be a positive integer).

    Returns:
    - int: The n-th Fibonacci number.

    Raises:
    - TypeError: If n is not an integer.
    - ValueError: If n is not a positive number.

    """

    @staticmethod
    def fibonacci_iterativ(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("Number must be an integer")
        if n < 1:
            raise ValueError("Number must be a positive number")
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            previous = 0
            current = 1
        for _ in range(2, n):
            next_fibonacci = previous + current
            previous = current
            current = next_fibonacci

        return current

    """
    Counts the number of digits in a positive natural number recursively.

    Parameters:
    - value (int): The positive natural number to count the digits of.

    Returns:
    - int: The number of digits in the given number.

    Raises:
    - TypeError: If value is not an integer.
    - ValueError: If value is not a positive number.

    """

    @staticmethod
    def count_digits(value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be a positive number")
        if value < 10:
            return 1
        if value == 0:
            return 1
        return 1 + RecursiveExercise.count_digits(value // 10)

    """
    Calculates the sum of the individual digits of a given integer value recursively.

    Parameters:
    - value (int): The integer value for which the sum of digits needs to be calculated.

    Returns:
    - int: The sum of the individual digits of the given value.

    Raises:
    - TypeError: If value is not an integer.
    
    """

    @staticmethod
    def calc_sum_of_digits(value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if 0 <= value <= 9:
            return value
        return value % 10 + RecursiveExercise.calc_sum_of_digits(value // 10)

    """
    Calculates the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - int: The greatest common divisor of a and b.

    Raises:
    - TypeError: If a or b is not an integer.
    """

    @staticmethod
    def gcd(a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a and b must be an integer")
        if a <= 0 or b < 0:
            raise ValueError("gcd is only for positiv number")
        if b == 0:
            return a
        else:
            return RecursiveExercise.gcd(b, a % b)

    """
    Calculates the greatest common divisor (GCD) of two positive integers using the iterative approach.
    
    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.
    
    Returns:
        int: The greatest common divisor of a and b.
        
    Raises:
        TypeError: If a or b is not an integer.
        ValueError: If a or b is not a positive integer.
    """

    @staticmethod
    def gcd_iterativ(a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a and b must be integers")
        if a < 0 or b <= 0:
            raise ValueError("a and b must be positive integers")

        while b != 0:
            a, b = b, a % b

        return a

    """
   Calculates the least common multiple (LCM) of two positive integers.

   Args:
       a (int): The first positive integer.
       b (int): The second positive integer.

   Returns:
       int: The least common multiple of a and b.

   Raises:
       TypeError: If a or b is not an integer.
       ValueError: If a or b is not a positive integer.
   """

    @staticmethod
    def lcm(a: int, b: int) -> int:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a and b must be integers")
        if a <= 0 or b <= 0:
            raise ValueError("a and b must be positive integers")

        return a * b // RecursiveExercise.gcd(a, b)

    """
    Reverses the characters of the input string recursively.
    
    Args:
        input (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
        
    Raises:
        TypeError: If input is not a string.
    """

    @staticmethod
    def reverse_string(text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        if len(text) == 0:
            raise ValueError("Empty String does not reverse ")
        if len(text) <= 1:
            return text
        first_char = text[0]
        rest_of_text = text[1:]
        reversed_rest = RecursiveExercise.reverse_string(rest_of_text)

        return reversed_rest + first_char

    """
        Calculates the sum of values in the given array recursively.

        :param values: A list of numbers for which the sum is to be calculated.
        :return: The sum of the values in the list.
        """

    @staticmethod
    def sum_rec(values):
        if len(values) < 1:
            return 0
        if len(values) == 1:
            return values[0]
        else:
            return values[0] + RecursiveExercise.sum_rec(values[1:])

    """
        Recursively finds the minimum value in the given array.

        :param values: A list of numeric values.
        :return: The minimum value in the list or sys.maxsize if the list is empty.
        """

    @staticmethod
    def min_rec(values):
        if len(values) < 1:
            return sys.maxsize
        if len(values) == 1:
            return values[0]
        else:
            min_rest = RecursiveExercise.min_rec(values[1:])
            return values[0] if values[0] < min_rest else min_rest

    """
        Recursively converts the given positive integer to its textual binary representation.

        :param n: A positive integer to be converted to binary.
        :return: The textual binary representation of the given integer.
        :raises ValueError: If n is not a positive number.
        """

    @staticmethod
    def to_binary(n):
        if n < 0:
            raise ValueError("n must be an positive number")
        if n == 0:
            return "0"
        if n == 1:
            return "1"

        return RecursiveExercise.to_binary(n // 2) + str(n % 2)

    """
        Converts the given positive integer to its textual octal representation.

        :param n: A positive integer to be converted to octal.
        :return: The textual octal representation of the given integer.
        :raises ValueError: If n is not a positive number.
        """

    @staticmethod
    def to_octal(n):
        if n < 0:
            raise ValueError("n must be an positive number")
        if n == 0:
            return "0"
        if n == 1:
            return "1"

        return RecursiveExercise.to_binary(n // 8) + str(n % 8)

    """
        Converts the given positive integer to its textual hexadecimal representation.

        :param n: A positive integer to be converted to hexadecimal.
        :return: The textual hexadecimal representation of the given integer.
        :raises ValueError: If n is not a positive number.
        """

    @staticmethod
    def to_hex(n):
        if n < 0:
            raise ValueError("n must be an positive number")
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        hex_digits = "0123456789ABCDEF"
        quotient, remainder = divmod(n, 16)
        if quotient == 0:
            return hex_digits[remainder]
        return RecursiveExercise.to_hex(quotient) + hex_digits[remainder]
