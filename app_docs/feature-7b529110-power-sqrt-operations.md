# Power and Square Root Operations

**ADW ID:** 7b529110
**Date:** 2025-12-24
**Specification:** specs/issue-1-adw-7b529110-sdlc_planner-add-power-sqrt-operations.md

## Overview

Added two new mathematical operations to the Calculator class: `power()` for exponential calculations and `sqrt()` for square root calculations. These methods extend the calculator's capabilities beyond basic arithmetic to support scientific and engineering calculations while maintaining input validation and error handling consistency.

## What Was Built

- `power(base, exponent)` method - calculates base raised to exponent power
- `sqrt(n)` method - calculates square root with negative input validation
- Comprehensive unit tests covering normal cases and edge cases
- Error handling for invalid inputs (negative square roots)

## Technical Implementation

### Files Modified

- `src/mathcalc/calculator.py`: Added two new methods (`power` and `sqrt`) to the Calculator class
- `tests/test_calculator.py`: Added three new test functions (`test_power`, `test_sqrt`, `test_sqrt_negative`)
- `pyproject.toml`: Updated dependencies to include ruff for development
- `.ports.env`: Added port configuration

### Key Changes

- **Power Method**: Implements exponentiation using Python's `**` operator, supports positive/negative/fractional exponents
- **Square Root Method**: Uses `math.sqrt()` with input validation that raises `ValueError` for negative inputs
- **Type Hints**: Both methods follow existing patterns with `float` type hints for parameters and return values
- **Docstrings**: Clear documentation explaining behavior and exceptions
- **Test Coverage**: Tests cover normal cases (perfect squares, exponents), edge cases (zero, negatives, fractionals), and error conditions

## How to Use

### Power Operation

```python
from mathcalc import Calculator

calc = Calculator()

# Basic exponentiation
calc.power(2, 3)      # Returns 8

# Zero exponent
calc.power(5, 0)      # Returns 1

# Negative exponent
calc.power(2, -2)     # Returns 0.25

# Fractional exponent
calc.power(4, 0.5)    # Returns 2.0
```

### Square Root Operation

```python
from mathcalc import Calculator

calc = Calculator()

# Perfect square
calc.sqrt(16)         # Returns 4.0

# Non-perfect square
calc.sqrt(2)          # Returns ~1.414

# Zero
calc.sqrt(0)          # Returns 0

# Negative number (raises error)
calc.sqrt(-1)         # Raises ValueError: "Cannot calculate square root of negative number"
```

## Configuration

No configuration required. Methods are available immediately upon instantiating the Calculator class.

## Testing

Run the test suite to verify functionality:

```bash
# Run all calculator tests
uv run pytest tests/test_calculator.py -v

# Run specific tests
uv run pytest tests/test_calculator.py::test_power -v
uv run pytest tests/test_calculator.py::test_sqrt -v
uv run pytest tests/test_calculator.py::test_sqrt_negative -v

# Manual validation
uv run python -c "from mathcalc import Calculator; c = Calculator(); print(f'power(2,3)={c.power(2,3)}'); print(f'sqrt(16)={c.sqrt(16)}')"
```

## Notes

- The `math` module was already imported in calculator.py, enabling direct use of `math.sqrt()`
- Implementation follows existing code patterns: type hints, docstrings, and explicit error handling
- No new dependencies required - uses Python standard library only
- README.md already mentioned these features, so no documentation updates were needed
- Future enhancement: Consider adding more edge case tests for extreme values (very large/small numbers)
