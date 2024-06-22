
import os
import unittest
from unittest.mock import patch, MagicMock,Mock
from zxftools.project.api_server import API_manager

class TestAPIManager(unittest.TestCase):
    def test_api_manager(self):
        pass


    @patch("zxftools.llms.llms.qet_openai")
    def test_wildcard(self,qet_openai):
        qet_openai.return_value = '1'
        llm = get_llm(type='openai_wildcard')
        print('llm',llm,'llm')
        # qet_openai.assert_called()