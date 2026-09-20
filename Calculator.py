"""A small console calculator. by Deepak"""

from __future__ import annotations

import math


def calculate(first: float, operator: str, second: float | None = None) -> float:
    """Apply a basic arithmetic operation to one or two numbers."""
    if operator in {"sqrt", "√"}:
        if first < 0:
            raise ValueError("cannot take square root of a negative number")
        return math.sqrt(first)

    if second is None:
        raise ValueError("second operand is required for binary operations")

    match operator:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            if second == 0:
                raise ValueError("cannot divide by zero")
            return first / second
        case "%":
            if second == 0:
                raise ValueError("cannot divide by zero")
            return first % second
        case _:
            raise ValueError(f"unsupported operator: {operator}")


def main() -> None:
    """Read an expression from the console and print its result."""
    expression = input(
        "Enter an expression (for example, 10 + 20 or sqrt 9): "
    ).split()
    unary_operators = {"sqrt", "√"}
    if len(expression) == 2 and expression[0] in unary_operators:
        operator = expression[0]
        first_text = expression[1]
        second_text = None
    elif len(expression) == 3:
        first_text = expression[0]
        operator = expression[1]
        second_text = expression[2]
    else:
        print("Error: enter 'sqrt <number>' or '<number> <operator> <number>'.")
        return

    try:
        first = float(first_text)
        second = float(second_text) if second_text is not None else None
        result = calculate(first, operator, second)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
