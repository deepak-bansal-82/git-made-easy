"""A small console calculator. by Deepak"""

from __future__ import annotations

import math


def calculate(first: float, operator: str, second: float | None = None) -> float:
    """Apply a supported arithmetic operation.

    Args:
        first: The primary operand. For unary square root, this is the value to
            evaluate.
        operator: The operator to apply. Supported values are ``+``, ``-``,
            ``*``, ``/``, ``%``, ``power``, ``sqrt``, and ``√``.
        second: The second operand for binary operators. Leave as ``None`` for
            unary square-root expressions.

    Returns:
        The computed arithmetic result.

    Raises:
        ValueError: If the operator is unsupported, a binary operator is used
            without a second operand, division or modulo uses zero, or square
                root is requested for a negative number, or power would produce a
                non-real result.
    """
    normalized_operator = "sqrt" if operator == "√" else operator.lower()
    if normalized_operator == "sqrt":
        if first < 0:
            raise ValueError("cannot take square root of a negative number")
        return math.sqrt(first)

    if second is None:
        raise ValueError("second operand is required for binary operations")

    match normalized_operator:
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
        case "power":
            try:
                result = first**second
            except ZeroDivisionError as error:
                raise ValueError("cannot raise zero to a negative power") from error
            if isinstance(result, complex):
                if not math.isclose(result.imag, 0.0, abs_tol=1e-12):
                    raise ValueError("power operation must return a real number")
                return result.real
            return result
        case _:
            raise ValueError(f"unsupported operator: {operator}")


def main() -> None:
    """Read an expression from the console and print its result.

    Supported input forms are ``<number> <operator> <number>`` for binary
    operators (including ``power``) and ``sqrt <number>`` or ``√ <number>`` for
    unary square root. Text operators are parsed case-insensitively.
    """
    expression = input(
        "Enter an expression (for example, 10 + 20, 2 power 4, sqrt 9, or √ 9): "
    ).split()
    first_operator = expression[0] if expression else ""
    if len(expression) == 2 and (first_operator == "√" or first_operator.lower() == "sqrt"):
        operator = "√" if first_operator == "√" else "sqrt"
        first_text = expression[1]
        second_text = None
    elif len(expression) == 3:
        first_text = expression[0]
        operator = expression[1]
        second_text = expression[2]
    else:
        print(
            "Error: enter 'sqrt <number>', '√ <number>', '<number> power <number>', or "
            "'<number> <operator> <number>' (text operators are case-insensitive)."
        )
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
