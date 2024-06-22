from llama_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor
)
from enum import Enum
from .utils import pop_get
from .libs import HumanExtractor, PProgramExtractor, StudyExtractor

class ExtractorType(Enum):
    TITLE = 'title'
    QUESTIONS_ANSWERED = 'qad'
    SUMMARY = 'summary'
    KEYWORD = 'keyword'
    STUDY = 'study'

    CUSTOM_EXTRACTOR = 'human_custom'
    PPROGRAM_EXTRACTOR = 'PProgram_custom'
    ENTITY = 'entity'

    HELP = f"""
TITLE_EXTRACTOR = 'Title'
QUESTIONS_ANSWERED_EXTRACTOR = 'QuestionsAnswered'
SUMMARY_EXTRACTOR = 'Summary'

TT
    #TODO 做一个实体提取 
    # marven 测试不通 Entity
    # metadata_mode=MetadataMode.EMBED, num_workers=8
    # list of summaries to extract: 'self', 'prev', 'next'
"""

class ExtractorFactory:
    def __new__(cls, type:ExtractorType or str, verbose=False,**kwargs):
        project_name = type if isinstance(type, str) else type.value

        if project_name == 'title':
            nodes = pop_get(kwargs,'nodes',5)
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')

            return TitleExtractor(nodes=nodes, llm=llm,**kwargs)
        elif project_name == 'qad':
            questions = pop_get(kwargs,'questions',3)
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ questions={questions} 
                                     llm={llm} ]''')
            return QuestionsAnsweredExtractor(questions=questions, llm=llm)
        elif project_name == 'summary':
            summaries = pop_get(kwargs,'summaries',["prev", "self"])
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ summaries={summaries} 
                                     llm={llm} ]''')
            return SummaryExtractor(summaries=summaries, llm=llm)
        elif project_name == 'keyword':
            keywords = pop_get(kwargs,'keywords',10)
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ keywords={keywords} 
                                     llm={llm} ]''')
            return KeywordExtractor(keywords=keywords, llm=llm)
        elif project_name == 'study':
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ llm={llm} ]''')
            return StudyExtractor(llm=llm)

        elif project_name == 'human_custom':
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ llm={llm} ]''')
            return HumanExtractor()

        elif project_name == 'PProgram_custom':
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ llm={llm} ]''')
            return PProgramExtractor(llm=llm)
        elif project_name == 'entity':
            from llama_index.extractors.entity import EntityExtractor
            return  EntityExtractor(
                prediction_threshold=0.5,
                label_entities=False,  # include the entity label in the metadata (can be erroneous)
                device="cpu",  # set to "cuda" if you have a GPU
            )
        else:
            raise ValueError(f'Invalid extractor type: {project_name}')

