import unittest
from sample import (
    add, subtract, multiply, divide, factorial,
    is_palindrome, count_vowels, truncate,
    get_even_numbers, find_max, BankAccount
)


# -- Math Utilities -----------------------------------------------------------

class TestMathUtilities(unittest.TestCase):

    def test_add(self):
        # Using self.subTest to replicate pytest's parametrization
        test_cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (-5, -5, -10)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-10, 2), -5.0)

    def test_divide_by_zero(self):
        # assertRaisesRegex lets us check the specific error message
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero."):
            divide(10, 0)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

        with self.assertRaises(ValueError):
            factorial(-1)

        with self.assertRaises(TypeError):
            factorial(3.5)


# -- String Utilities ---------------------------------------------------------

class TestStringUtilities(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("python"))

    def test_is_palindrome_type_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_truncate(self):
        self.assertEqual(truncate("Hello World", 5), "Hello...")
        self.assertEqual(truncate("Hi", 5), "Hi")

        with self.assertRaises(ValueError):
            truncate("Text", -1)


# -- List Utilities -----------------------------------------------------------

class TestListUtilities(unittest.TestCase):

    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(get_even_numbers([1, 3, 5]), [])

        with self.assertRaises(TypeError):
            get_even_numbers([1, "two", 3])

    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_max([-10, -5, -20]), -5)

        with self.assertRaises(ValueError):
            find_max([])


# -- Classes ------------------------------------------------------------------

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # setUp runs before EVERY test method in this class.
        # This replaces the pytest fixture, giving us a fresh account each time.
        self.account = BankAccount("Alice", 100.0)

    def test_bank_account_initialization(self):
        new_account = BankAccount("Bob", 50.0)
        self.assertEqual(new_account.owner, "Bob")
        self.assertEqual(new_account.get_balance(), 50.0)

        with self.assertRaises(ValueError):
            BankAccount("Charlie", -10.0)

    def test_bank_account_deposit(self):
        # Uses self.account created in setUp
        new_balance = self.account.deposit(50.0)
        self.assertEqual(new_balance, 150.0)
        self.assertEqual(self.account.get_balance(), 150.0)

        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)

    def test_bank_account_withdraw(self):
        new_balance = self.account.withdraw(40.0)
        self.assertEqual(new_balance, 60.0)

        with self.assertRaisesRegex(ValueError, "Insufficient funds."):
            self.account.withdraw(200.0)

if __name__ == '__main__':
    unittest.main()