import unittest

class TestFunction(unittest.TestCase):
    
    def test(self):
        inputs = 'Ahrefs'
        result = func(inputs)
        self.assertTrue(result)

    def test2(self):
        inputs = 'Ahrxv'
        result = func(inputs)
        self.assertFalse(result)

    

if __name__ == '__main__':
    unittest.main()
