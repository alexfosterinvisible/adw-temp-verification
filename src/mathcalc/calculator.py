"""Calculator module with basic arithmetic operations."""

import math


class Calculator:
    """Simple calculator for basic math operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Return base raised to exponent power."""
        return base ** exponent

    def sqrt(self, n: float) -> float:
        """Return the square root of n. Raises ValueError if n is negative."""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)
