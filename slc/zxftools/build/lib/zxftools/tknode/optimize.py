from .utils import NodePostprocessorsFactory,NodePostprocessorsType,load_data,IndexType,IndexMaker
import diskcache
import functools
import os

class OptConfig(object):
    def __init__(self, func_name, cache_home=None):
        self.cache_home = cache_home or os.environ.get('cache_home', './cache')
        self.cache = diskcache.Cache(os.path.join(self.cache_home, func_name))

        self.nodepost = NodePostprocessorsFactory(postprocessor=NodePostprocessorsType.SimilarityPostprocessor,
                                                  similarity_cutoff=0.77)
        documents = load_data({self.cache.get(key): str(key) for key in self.cache})
        indexs = IndexMaker().create_index(documents)
        self.retrieve = indexs.as_retriever()


def zcache(optconfig, type: str = 'exact_match'):
    """
    type  模糊匹配  精确匹配
    要求只能使用kwargs
    fuzzy_match
    """

    def outer_packing(func):

        @functools.wraps(func)
        def wrapper(**kwargs):
            if type == 'fuzzy_match':
                result_list = optconfig.nodepost.postprocess_nodes(optconfig.retrieve.retrieve(str(kwargs)))
            elif type == 'exact_match':
                result_list = optconfig.cache.get(kwargs)
            else:
                pass

            if result_list:
                if type == 'fuzzy_match':
                    result = result_list[0].metadata['file_path']
                elif type == 'exact_match':
                    result = result_list
                else:
                    pass
            else:
                result = func(**kwargs)
                optconfig.cache.set(kwargs, result, tag="data", expire=None, read=True)

            return result

        return wrapper

    return outer_packing
