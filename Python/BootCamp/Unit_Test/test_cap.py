'''
Unit Test
'''

import unittest
import cap

# Test Class
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.text_cap(text)
        self.assertEqual(result, 'Python')

    def test_mutiple_word(self):
        text = 'monty python i like'
        result = cap.text_cap(text)
        self.assertEqual(result, 'Monty Python I Like')

# Main function
if __name__ == "__main__":
    unittest.main()
