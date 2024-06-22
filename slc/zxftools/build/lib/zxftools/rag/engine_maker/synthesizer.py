
from llama_index.core.response_synthesizers import Refine,Accumulate,BaseSynthesizer,CompactAndRefine,Generation,SimpleSummarize,TreeSummarize

from enum import Enum

class ResponseSynthesizerType(Enum):
    Refine = 'Refine'
    Accumulate = 'Accumulate'
    BaseSynthesizer = 'BaseSynthesizer'
    CompactAndRefine = 'CompactAndRefine'
    TreeSummarize = 'TreeSummarize'

class ResponseSynthesizerFactory:
    def __new__(cls, resp_syn_type: ResponseSynthesizerType=ResponseSynthesizerType.Refine,**kwargs):
        if resp_syn_type.value == 'Refine':
            syn = Refine()
        elif resp_syn_type.value == 'Accumulate':
            syn = Accumulate()
        elif resp_syn_type.value == 'BaseSynthesizer':
            syn = BaseSynthesizer()
        elif resp_syn_type.value == 'CompactAndRefine':
            syn = CompactAndRefine()
        elif resp_syn_type.value == 'TreeSummarize':
            syn = TreeSummarize()
        else:
            raise Exception('不支持')
        return syn
