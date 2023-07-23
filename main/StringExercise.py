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

    """
    Joins a list of strings with a delimiter and returns the resulting string.

    Args:
        values (list): A list of strings to be joined.
        delimiter (str): The delimiter string to be inserted between the strings.

    Returns:
        str: The string resulting from joining the elements with the specified delimiter.
    """

    @staticmethod
    def join(values: list, delimiter: str) -> str:
        if not values or not delimiter:
            raise ValueError("values and delimiter must not be empty")
        list_to_str = values[0]
        for index in range(1, len(values)):
            list_to_str += delimiter + values[index]

        return list_to_str

    """
    Reverses the characters in a string and returns the reversed string.

    Args:
        text (str): The input string whose characters are to be reversed.

    Returns:
        str: The reversed string.
    """

    @staticmethod
    def reverse(text: str) -> str:
        if not text:
            raise ValueError("Empty string can not be return")
        if len(text) == 1:
            return text
        reversed_text = ""
        for index in range(len(text) - 1, -1, -1):
            reversed_text += text[index]

        return reversed_text

    """
    Checks if a given string is a palindrome, ignoring spaces and punctuation marks.

    Args:
        text (str): The input string to be checked.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.

    Raises:
        ValueError: If the input string is empty.
    """

    @staticmethod
    def is_palindrome(text: str) -> bool:
        if not text:
            raise ValueError("Empty string can not be checked")
        cleaned_text = ""
        for char in text:
            if char.isalnum():
                cleaned_text += char

        return cleaned_text.upper() == StringExercise.reverse(cleaned_text.upper())

    """
    Check if a given string contains no duplicate characters, ignoring the case of letters.
    
    Args:
        text (str): The input string to be checked.
        
    Returns:
        bool: True if the string contains no duplicate characters, False otherwise.
        
    Raises:
        ValueError: If the input string is empty.
    """

    @staticmethod
    def check_no_duplicate_chars(text: str) -> bool:
        if not text:
            raise ValueError("Empty string can not be checked")
        if len(text) == 1:
            return True
        text = text.lower()
        for index, char in enumerate(text):
            if char.isalpha() and text[:index].find(char) != -1:
                return False

        return True
