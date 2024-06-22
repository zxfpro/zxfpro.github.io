import os
import time
def interpret_intent(statement: str) -> str:
    """
    根据给定的语句和背景信息推断用户真正的意图。
    """
    # 根据语句和背景信息进行意图推断的逻辑
    inferred_intent = """
用户希望编写一个软件著作权的申请书,但是我们还需要编写主体,相关材料等信息
    """
    inferred_intent = input(statement)
    # cache 一下内容  statement : inferred_intent

    # cache 整合策略点 带点

    return inferred_intent


def gather_required_info(ask: str) -> str:
    """
    可以根据这个函数来向用户索要相关的信息
    """
    result = input(ask)
    return result



def human_inter_with_txt(self, text: str) -> str:
    """
    inter with human
    :param text:
    :return:
    """
    if not os.path.exists('.temp.txt'):
        with open('.temp.txt', 'w') as file:
            file.write('')
    print(text)
    while True:
        with open('.temp.txt', 'r') as file:
            result = file.read()
        if result:
            break

        time.sleep(0.5)  # Wait for specified time before checking again

    os.remove('.temp.txt')

    return result


# 人工交互
def human_2_0_inp(self):
    input_value = input('Please input: ')
    with open('.temp.txt', 'w') as file:
        file.write(input_value)

def search_brave(content:str)->str:
    """
    这个工具可以通过搜索引擎BraveSearch 获得信息
    """
    from langchain_community.tools import BraveSearch
    tool = BraveSearch.from_api_key(api_key=os.environ.get("Brave_API_KEY"), search_kwargs={"count": 3})
    result = tool.run(content)
    return result

def search_arxiv(content:str)->str:
    """
    这个工具可以通过搜索论文网站arxiv 获得信息
    """
    from langchain_community.utilities import ArxivAPIWrapper
    arxiv = ArxivAPIWrapper()
    docs = arxiv.run(content)
    return docs

def search_stackexchange(content:str)->str:
    """
    这个工具可以通过搜索论坛网站StackExchange 获得信息
    """
    from langchain_community.utilities import StackExchangeAPIWrapper
    stackexchange = StackExchangeAPIWrapper()
    result = stackexchange.run(content)
    return result

def search_SearchAPI(content:str)->str:
    """
    这个工具可以通过搜索API获得信息
    """
    from langchain_community.utilities import SearchApiAPIWrapper
    search = SearchApiAPIWrapper()
    result = search.run(content)
    return result


def search_tavily(content:str)->str:
    """
    这个工具可以通过搜索Tavily获得信息
    """
    from langchain_community.tools.tavily_search import TavilySearchResults
    tool = TavilySearchResults()
    return tool.invoke({"query": content})

def search_wikidata(content:str)->str:
    """
    这个工具可以通过搜索维基数据获得信息
    """
    from langchain_community.tools.wikidata.tool import WikidataAPIWrapper, WikidataQueryRun

    wikidata = WikidataQueryRun(api_wrapper=WikidataAPIWrapper())
    result = wikidata.run(content)
    return result

def search_wikipediaQuery(content:str)->str:
    """
    这个工具可以通过搜索维基百科获得信息
    """
    from langchain_community.utilities import WikipediaAPIWrapper
    from langchain.tools import WikipediaQueryRun
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    result = wikipedia.run(content)
    return result

