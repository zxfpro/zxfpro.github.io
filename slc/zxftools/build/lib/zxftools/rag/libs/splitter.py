from llama_index.core.node_parser import SentenceSplitter
from typing import Callable, List


class MarkSplitter(SentenceSplitter):
    mark = ''
    def __init__(self,mark = '##',**kwargs):
        super(MarkSplitter, self).__init__(**kwargs)
        self.mark = mark
    def _split_text(self, text: str, chunk_size: int) -> List[str]:
        return text.split(self.mark)