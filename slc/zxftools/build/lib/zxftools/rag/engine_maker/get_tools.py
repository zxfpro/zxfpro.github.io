from enum import Enum
from .libs.tools import *

# 说的啥话不记得了 但是那个意思就是说 xxxx
class ToolsType(Enum):
    Math = 'Math'
    search_brave = 'search_brave'
    search_arxiv = 'search_arxiv'
    search_stackexchange = 'search_stackexchange'
    search_SearchAPI = 'search_SearchAPI'
    search_tavily = 'search_tavily'
    search_wikidata = 'search_wikidata'
    search_wikipediaQuery = 'search_wikipediaQuery'
    Coder = 'Coder'
    File = 'File'
    HumanIO = 'HumanIO'
    Shell = 'Shell'
    Web = 'Web'
    # ArxivToolSpec = 'ArxivToolSpec'
    # CusTavilyToolSpec = 'CusTavilyToolSpec'
    # WikipediaToolSpec = 'WikipediaToolSpec'

def get_tools(type:ToolsType):
    if type.value == 'Math':

        print(MathTools.register_default)
        return MathTools,'class'
    elif type.value == 'search_brave':
        return search_brave,'single'
    elif type.value == 'search_arxiv':
        return search_arxiv,'single'
    elif type.value == 'search_stackexchange':
        return search_stackexchange,'single'
    elif type.value == 'search_SearchAPI':
        return search_SearchAPI,'single'
    elif type.value == 'search_tavily':
        return search_tavily,'single'
    elif type.value == 'search_wikidata':
        return search_wikidata,'single'
    elif type.value == 'search_wikipediaQuery':
        return search_wikipediaQuery,'single'
    elif type.value == 'Coder':
        return CoderTools,'class'
    elif type.value == 'File':
        return FileTools,'class'
    elif type.value == 'HumanIO':
        return HumanIOTools,'class'
    elif type.value == 'Shell':
        return ShellTools,'class'
    elif type.value == 'Web':
        return WebTools,'class'
    # elif type.value == 'ArxivToolSpec':
    #     return ArxivToolSpec,'origin'
    # elif type.value == 'CusTavilyToolSpec':
    #     return CusTavilyToolSpec,'origin'
    # elif type.value == 'WikipediaToolSpec':
    #     return WikipediaToolSpec,'origin'

