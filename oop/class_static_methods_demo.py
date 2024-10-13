class Calculator:
    # Class attribute for the type of calculations
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of a and b, printing the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

