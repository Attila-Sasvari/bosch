class Calculator:
    """Class to run calculations such as:
    - addition
    - subsctraction
    - multiplication
    - division
    """

    def add(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> int:
        return int(x / y)
