# Feature: Add power and square root operations

## Metadata
issue_number: `1`
adw_id: `7b529110`
issue_json: `{"number":1,"title":"Add power and square root operations","body":"## Feature Request\n\nAdd two new methods to the Calculator class:\n\n1. **power(base, exponent)** - Returns base raised to exponent power\n2. **sqrt(n)** - Returns square root of n, raises ValueError if n < 0\n\n## Acceptance Criteria\n- Both methods should be added to Calculator class\n- Tests should be added for both methods\n- sqrt should validate input is non-negative\n\n## Example Usage\n```python\ncalc = Calculator()\ncalc.power(2, 3)  # Returns 8\ncalc.sqrt(16)     # Returns 4.0\ncalc.sqrt(-1)     # Raises ValueError\n```\n"}`

## Feature Description
This feature adds two mathematical operations to the existing Calculator class:
1. A `power` method that calculates base raised to an exponent
2. A `sqrt` (square root) method that calculates the square root of a number with input validation

These operations extend the calculator's capabilities beyond basic arithmetic (add, subtract, multiply, divide) to include exponential and root operations, making it more useful for scientific and engineering calculations.

## User Story
As a user of the MathCalc library
I want to calculate powers and square roots
So that I can perform more advanced mathematical operations beyond basic arithmetic

## Problem Statement
The Calculator class currently only supports basic arithmetic operations (addition, subtraction, multiplication, division). Users need to perform power and square root calculations but must rely on external libraries or manual calculations, which is inefficient and inconsistent with the existing calculator interface.

## Solution Statement
Extend the Calculator class with two new methods:
- `power(base: float, exponent: float) -> float`: Uses Python's built-in exponentiation operator to calculate base raised to exponent
- `sqrt(n: float) -> float`: Uses the `math.sqrt()` function to calculate square root, with validation to raise ValueError for negative inputs

This maintains consistency with existing method patterns (type hints, docstrings, error handling) while leveraging Python's standard library for reliable mathematical operations.

## Relevant Files
Use these files to implement the feature:

- **src/mathcalc/calculator.py** (line 1-26)
  - Contains the Calculator class with existing arithmetic methods
  - This is where the new `power` and `sqrt` methods will be added
  - Already imports `math` module (line 3) which provides `math.sqrt()`
  - Follows pattern of input validation (see `divide` method raising ValueError)

- **tests/test_calculator.py** (line 1-35)
  - Contains all unit tests for Calculator methods
  - This is where new test functions for `power` and `sqrt` will be added
  - Already uses pytest and follows consistent test patterns
  - Includes example of testing error conditions (see `test_divide_by_zero`)

### New Files
None - all changes will be made to existing files

## Implementation Plan
### Phase 1: Foundation
No foundational work required - the Calculator class already exists with proper structure, the `math` module is already imported, and the testing framework is set up.

### Phase 2: Core Implementation
1. Add the `power` method to the Calculator class following the existing method pattern with type hints and docstring
2. Add the `sqrt` method to the Calculator class with input validation to raise ValueError for negative numbers
3. Ensure both methods follow the same coding style as existing methods

### Phase 3: Integration
1. Add comprehensive unit tests for both methods covering normal cases and edge cases
2. Verify that existing tests continue to pass (no regression)
3. Update documentation if needed (README already mentions these features)

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### Step 1: Add power method to Calculator class
- Open `src/mathcalc/calculator.py`
- Add the `power(self, base: float, exponent: float) -> float` method after the `divide` method
- Include a clear docstring explaining the method returns base raised to exponent power
- Implement using Python's `**` operator: `return base ** exponent`
- Follow the same formatting and style as existing methods

### Step 2: Add sqrt method to Calculator class
- In the same file `src/mathcalc/calculator.py`
- Add the `sqrt(self, n: float) -> float` method after the `power` method
- Include a clear docstring explaining it returns the square root and raises ValueError for negative inputs
- Add input validation: `if n < 0: raise ValueError("Cannot calculate square root of negative number")`
- Implement using `math.sqrt()`: `return math.sqrt(n)`
- Follow the same formatting and style as existing methods

### Step 3: Add unit tests for power method
- Open `tests/test_calculator.py`
- Add `test_power()` function after the existing tests
- Test positive base and exponent: `calc.power(2, 3) == 8`
- Test with zero exponent: `calc.power(5, 0) == 1`
- Test with negative exponent: `calc.power(2, -2) == 0.25`
- Test with fractional exponent: `calc.power(4, 0.5) == 2.0`

### Step 4: Add unit tests for sqrt method
- In the same file `tests/test_calculator.py`
- Add `test_sqrt()` function after `test_power()`
- Test perfect square: `calc.sqrt(16) == 4.0`
- Test non-perfect square: `calc.sqrt(2) == pytest.approx(1.414, rel=0.001)`
- Test zero: `calc.sqrt(0) == 0`

### Step 5: Add unit test for sqrt error handling
- In the same file `tests/test_calculator.py`
- Add `test_sqrt_negative()` function after `test_sqrt()`
- Use pytest.raises to verify ValueError is raised for negative input
- Test with `-1` as input and match the error message

### Step 6: Run validation commands
- Execute all validation commands listed below to ensure the feature works correctly with zero regressions

## Testing Strategy
### Unit Tests
- **test_power()**: Tests various power calculations including positive/negative/zero/fractional exponents
- **test_sqrt()**: Tests square root calculations for perfect squares, non-perfect squares, and zero
- **test_sqrt_negative()**: Tests that ValueError is raised for negative inputs with appropriate error message

### Edge Cases
- Power with zero exponent (should return 1)
- Power with negative exponent (should return fraction)
- Power with fractional exponent (should work correctly)
- Square root of zero (should return 0)
- Square root of negative number (should raise ValueError)
- Square root of very large numbers (should handle without overflow)
- Square root of very small positive numbers (should handle precision)

## Acceptance Criteria
- ✓ `power` method is added to Calculator class with correct signature: `power(base: float, exponent: float) -> float`
- ✓ `sqrt` method is added to Calculator class with correct signature: `sqrt(n: float) -> float`
- ✓ `sqrt` method raises ValueError when input is negative
- ✓ Unit tests are added for both methods covering normal and edge cases
- ✓ All existing tests continue to pass (no regression)
- ✓ All new tests pass
- ✓ Code follows existing style and patterns in the codebase
- ✓ Methods include proper type hints and docstrings

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

- `cd /Users/dev3/code4b/adw-temp-verification/.venv/lib/python3.11/trees/7b529110 && uv run pytest tests/test_calculator.py -v` - Run all tests with verbose output to verify both new and existing functionality
- `cd /Users/dev3/code4b/adw-temp-verification/.venv/lib/python3.11/trees/7b529110 && uv run pytest tests/test_calculator.py::test_power -v` - Run power tests specifically
- `cd /Users/dev3/code4b/adw-temp-verification/.venv/lib/python3.11/trees/7b529110 && uv run pytest tests/test_calculator.py::test_sqrt -v` - Run sqrt tests specifically
- `cd /Users/dev3/code4b/adw-temp-verification/.venv/lib/python3.11/trees/7b529110 && uv run pytest tests/test_calculator.py::test_sqrt_negative -v` - Run sqrt error handling test
- `cd /Users/dev3/code4b/adw-temp-verification/.venv/lib/python3.11/trees/7b529110 && uv run python -c "from mathcalc import Calculator; c = Calculator(); print(f'power(2,3)={c.power(2,3)}'); print(f'sqrt(16)={c.sqrt(16)}'); print('Manual validation: power and sqrt work correctly')"` - Manual validation that methods are accessible and work correctly

## Notes
- The `math` module is already imported in `calculator.py`, so we can use `math.sqrt()` directly
- The existing code style uses clear method names, type hints, docstrings, and explicit error handling - maintain this consistency
- No new dependencies are required - all functionality uses Python standard library
- The README.md already mentions "Power and square root operations" in the Features section (line 7), so no documentation update is needed
- Consider adding more edge case tests in the future for extreme values (very large/small numbers)
