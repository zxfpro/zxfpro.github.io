import unittest
from zxftools.rag.load_data import ChatGPTShareUrlReader

class TestReaders(unittest.TestCase):
    def test_chatgpt_url(self):
        reader = ChatGPTShareUrlReader(url='https://chatgpt.com/share/5d8c40ef-6d75-476b-8515-582da62d446f')
        result = reader.load_data()
        # print(result,'result')

    def test_2(self):
        pass