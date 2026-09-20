import pytest

from Calculator import calculate, main


@pytest.mark.parametrize(
	("operator", "expected"),
	[("+", 15), ("-", 9), ("*", 36), ("/", 4), ("%", 0)],
)
def test_calculate_operations(operator: str, expected: float) -> None:
	assert calculate(12, operator, 3) == expected


def test_calculate_rejects_division_by_zero() -> None:
	with pytest.raises(ValueError, match="cannot divide by zero"):
		calculate(12, "/", 0)


def test_calculate_rejects_modulo_by_zero() -> None:
	with pytest.raises(ValueError, match="cannot divide by zero"):
		calculate(12, "%", 0)


def test_calculate_rejects_unsupported_operator() -> None:
	with pytest.raises(ValueError, match="unsupported operator"):
		calculate(12, "^", 3)


def test_main_reads_expression_from_console(monkeypatch, capsys) -> None:
	monkeypatch.setattr("builtins.input", lambda _: "12 * 3")

	main()

	assert capsys.readouterr().out == "Result: 36\n"


def test_main_reports_invalid_expression(monkeypatch, capsys) -> None:
	monkeypatch.setattr("builtins.input", lambda _: "12")

	main()

	assert "enter a number" in capsys.readouterr().out.lower()