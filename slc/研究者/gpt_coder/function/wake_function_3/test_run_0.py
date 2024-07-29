
def func(input_value):
    return isinstance(input_value, str)

import unittest

class TestFunction(unittest.TestCase):
    
    def test(self):
        inputs = 'some words'
        result = func(inputs)
        self.assertTrue(result)

    def test2(self):
        inputs = ''
        result = func(inputs)
        self.assertTrue(result)

    def test3(self):
        inputs = None
        result = func(inputs)
        self.assertFalse(result)
    

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
