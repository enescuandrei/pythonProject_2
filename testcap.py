"""
TestCap
"""
import unittest
import cap


class TestCap(unittest.TestCase):
    """
    Ceva
    """

    def test_one_word(self):
        """
        TestCap
        """
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        """
        TestCap
        """
        text = 'python test multiple'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python Test Multiple')


if __name__ == '__main__':
    unittest.main()
