import unittest
import timeit
import resource

from zxftools.rag.load_data import load_data

class LoadDataWay(unittest.TestCase):
    def test_url(self):
        url = 'www.baidu.com'
        result = load_data(url)
        assert len(result) > 1

    def test_arxiv(self):
        url = 'https://arxiv.org/pdf/2404.15153'
        result = load_data(url)
        assert len(result) > 1

    def test_datas(self):
        data_path = 'data'
        result = load_data(data_path)
        print(result)
        assert len(result) > 1

    def test_datas_recursive(self):
        data_path = 'data'
        result = load_data(data_path,params='r')
        print(result)
        assert len(result) > 1

    def test_datas_recursive2(self):
        # TODO
        data_path = "/Users/zhaoxuefeng/GitHub_AI/SDV"
        result = load_data(data_path, params='r')
        print(result)
        assert len(result) > 1

    def test_pdf(self):
        data_path = 'data/10k-132.pdf'
        result = load_data(data_path)
        assert len(result) > 1

    def test_dict(self):
        data_dict = {1:'23',3:'23'}
        result = load_data(data_dict)
        assert len(result) > 1
        data_dict = {'wd':'我的','xc':'23'}
        result = load_data(data_dict)
        assert len(result) > 1
        data_dict = {'wd':'我的','xc':{'xx':'vcx'}}
        result = load_data(data_dict)
        assert len(result) > 1

    def test_json(self):
        pass

    def test_str(self):
        data_str = 'hello'
        result = load_data(data_str)
        assert len(result) > 1
        data_str = '我是这个真实'
        result = load_data(data_str)
        assert len(result) > 1

    def test_github(self):
        data_github = 'https://github.com/THUDM/GLM-4'
        result = load_data(data_github)
        assert len(result) > 1


#
#
#
# import os
# from zxftools.rag.load_data import (is_url,DictReader,DirectoryReader,DirectoryRecursiveReader,SampleFireReader,
#                                     PDFUrlReader,JsonReader,StrReader,GithubReader,WebReader,ObsidianlReader)
#
# class LoadDataUnitTests(unittest.TestCase):
#     data_path  = '/Users/zhaoxuefeng/GitHub/zxftools/zxftools/tknode/rag/data/'
#     def test_is_url(self):
#         result = is_url('https://docs.llamaindex.ai/')
#         self.assertTrue(result)
#
#     def test_Reader(self):
#
#         #PDFUrlReader
#         reader = DirectoryRecursiveReader(self.data_path)
#         assert len(reader.load_data()) > 3
#         reader = DirectoryReader(self.data_path)
#         assert len(reader.load_data()) > 3
#         reader = SampleFireReader(os.path.join(self.data_path,'paul_graham_essay.txt'))
#         assert len(reader.load_data()) ==1
#         reader = PDFUrlReader('https://arxiv.org/pdf/1705.07552')
#         assert len(reader.load_data()) > 3
#
#     def test_ReaderTime_Memory(self):
#         def work1():
#             reader = DirectoryRecursiveReader(self.data_path)
#             assert len(reader.load_data()) > 3
#
#         mem_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
#         execution_time = timeit.timeit(work1, number=1)
#         mem_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
#         size, unit = convert_kb_to_mb_gb(mem_after - mem_before)
#         print(f"内存使用：{size} {unit}")
#         print(f"执行时间：{execution_time} 秒")
#         self.assertLess(execution_time, 7)
#
#     def test_JsonReader(self):
#         reader = JsonReader(os.path.join(self.data_path, 'test.json'))
#         result = reader.load_data()
#         self.assertIsNotNone(result)
#
#     def test_StrReader(self):
#         reader = StrReader("This is a test string")
#         result = reader.load_data()
#         self.assertIsNotNone(result)
#
#     def test_DictReader(self):
#         reader = DictReader({1: "Document 1", 2: "Document 2"})
#         result = reader.load_data()
#         self.assertEqual(len(result), 2)
#
#     def test_GithubReader(self):
#         # 未通过
#         reader = GithubReader("ymcui/Chinese-Mixtral/main")
#         result = reader.load_data()
#         self.assertIsNotNone(result)
#
#     def test_WebReader(self):
#         reader = WebReader("https://docs.llamaindex.ai/")
#         result = reader.load_data()
#         self.assertIsNotNone(result)
#
#     def test_ObsidianlReader(self):
#         # 笔记
#         reader = ObsidianlReader()
#         result = reader.load_data()
#         self.assertIsNotNone(result)
#
#     def test_ImageTabularReader(self):
#         reader = ImageTabularReader(os.path.join(self.data_path, 'marine_chart.png'))
#         result = reader.load_data()
#         self.assertIsNotNone(result)
#
#     def test_route(self):
#         result = automatic_route_selection(self.data_path)
#         self.assertEqual(result,'directory','信息1')
#
#         result = automatic_route_selection(os.path.join(self.data_path, 'test.json'))
#         self.assertEqual(result, 'json')
#
#         data = '/path/to/file.txt'
#         result = automatic_route_selection(os.path.join(self.data_path, 'chat_stream.py'))
#         self.assertEqual(result, 'file')
#
#
#         data = 'https://arxiv.org/pdf/1705.07552'
#         result = automatic_route_selection(data)
#         self.assertEqual(result, 'pdfs')
#
#
#         data = 'https://docs.llamaindex.ai/'
#         result = automatic_route_selection(data)
#         self.assertEqual(result, 'web')
#
#
#         data = 'This is a string'
#         result = automatic_route_selection(data)
#         self.assertEqual(result, 'str')
#
#
#         data = {'key': 'value'}
#         result = automatic_route_selection(data)
#         self.assertEqual(result, 'dict')
#
#         data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
#         result = automatic_route_selection(data)
#         self.assertEqual(result, 'DataFrame')
#
#         data = 'https://github.com/username/repo'
#         result = automatic_route_selection(data)
#         self.assertEqual(result, 'github')
#
#     # 测试异常
#     def test_add_type_error(self):
#         with self.assertRaises(TypeError):
#             pass
#             # add(1, "two")


# 运行所有测试


if __name__ == '__main__':
    unittest.main()