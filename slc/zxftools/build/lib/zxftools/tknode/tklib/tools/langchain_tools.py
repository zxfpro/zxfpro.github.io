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


from zxftools.tknode.tklib.tools.base import BaseTools
import os
from exa_py import Exa

class ExaTools(BaseTools):
    register_default = ['search', 'find_similar', 'get_contents']

    def __init__(self, register=[]):
        super().__init__(register, self.register_default)
        self.exa = Exa(api_key=os.environ["EXA_API_KEY"])

    def search(self, query: str):
        """Search for a webpage based on the query."""
        return self.exa.search(f"{query}", use_autoprompt=True, num_results=5)

    def find_similar(self, url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return self.exa.find_similar(url, num_results=5)

    def get_contents(self, ids: list[str]):
        """Get the contents of a webpage.
        The ids passed in should be a list of ids returned from `search`.
        """
        return self.exa.get_contents(ids)

