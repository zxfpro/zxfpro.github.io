from llama_index.core import SimpleDirectoryReader
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
from llama_index.readers.web import SimpleWebPageReader
from llama_index.readers.json import JSONReader
from llama_index.readers.weather import WeatherReader
from llama_index.readers.github import GithubClient, GithubRepositoryReader,GitHubRepositoryCollaboratorsReader
from llama_index.core import Document
from llama_index.readers.maps import OpenMap
from llama_index.readers.file import ImageTabularChartReader
from llama_index.readers.obsidian import ObsidianReader
from pathlib import Path
import os
import re
import pandas as pd
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
        self.reader = SmartPDFLoader(llmsherpa_api_url="https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all")
        self.pdf_url = pdf_url
    def load_data(self):
        return self.reader.load_data(self.pdf_url)

class JsonReader(BaseReader):
    def __init__(self, file):
        super(JsonReader, self).__init__()
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

class GithubReader(BaseReader):
    #TODO
    def __init__(self,owner_repo_branch: str):
        """
        # branch="branch"  commit_sha="commit_sha"
        owner/repo/branch
        :param owner:
        :param repo:
        :param branch:
        """

        super(GithubReader, self).__init__()
        owner,repo,branch = owner_repo_branch.split('/')
        self.reader  = GithubRepositoryReader(GithubClient(github_token=os.environ.get('GitHub_Token'),verbose=True),
                                        owner,
                                        repo,
                                        use_parser=False,
                                        verbose=True,
                                        )
        self.branch = branch
    def load_data(self):
        return self.reader.load_data(branch=self.branch)

class WebReader(BaseReader):
    def __init__(self, urls):
        super(WebReader, self).__init__()
        self.reader = SimpleWebPageReader(html_to_text=True)
        self.urls = urls
    def load_data(self):
        return self.reader.load_data(urls=[self.urls])
        # return self.reader.load_data(urls=self.urls)


class ObsidianlReader(BaseReader):
    def __init__(self,input_dir="/Users/zhaoxuefeng/Documents"):
        super().__init__()
        self.reader = ObsidianReader(input_dir)
    def load_data(self):
        return self.reader.load_data()

class ImageTabularReader(BaseReader):
    def __init__(self,image_path,keep_image=True):
        super().__init__()
        self.reader = ImageTabularChartReader(keep_image=keep_image)
        self.file = Path(image_path)
    def load_data(self):
        return self.reader.load_data(file = self.file)


def automatic_route_selection(data):
    if isinstance(data, str):
        if os.path.isdir(data):
            data_type = 'directory'
        elif os.path.isfile(data):
            data_type = 'json' if data.endswith('json') else 'file'
        elif is_url(data):
            if data.startswith('https://arxiv.org/pdf'):
                data_type = 'pdfs'
            elif data.startswith('https://github'):
                data_type = 'github'
            else:
                data_type = 'pdfs' if data.endswith('pdf') else 'web'
        else:
            data_type = 'str'

    elif isinstance(data,dict):
        data_type = 'dict'
    elif isinstance(data,pd.DataFrame):
        data_type = 'DataFrame'
    else:
        data_type = None
    return data_type


def load_data(data,type=None,**kwargs):
    """

    :param data = ? 输入需要加载的数据
    :param type = 可以指定 支持自动识别
    :return:
    """
    data_types = type or automatic_route_selection(data)

    Reader_dict = {
        'dict': DictReader,
        'directory':DirectoryReader,
        'file':SampleFireReader,
        'json':JsonReader,
        'pdfs':PDFUrlReader,
        'web':WebReader,
        'str':StrReader,
        'github': GithubReader,
        # 'DataFrame':,
                     }

    reader_obj = Reader_dict.get(data_types)
    reader = reader_obj(data,**kwargs)
    return reader.load_data()


if __name__ == '__main__':
    pass
