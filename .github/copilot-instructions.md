# GitHub Copilot Python Project Instructions

## Tech Stack & Environment
- Language: Python 3.11+
- Package Manager: pip / poetry
- Core Frameworks: [e.g., FastAPI, Django, Flask, Pandas, None - Edit this line]

## Coding Standards & Code Style
- **Formatting:** Follow PEP 8 guidelines strictly.
- **Naming Conventions:** Use `snake_case` for functions/variables, `PascalCase` for classes, and `UPPER_CASE` for constants.
- **Type Hinting:** Always include explicit type hints for function arguments and return values using the `typing` module or built-in collection types.
- **Docstrings:** Write descriptive docstrings for all public modules, classes, and functions using the Google Python Style guide format.

## Architectural Guidelines
- **Modern Syntax:** Prefer structural pattern matching (`match/case`), `f-strings` for string formatting, and `pathlib` over `os.path`.
- **Error Handling:** Avoid generic `except: Pass` blocks. Catch specific exceptions and log errors with appropriate context.
- **Dependencies:** Prefer standard library modules (like `json`, `datetime`, `collections`) unless a third-party library offers a significant advantage.
- **Performance:** Use list comprehensions, generator expressions, and built-in functions for clean and efficient loops.

## Testing & Quality Control
- **Testing Framework:** Use `pytest` for all unit and integration tests.
- **Fixtures:** Leverage pytest fixtures for mock data and setup/teardown logic.

