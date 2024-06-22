from llama_index.core.node_parser import (
    HierarchicalNodeParser,
    SemanticSplitterNodeParser,
    SentenceWindowNodeParser,
    SentenceSplitter,
    TokenTextSplitter,
    MarkdownNodeParser,
    JSONNodeParser,
    LangchainNodeParser,
    CodeSplitter,
    HTMLNodeParser,
    NodeParser,
    SimpleFileNodeParser,
    MarkdownElementNodeParser,
    UnstructuredElementNodeParser,
    LlamaParseJsonNodeParser,
    SimpleNodeParser,
)
from llama_index.embeddings.openai import OpenAIEmbedding
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter


from .libs import MarkSplitter
from .utils import pop_get
from enum import Enum




class SplitterType(Enum):
    SENTENCE = 'sentence'
    SENTENCE_WINDOW = 'sentence_window'
    TOKEN_TEXT = 'token_text'
    MARK = 'mark_custom'
    SEMANTIC = 'semantic'
    HIERARCHICAL = 'hierarchical'
    CODE = 'code'
    MARKDOWN = 'markdown'
    JSON = 'json'
    HTML = 'html'
    LANGCHAIN = 'langchain'

    HELP = f"""
Sentence : 切分
SentenceWindow : 切分 (包含上下文)
TokenText : token 切分
Mark : 按照 特定符号切分

        sentence : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        sentence_window : kwargs [window_size 3, window_metadata_key window   original_text_metadata_key  original_sentence]
        token_text : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        mark : "mark","##"
        semantic : buffer_size 1   breakpoint_percentile_threshold 95
        hierarchical: chunk_sizes [2048, 512, 128]
        code : language','python'  'chunk_lines',80) 'chunk_lines_overlap',15) 'max_chars',4000)


other:
     semantic   # 主要适用于英语句子
     # from llama_index.core.node_parser import SimpleFileNodeParser
     # splitter = SimpleFileNodeParser()
"""

class SplitterFactory:
    def __new__(cls, type:SplitterType or str,verbose=False, **kwargs):
        """

        sentence : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        sentence_window : kwargs [window_size 3, window_metadata_key window   original_text_metadata_key  original_sentence]
        token_text : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        mark : "mark","##"
        semantic : buffer_size 1   breakpoint_percentile_threshold 95
        hierarchical: chunk_sizes [2048, 512, 128]
        code : language','python'  'chunk_lines',80) 'chunk_lines_overlap',15) 'max_chars',4000)

        :param splitter_type:
        :param verbose:
        :param kwargs:
        """
        project_name = type if isinstance(type, str) else type.value


        if project_name == 'sentence':
            chunk_size = pop_get(kwargs, 'chunk_size', 404)
            chunk_overlap = pop_get(kwargs, 'chunk_overlap', 20)
            separator = pop_get(kwargs, 'separator', ' ')
            if verbose:
                print(f'''Params : [ chunk_size={chunk_size} 
                                     chunk_overlap={chunk_overlap} 
                                     separator={separator} ]''')
            splitter = SentenceSplitter.from_defaults(chunk_size=chunk_size, chunk_overlap=chunk_overlap,
                                                      separator=separator, **kwargs)

        elif project_name == 'sentence_window':
            window_size = kwargs.get("window_size", 3)
            window_metadata_key = kwargs.get("window_metadata_key", "window")
            original_text_metadata_key = kwargs.get("original_text_metadata_key", "original_sentence")
            if verbose:
                print(f'''Params : [ window_size={window_size} window_metadata_key={window_metadata_key} original_text_metadata_key={original_text_metadata_key} ]''')
            # 这对于生成具有非常特定范围的嵌入最有用。然后，结合MetadataReplacementNodePostProcessor，您可以在将节点发送到LLM之前将句子替换为周围的上下文。
            splitter = SentenceWindowNodeParser.from_defaults(
                window_size=window_size,# how many sentences on either side to capture
                window_metadata_key=window_metadata_key,# the metadata key that holds the window of surrounding sentences
                original_text_metadata_key=original_text_metadata_key,# the metadata key that holds the original sentence
            )

        elif project_name == 'token_text':
            chunk_size = pop_get(kwargs,'chunk_size',404)
            chunk_overlap = pop_get(kwargs, 'chunk_overlap', 20)
            separator = pop_get(kwargs, 'separator', ' ')
            if verbose:
                print(f'''Params : [ chunk_size={chunk_size} 
                                     chunk_overlap={chunk_overlap} 
                                     separator={separator} ]''')
            splitter = TokenTextSplitter.from_defaults(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=separator, **kwargs)

        elif project_name == 'mark_custom':
            if verbose:
                print(f'Params : [ mark={kwargs.get("mark","##")} ]')
            splitter = MarkSplitter(mark=kwargs.get('mark','##'))

        elif project_name == 'hierarchical':
            splitter = HierarchicalNodeParser.from_defaults(chunk_sizes=kwargs.get('chunk_sizes',[2048, 512, 128]))


        elif project_name == 'code':
            # code
            language = kwargs.get('language','python')
            chunk_lines = kwargs.get('chunk_lines',80)
            chunk_lines_overlap = kwargs.get('chunk_lines_overlap',15)
            max_chars = kwargs.get('max_chars',4000)
            splitter = CodeSplitter(
                language=language,
                chunk_lines=chunk_lines,  # lines per chunk
                chunk_lines_overlap=chunk_lines_overlap,  # lines overlap between chunks
                max_chars=max_chars,  # max chars per chunk
                **kwargs
            )

        elif project_name == 'markdown':
            splitter = MarkdownNodeParser.from_defaults(include_metadata = kwargs.get('include_metadata', True),
                                                        include_prev_next_rel = kwargs.get('include_prev_next_rel', True),
                                                        callback_manager = kwargs.get('callback_manager', None))

        elif project_name == 'json':
            splitter = JSONNodeParser.from_defaults(include_metadata = kwargs.get('include_metadata', True),
                                                    include_prev_next_rel = kwargs.get('include_prev_next_rel', True),
                                                    callback_manager = kwargs.get('callback_manager', None),)

        elif project_name == 'html':
            splitter = HTMLNodeParser(tags=kwargs.get('tags', ["p", "h1"]))  # optional list of tags
            # 默认标签是：["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "b", "i", "u", "section"]
        elif project_name == 'langchain':
            # langchain
            langchain_splitter = kwargs.get('langchain_splitter',None)
            langchain_splitter = langchain_splitter or RecursiveCharacterTextSplitter
            issubclass(langchain_splitter, TextSplitter)
            splitter = LangchainNodeParser(langchain_splitter())

        # TODO ####################
        # from llama_index.core.node_parser import # 有十几个吧
        elif project_name == 'semantic':



            buffer_size = kwargs.get('buffer_size', 1)
            breakpoint_percentile_threshold = kwargs.get('breakpoint_percentile_threshold', 95)
            embedd = OpenAIEmbedding()# TODO
            splitter = SemanticSplitterNodeParser(buffer_size=buffer_size,
                                                  breakpoint_percentile_threshold=breakpoint_percentile_threshold,
                                                  embed_model=embedd)


        else:
            raise ValueError("Invalid splitter name")
        return splitter
