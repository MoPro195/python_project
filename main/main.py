from collections import OrderedDict


class BasicCalculationTypes:
    # Calculates the product of the two numbers, divides it by 2,
    # and takes the remainder when divided by 7.
    def calculator(self, number1, number2):
        if not isinstance(number1, int) or not isinstance(number2, int):
            raise TypeError("Both numbers must be integers.")
        return (number1 * number2 // 2) % 7

    """
      Calculates the sum and count of numbers divisible by 2 or 7 up to the given maximum (exclusive).
      Raises a TypeError if the input is not an integer.
      Returns the result formatted as a string.
      """

    def calc_sum_and_count_all_numbers_div_by_2_or_7(self, max_exclusive):
        total_sum = 0
        count = 0
        if not isinstance(max_exclusive, int):
            raise TypeError("Numbers must be integers")

        for index in range(max_exclusive + 1):
            if index % 2 == 0 or index % 2 == 0:
                count += 1
                total_sum += index

        return self.format_result_as_string(count, total_sum)

        # Formats the count and sum as a string.

    def format_result_as_string(self, count, total_sum):
        return "Count: {}, Sum: {}".format(count, total_sum)

    def is_even(self, number):
        if not isinstance(number, int):
            raise TypeError("Numbers must be integers")
        return number % 2 == 0

    def is_odd(self, number):
        if not isinstance(number, int):
            raise TypeError("Numbers must be integers")
        return number % 2 != 0

    def number_as_text(self, number):
        if not isinstance(number, int):
            raise TypeError("Numbers must be integers")

        digits_text = []
        while number > 0:
            last_digit = number % 10
            if last_digit == 0:
                digit_text = "ZERO"
            elif last_digit == 1:
                digit_text = "ONE"
            elif last_digit == 2:
                digit_text = "TWO"
            elif last_digit == 3:
                digit_text = "THREE"
            elif last_digit == 4:
                digit_text = "FOUR"
            elif last_digit == 5:
                digit_text = "FIVE"
            elif last_digit == 6:
                digit_text = "SIX"
            elif last_digit == 7:
                digit_text = "SEVEN"
            elif last_digit == 8:
                digit_text = "EIGHT"
            elif last_digit == 9:
                digit_text = "NINE"
            else:
                digit_text = ""
            digits_text.insert(0, digit_text)
            number //= 10

        return " ".join(digits_text)

    def calculation_perfect_numbers(self, max_exclusive):
        if not isinstance(max_exclusive, int):
            raise TypeError("Numbers must be integers")
        if max_exclusive < 0:
            raise ValueError("Numbers must be positive")
        number_list = []
        for number in range(1, max_exclusive + 1):
            sum = 0
            for divisible_number in range(1, number):
                if number % divisible_number == 0:
                    sum += divisible_number
            if sum == number:
                number_list.append(sum)

        return number_list

    def calc_primes_up_to(self, max_value):
        if not isinstance(max_value, int):
            raise TypeError("Numbers must be integers")
        if max_value < 2:
            raise ValueError("Prime numbers start at 2")

        is_prime = [True] * (max_value + 1)
        primes = []

        for i in range(2, max_value + 1):
            for j in range(i * i, max_value + 1, i):
                if is_prime[j]:
                    is_prime[j] = False

        for i in range(2, max_value + 1):
            if is_prime[i]:
                primes.append(i)

        return primes

    def calculate_checksum(self, input_string):
        # Check if the input value is a string
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string")
        # Check if the string has at least one element
        if len(input_string) < 1:
            raise ValueError("String must have at least one element")
        total_sum = 0
        # Iterate over the individual digits in the string
        for position, digit in enumerate(input_string):
            # Calculate the intermediate sum taking into account the position of the digit
            total_sum += (position + 1) * int(digit)

        return total_sum % 10

    def roman_to_decimal(self, roman_number):
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if not isinstance(roman_number, str):
            raise TypeError("Input must be a string")
        if len(roman_number) < 1:
            raise ValueError("String must have at least one element")

        decimal_number = 0

        for position, digit in enumerate(roman_number):
            if digit not in roman_numerals:
                raise KeyError("The input is not available in the roman ABC")

            if position < len(roman_number) - 1:
                next_digit = roman_number[position + 1]
                if roman_numerals[digit] < roman_numerals[next_digit]:
                    decimal_number -= roman_numerals[digit]
                else:
                    decimal_number += roman_numerals[digit]
            else:
                decimal_number += roman_numerals[digit]

        return decimal_number
