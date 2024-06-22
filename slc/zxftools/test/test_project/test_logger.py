import unittest
from zxftools.project.logger import Logger

class TestLogger(unittest.TestCase):

    def test_use(self):
        logger = Logger('test.log')
        logger.info('tests')

    # def test_load(self):
    #     logger = Logger('test.log')
    #     @Logger.load(logger)
    #     def tes():
    #         raise 'nininini'
    #         return 1
    #     tes()

