
# -- Math Utilities -----------------------------------------------------------

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    Raises ValueError for negative numbers or TypeError for non-integers.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# -- String Utilities ---------------------------------------------------------

def is_palindrome(word):
    """Returns True if the word is a palindrome, False otherwise."""
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    # Clean the string: lowercase and remove spaces
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]

def count_vowels(text):
    """
    Returns the number of vowels (a, e, i, o, u) in a given string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = set("aeiou")
    return sum(1 for char in text.lower() if char in vowels)

def truncate(text, max_length):
    """
    Truncates a string to max_length and appends '...' if it is longer.
    """
    if not isinstance(text, str):
        raise TypeError("Text input must be a string.")
    if not isinstance(max_length, int) or max_length < 0:
        raise ValueError("max_length must be a positive integer.")

    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


# -- List Utilities -----------------------------------------------------------

def get_even_numbers(numbers):
    """
    Takes a list of integers and returns a new list containing only the even numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    # Ensure all elements in the list are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")

    return [num for num in numbers if num % 2 == 0]

def find_max(numbers):
    """
    Returns the maximum value in a list of numbers.
    Raises ValueError if the list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("List cannot be empty.")

    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num

    return current_max


# -- Classes ------------------------------------------------------------------

class BankAccount:
    """
    A simple bank account class to demonstrate stateful testing.
    """

    def __init__(self, owner, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """Adds funds to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        """Removes funds from the account if sufficient balance exists."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= float(amount)
        return self.balance

    def get_balance(self):
        """Returns the current account balance."""
        return self.balance
