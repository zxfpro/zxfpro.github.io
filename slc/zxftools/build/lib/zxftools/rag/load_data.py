from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document
import json
from pathlib import Path
import os
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
# from llama_index.readers.weather import WeatherReader
# from llama_index.readers.maps import OpenMap





def get_folder_paths_with_files(directory):
    folder_paths = []
    for root, dirs, files in os.walk(directory):
        if files:
            folder_paths.append(root)
    return folder_paths


def is_url(string):
    pattern = re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    return bool(re.match(pattern, string))

class BaseReader():
    def __init__(self,value=None):
        self.value = value

    def load_data(self):
        pass

class DirectoryRecursiveReader(BaseReader):
    def __init__(self,files):
        super().__init__()
        folders = get_folder_paths_with_files(files)
        self.reader = [SimpleDirectoryReader(folder, filename_as_id=True) for folder in folders]
        self.files = files
    def load_data(self):
        document = []
        for i_reader in self.reader:
            document += i_reader.load_data()
        return document

class DirectoryReader(BaseReader):
    def __init__(self,files):
        super(DirectoryReader, self).__init__()
        self.reader = SimpleDirectoryReader(files, filename_as_id=True)
        self.files = files
    def load_data(self):
        return self.reader.load_data()

class SampleFireReader(BaseReader):
    def __init__(self, file,**kwargs):
        super(SampleFireReader, self).__init__()
        self.reader = SimpleDirectoryReader(input_files=[file],filename_as_id = kwargs.get('filename_as_id'),
                                            num_files_limit=kwargs.get('num_files_limit'))

    def load_data(self):
        return self.reader.load_data()

class PDFUrlReader(BaseReader):
    def __init__(self, pdf_url):
        super().__init__()
        try:
            from llama_index.readers.smart_pdf_loader import SmartPDFLoader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "pip install llama-index-readers-smart-pdf-loader"')

        self.reader = SmartPDFLoader(llmsherpa_api_url="https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all")
        self.pdf_url = pdf_url
    def load_data(self):
        return self.reader.load_data(self.pdf_url)

class JsonReader(BaseReader):
    def __init__(self, file):
        super(JsonReader, self).__init__()
        try:
            from llama_index.readers.json import JSONReader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "pip install llama-index-readers-json"')

        self.reader = JSONReader()
        self.file = file
    def load_data(self):
        return self.reader.load_data(self.file)

class StrReader(BaseReader):
    def __init__(self,strs,**kwargs):
        super(StrReader, self).__init__()
        self.strs = strs
        self.doc_id = kwargs.get('doc_id',None)
    def load_data(self):
        if self.doc_id:
            return [Document(text = self.strs,doc_id=self.doc_id)]
        else:
            return [Document(text=self.strs)]



class ChatGPTShareUrlReader(BaseReader):
    def __init__(self, url):
        super(ChatGPTShareUrlReader, self).__init__()

        self.url = url

    def load_data(self):
        result = requests.get(self.url).content
        soup = BeautifulSoup(result, 'html.parser')
        tags = soup.find('script', id='__NEXT_DATA__')
        data = json.loads(tags.string)
        mapping = data['props']['pageProps']['serverResponse']['data']['mapping']

        documents = []
        for doc_id, content in mapping.items():
            message = content.get('message')
            if message:
                parts = message.get('content', {}).get('parts', [])
                if parts:
                    text = parts[0]
                    doc = Document(doc_id=doc_id, text=text)
                    doc.metadata['file_path'] = doc_id
                    documents.append(doc)
        documents.reverse()
        return documents


class DictReader(BaseReader):
    def __init__(self,dicts):
        super(DictReader, self).__init__()
        self.dicts = dicts
    def load_data(self):
        documents = []
        for doc_id, doc_text in self.dicts.items():
            documents.append(Document(doc_id=doc_id, text=doc_text))
            documents[-1].metadata['file_path'] = doc_id
        return documents


class WebReader(BaseReader):
    def __init__(self, urls):
        super(WebReader, self).__init__()
        try:
            from llama_index.readers.web import SimpleWebPageReader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "pip install llama-index-readers-web"')

        self.reader = SimpleWebPageReader(html_to_text=True)
        self.urls = urls
    def load_data(self):
        return self.reader.load_data(urls=[self.urls])
        # return self.reader.load_data(urls=self.urls)


class GithubReader(BaseReader):
    def __init__(self,owner_repo_branch: str):
        """
        只能够 读取public
        for example:
         'github:zxfpro/AI_coder_for_notebook/main'

        github:owner/repo/branch
        :param owner:
        :param repo:
        :param branch:
        """

        super(GithubReader, self).__init__()
        owner_repo_branch = owner_repo_branch.replace('github:','')
        owner,repo,branch = owner_repo_branch.split('/')
        try:
            from llama_index.readers.github import GithubClient, GithubRepositoryReader, \
                GitHubRepositoryCollaboratorsReader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "pip install llama-index-readers-github"')

        self.reader  = GithubRepositoryReader(GithubClient(github_token=os.environ.get('GitHub_Token'),verbose=True),
                                        owner,
                                        repo,
                                        use_parser=False,
                                        verbose=True,
                                        filter_directories=(["docs"], GithubRepositoryReader.FilterType.INCLUDE,),
                                        filter_file_extensions=(
                                          [".png",".jpg",".jpeg",".gif",".svg",".ico","json",".ipynb",],
                                          GithubRepositoryReader.FilterType.EXCLUDE,),
                                      )
        self.branch = branch
    def load_data(self):
        return self.reader.load_data(branch=self.branch)



class ObsidianlReader(BaseReader):
    def __init__(self,inputs):
        super().__init__()
        try:
            from llama_index.readers.obsidian import ObsidianReader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "llama-index-readers-obsidian"')


        if inputs.startswith('obsidian:'):
            input_dir = "/Users/zhaoxuefeng/Documents"
        self.reader = ObsidianReader(input_dir)
    def load_data(self):
        return self.reader.load_data()


class WikipedialReader(BaseReader):
    def __init__(self,inputs):
        # pages = ["OpenAI", "Sam Altman", "Mira Murati", "Emmett Shear"]
        super().__init__()
        try:
            from llama_index.readers.wikipedia import WikipediaReader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "llama-index-readers-wikipedia"')
        if inputs.startswith('wikipedia:'):
            pages = [inputs.replace('wikipedia:','')]

        self.reader = WikipediaReader()
        self.pages = pages
    def load_data(self):
        return self.reader.load_data(pages=self.pages,auto_suggest=False,)


class ImageTabularReader(BaseReader):
    def __init__(self,image_path,keep_image=True):
        super().__init__()
        try:
            from llama_index.readers.file import ImageTabularChartReader
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "llama-index-readers-file"')

        self.reader = ImageTabularChartReader(keep_image=keep_image)
        self.file = Path(image_path)
    def load_data(self):
        return self.reader.load_data(file = self.file)

# get image_documents
# image_path = "./images"
# image_documents = SimpleDirectoryReader(image_path).load_data()


def automatic_route_selection(data,params=None):
    # 考虑将其做成一个神经网络
    if isinstance(data, str):
        if os.path.isdir(data):
            if params == 'r':
                data_type = 'directory_recursive'
            else:
                data_type = 'directory'
        elif os.path.isfile(data):
            data_type = 'json' if data.endswith('json') else 'file'
        elif is_url(data):
            if data.startswith('https://arxiv.org/pdf'):
                data_type = 'pdfs'
            elif data.startswith('https://github'):
                data_type = 'github'
            elif data.startswith('https://chatgpt.com/share'):
                data_type = 'chatgpturl'
            else:
                data_type = 'pdfs' if data.endswith('pdf') else 'web'
        else:
            if data.startswith('github:'):
                data_type = 'github'
            elif data.startswith('obsidian:'):
                data_type = 'obsidian'
            elif data.startswith('wikipedia:'):
                data_type = 'wikipedia'

            else:
                data_type = 'str'

    elif isinstance(data,dict):
        data_type = 'dict'
    elif isinstance(data,pd.DataFrame):
        data_type = 'DataFrame'
    else:
        data_type = None
    return data_type


def load_data(data,type=None,params=None,**kwargs):
    """

    :param data = ? 输入需要加载的数据
    :param type = 可以指定 支持自动识别
    :return:
    """
    data_types = type or automatic_route_selection(data,params=params)

    Reader_dict = {
        'str': StrReader,
        'dict': DictReader,
        'json': JsonReader,
        'directory_recursive': DirectoryRecursiveReader,
        'directory':DirectoryReader,
        'file':SampleFireReader,
        'pdfs': PDFUrlReader,
        'chatgpturl':ChatGPTShareUrlReader,
        'web':WebReader,
        'wikipedia':WikipedialReader,
        'obsidian':ObsidianlReader,
        'github': GithubReader,
        # 'DataFrame':,
                     }

    reader_obj = Reader_dict.get(data_types)
    reader = reader_obj(data,**kwargs)
    return reader.load_data()


if __name__ == '__main__':
    pass
