class Calculator:
    """A simple calculator class demonstrating class and static methods."""

    # Class attribute to describe the type of calculations
    calculation_type = "Arithmetic Operations"

    @classmethod
    def multiply(cls, a, b):
        """Return the product of a and b after printing the calculation type."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b