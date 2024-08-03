import unittest

class TestFunction(unittest.TestCase):
    
    def test(self):
        inputs = 'Social'
        result = func(inputs)
        self.assertTrue(result)

    def test2(self):
        inputs = 'csv'
        result = func(inputs)
        self.assertFalse(result)

    def test3(self):
        inputs = 'Tools'
        result = func(inputs)
        self.assertTrue(result)
    

if __name__ == '__main__':
    unittest.main()
