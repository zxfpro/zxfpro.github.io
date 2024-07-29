import unittest

class TestFunction(unittest.TestCase):
    
    def test(self):
        inputs = 'some words'
        result = function(inputs)
        self.assertTrue(result)

    def test2(self):
        inputs = ''
        result = function(inputs)
        self.assertFalse(result)

    def test3(self):
        inputs = None
        result = function(inputs)
        self.assertFalse(result)
    

if __name__ == '__main__':
    unittest.main()
