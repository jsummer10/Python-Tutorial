
from pathlib import Path

py_project = str(Path(__file__).parent/'glitchforge')

def run_mypy():
    from mypy import api

    # Define your command line arguments as a list
    args = [py_project, '--strict', '--ignore-missing-imports']

    # Execute mypy
    stdout, stderr, exit_status = api.run(args)

    # Handle the results
    if exit_status == 0:
        print("Success: No type errors found!")
    else:
        print("Mypy found issues:")
        print(stdout)
        if stderr:
            print("Errors:", stderr)


def run_pylint():
    from pylint.lint import Run

    # Arguments are passed as a list of strings, just like CLI
    results = Run([py_project])

    # Access the final score
    print(f"Final score: {results.linter.stats.global_note}")


def run_ruff():
    import subprocess

    try:
        # Executes 'ruff check <path>'
        result = subprocess.run(
            ["ruff", "check", py_project],
            capture_output=True,
            text=True,
            check=False  # Set to True to raise an error on non-zero exit codes
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        return result.returncode
    except FileNotFoundError:
        print("Ruff is not installed or not in PATH.")
        return 1


def run_flake8():
    import subprocess
    import sys

    # Runs flake8 as a command-line tool via Python
    result = subprocess.run(
        [sys.executable, "-m", "flake8", py_project],
        capture_output=True,
        text=True
    )

    # Flake8 returns non-zero if issues are found
    if result.returncode != 0:
        print("Flake8 found issues:")
        print(result.stdout)
    else:
        print("No issues found!")

    return result.returncode


# run_mypy()
# run_pylint()
# run_ruff()
# run_flake8()
