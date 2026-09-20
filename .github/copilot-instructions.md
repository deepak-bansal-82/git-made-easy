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

## Development Workflow
- **Issue Required:** Every repository task must start with a GitHub issue that captures the high-level requirement. If no issue exists for the requested work, create one before doing anything else.
- **Assignment Required:** Assign the issue to the responsible agent before planning begins.
- **Two-Phase, HITL Process:** Work happens in two distinct phases with a human approval gate between them. Never skip straight to implementation.
  1. **Planning phase (Planning Agent role):** Analyze the high-level requirement in the issue and post a detailed plan on that same issue, or update the PR description when a PR already exists. The plan must document scope, affected files, risks, and validation. During planning, do not modify source files, tests, configuration, or any other repository files.
  2. **Approval gate:** Wait for a human to approve the plan on the issue or PR before implementation. Approval must be recorded by the repository's agreed approval marker (`plan-approved` label or an explicit approval comment). Agent-generated approval does not satisfy this gate.
  3. **Execution phase (Execution Agent role):** Only after human approval may the execution agent modify code or other repository files, and it must implement exactly what the approved plan describes. The resulting PR must link back to the issue (for example, `Closes #123`) and identify the approved plan comment or approval record.
