import pytest
from sample import (
    add, subtract, multiply, divide, factorial,
    is_palindrome, count_vowels, truncate,
    get_even_numbers, find_max, BankAccount
)


# -- Math Utilities -----------------------------------------------------------

# pytest.mark.parametrize is a great way to run the same test
# with multiple sets of data without writing repetitive code!
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -5, -10)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0

def test_divide_by_zero():
    # Pytest's way of checking for expected exceptions
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(TypeError):
        factorial(3.5)


# -- String Utilities ---------------------------------------------------------

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("python") is False

def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(123)

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("rhythm") == 0
    assert count_vowels("AEIOU") == 5

def test_truncate():
    assert truncate("Hello World", 5) == "Hello..."
    assert truncate("Hi", 5) == "Hi"

    with pytest.raises(ValueError):
        truncate("Text", -1)


# -- List Utilities -----------------------------------------------------------

def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([1, 3, 5]) == []

    with pytest.raises(TypeError):
        get_even_numbers([1, "two", 3])

def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([-10, -5, -20]) == -5

    with pytest.raises(ValueError):
        find_max([])


# -- Classes ------------------------------------------------------------------

# Fixtures are setup functions. Pytest will automatically pass the
# result of this function to any test that requests it by name.
@pytest.fixture
def account():
    return BankAccount("Alice", 100.0)

def test_bank_account_initialization():
    new_account = BankAccount("Bob", 50.0)
    assert new_account.owner == "Bob"
    assert new_account.get_balance() == 50.0

    with pytest.raises(ValueError):
        BankAccount("Charlie", -10.0)

# Notice how 'account' is passed in as an argument. Pytest uses the fixture!
def test_bank_account_deposit(account):
    new_balance = account.deposit(50.0)
    assert new_balance == 150.
