import pytest

from Calculator import calculate, main


@pytest.mark.parametrize(
    ("operator", "expected"),
    [
        ("+", 15),
        ("-", 9),
        ("*", 36),
        ("/", 4),
        ("%", 0),
        ("power", 1728),
        ("Power", 1728),
    ],
)
def test_calculate_operations(operator: str, expected: float) -> None:
    assert calculate(12, operator, 3) == expected


@pytest.mark.parametrize("operator", ["sqrt", "√"])
def test_calculate_square_root(operator: str) -> None:
    assert calculate(9, operator) == 3


def test_calculate_rejects_negative_square_root() -> None:
    with pytest.raises(ValueError, match="cannot take square root"):
        calculate(-1, "sqrt")


def test_calculate_rejects_missing_second_operand() -> None:
    with pytest.raises(ValueError, match="second operand is required"):
        calculate(12, "+")


def test_calculate_rejects_division_by_zero() -> None:
    with pytest.raises(ValueError, match="cannot divide by zero"):
        calculate(12, "/", 0)


def test_calculate_rejects_modulo_by_zero() -> None:
    with pytest.raises(ValueError, match="cannot divide by zero"):
        calculate(12, "%", 0)


def test_calculate_rejects_unsupported_operator() -> None:
    with pytest.raises(ValueError, match="unsupported operator"):
        calculate(12, "^", 3)


def test_calculate_power_accepts_integer_exponent_for_negative_base() -> None:
    assert calculate(-2, "power", 3) == -8


def test_calculate_power_rejects_non_real_result() -> None:
    with pytest.raises(ValueError, match="must return a real number"):
        calculate(-1, "power", 0.5)


def test_calculate_power_rejects_zero_to_negative_power() -> None:
    with pytest.raises(ValueError, match="cannot raise zero to a negative power"):
        calculate(0, "power", -1)


def test_main_reads_expression_from_console(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "12 * 3")

    main()

    assert capsys.readouterr().out == "Result: 36\n"


def test_main_reads_square_root_expression(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "sqrt 9")

    main()

    assert capsys.readouterr().out == "Result: 3\n"


def test_main_reads_case_insensitive_square_root_expression(
    monkeypatch, capsys
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "Sqrt 9")

    main()

    assert capsys.readouterr().out == "Result: 3\n"


def test_main_reads_power_expression(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "2 power 4")

    main()

    assert capsys.readouterr().out == "Result: 16\n"


def test_main_prompt_shows_operation_examples(monkeypatch) -> None:
    received_prompt = ""

    def fake_input(prompt: str) -> str:
        nonlocal received_prompt
        received_prompt = prompt
        return "2 + 3"

    monkeypatch.setattr("builtins.input", fake_input)

    main()

    assert "Add: 2 + 3 = 5" in received_prompt
    assert "Power: 2 power 3 = 8" in received_prompt


def test_main_reports_invalid_expression(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "12")

    main()

    assert "sqrt <number>" in capsys.readouterr().out.lower()


def test_main_rejects_incomplete_binary_expression(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "/ 2")

    main()

    assert "sqrt <number>" in capsys.readouterr().out.lower()
