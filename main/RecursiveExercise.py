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
