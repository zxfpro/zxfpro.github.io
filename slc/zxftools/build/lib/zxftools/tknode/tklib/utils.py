
from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache
from langchain.memory import ConversationEntityMemory #实体记忆
from langchain.prompts import BaseChatPromptTemplate

import os


def check_memorys(memory,prompt):
    if isinstance(memory,ConversationEntityMemory):
        assert memory.chat_history_key in prompt.input_variables
    else:
        assert memory.memory_key in prompt.input_variables
    assert memory.return_messages == isinstance(prompt, BaseChatPromptTemplate)


def llm_cache(type='memory',database_path=".langchain.db"):
    if type == 'memory':
        set_llm_cache(InMemoryCache())
    elif type == 'sql':
        set_llm_cache(SQLiteCache(database_path=database_path))

def generate_article(mode, llm, num_examples):
    """
    few shot
    输入模板 , 生成模板的不同版本,最终得到num_examples个示例
    :param mode:
    :param llm:
    :param num_examples:
    :return:
    """
    syn_text = mode
    result = mode
    for i in range(num_examples):
        resp = llm.complete(f"""
        请根据以下文章为模板,生成一篇相同格式的文本
        文章:{syn_text}
        """)
        syn_text = resp.text
        result += '\n案例:\n' + syn_text
    '案例:\n'+result
    return result

def simple_gradrail(sensitive_words: list, content: str, replace_word='X') -> str:
    # 敏感词替换
    for i in sensitive_words:
        content_B = content.replace(i, replace_word)
    return content_B


#  给我看对应原文
class CodeExtractor:
    @staticmethod
    def search_py_files(folder_path):
        py_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
        return py_files

    @staticmethod
    def search_markdown_files(folder_path):
        py_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".md"):
                    py_files.append(os.path.join(root, file))
        return py_files

    @staticmethod
    def extract_code(file_path):
        with open(file_path, "r") as file:
            code = file.read()
        return code, file_path  # returning code and file path

    @staticmethod
    def extract_markdown(file_path):
        with open(file_path, "r") as file:
            markdown = file.read()
        return markdown, file_path  # returning code and file path

    @staticmethod
    def extract_code_from_folder(folder_path):
        py_files = CodeExtractor.search_py_files(folder_path)
        code_list = []
        for file_path in py_files:
            code, file_path = CodeExtractor.extract_code(file_path)  # getting code and file path
            code_list.append((code, file_path))  # appending code and file path as a tuple
        return code_list

    @staticmethod
    def extract_markdown_from_folder(folder_path):
        py_files = CodeExtractor.search_markdown_files(folder_path)
        code_list = []
        for file_path in py_files:
            code, file_path = CodeExtractor.extract_markdown(file_path)  # getting code and file path
            code_list.append((code, file_path))  # appending code and file path as a tuple
        return code_list

    @staticmethod
    def print_code_from_folder(folder_path):
        code_list = CodeExtractor.extract_code_from_folder(folder_path)
        xx = ""
        for code, file_path in code_list:  # iterating through code and file path
            file_path = "## " + file_path
            xx += file_path
            xx += code

            # print("\033[91mFile Path:", file_path)  # printing file path in red
            # print("\033[92m" + code)  # printing code in green
            # print("\n")  # adding a new line for separation

        return xx

    @staticmethod
    def print_code_from_folder_list(folder_path):
        code_list = CodeExtractor.extract_code_from_folder(folder_path)
        xx = ''
        pp = {}
        for code, file_path in code_list:  # iterating through code and file path
            pp[file_path] = code

            # print("\033[91mFile Path:", file_path)  # printing file path in red
            # print("\033[92m" + code)  # printing code in green
            # print("\n")  # adding a new line for separation

        return pp

    @staticmethod
    def print_markdown_from_folder(folder_path, verbose=False):
        code_list = CodeExtractor.extract_markdown_from_folder(folder_path)
        xx = ""
        for code, file_path in code_list:  # iterating through code and file path
            file_path = "## " + file_path
            xx += file_path
            xx += code
            if verbose:
                print("\033[91mFile Path:", file_path)  # printing file path in red
                print("\033[92m" + code)  # printing code in green
                print("\n")  # adding a new line for separation

        return xx

