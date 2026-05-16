import unittest

class SimpleTest(unittest.TestCase):

    def test_abc(self):
        self.assertEqual('abc', 'abc')

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()