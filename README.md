# Simple Calculator

A small Python calculator supporting addition, subtraction, multiplication, division, modulo, and square root via `sqrt` or `√`.

## Usage

Run the calculator and enter an expression when prompted:

```bash
python Calculator.py
```

Example input:

```bash
Enter an expression (for example, 10 + 20): 12 * 3
Result: 36
```

Square root uses unary input:

```bash
Enter an expression (for example, 10 + 20, sqrt 9, or √ 9): sqrt 9
Result: 3
```

Division by zero and unsupported operators are rejected with an error.

Run the test suite with:

```bash
pytest
```