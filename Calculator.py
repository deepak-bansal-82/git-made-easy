"""A small console calculator. by Deepak"""

from __future__ import annotations


def calculate(first: float, operator: str, second: float) -> float:
	"""Apply a basic arithmetic operation to two numbers."""
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
	expression = input("Enter an expression (for example, 10 + 20): ").split()
	if len(expression) != 3:
		print("Error: enter a number, an operator, and another number.")
		return

	try:
		first = float(expression[0])
		operator = expression[1]
		second = float(expression[2])
		result = calculate(first, operator, second)
	except ValueError as error:
		print(f"Error: {error}")
		return

	print(f"Result: {result:g}")


if __name__ == "__main__":
	main()
