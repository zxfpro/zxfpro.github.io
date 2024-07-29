
import requests

def get_sql_app(app_name):
    url = "http://180.184.80.35:6688/aiquant-mark/page-data/queryApp"
    param = {'appName': app_name}
    response = requests.get(url, params=param)
    return response.json()

def func(app_name):
    response = get_sql_app(app_name)
    if response['code'] == '00000000' and response['data']:
        return True
    return False

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

if __name__ == '__main__':
    unittest.main()
