import unittest
from unittest.mock import patch, MagicMock,Mock
from zxftools.project.external_interaction import DDMessage,tool_qrcode



class TestDDMessage(unittest.TestCase):


    def test_send(self):
        message = DDMessage()
        message.send('完成')

    def test_tool_qrcode(self):
        @tool_qrcode()
        def aa():
            return 1234
        aa()
