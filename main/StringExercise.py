class StringExercise:
    """
    Check if the given string represents a binary number,
    containing only the characters '0' and '1'.

    Args:
        text (str): The string to be checked.

    Returns:
        bool: True if the string represents a binary number, False otherwise.

    Raises:
        ValueError: If the input string is empty.
    """

    @staticmethod
    def is_binary_number(text: str) -> bool:
        if len(text) < 1:
            raise ValueError("Empty string does not checked ")
        return set(text) == {'0', '1'}

    """
    Convert a binary number represented as a string to its corresponding decimal representation.
    Args:
        text (str): The binary number represented as a string.
    Returns:
        int: The decimal representation of the given binary number.
    Raises:
        ValueError: If the input contains characters other than '0' and '1'.
        ValueError: If the input string is empty and cannot be processed.
    """

    @staticmethod
    def binary_to_decimal(text: str) -> int:
        if not StringExercise.is_binary_number(text):
            raise ValueError("Binary number has online 1 and 0")
        if len(text) < 1:
            raise ValueError("Empty string does not checked ")
        convert_to_decimal = 0
        for i, digit in enumerate(reversed(text)):
            if digit == '1':
                convert_to_decimal += 2 ** i

        return convert_to_decimal

    """
    Convert a valid hexadecimal number represented as a string to its corresponding decimal value.

    Args:
        text (str): The hexadecimal number represented as a string.

    Returns:
        int: The decimal value corresponding to the given hexadecimal number.

    Raises:
        ValueError: If the input contains any invalid hexadecimal characters.
    """

    @staticmethod
    def hex_to_decimal(text: str) -> int:
        hex_digits = "0123456789ABCDEF"
        text = text.upper()
        for char in text:
            if char not in hex_digits:
                raise ValueError("Invalid hex number")
        decimal_value = 0
        for i, char in enumerate(reversed(text)):
            decimal_value += hex_digits.index(char) * (16 ** i)
        return decimal_value
