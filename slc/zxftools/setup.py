from setuptools import setup, find_packages

setup(name='zxftools',  # 包名
      version="2.3.20",
      author='zhaoxuefeng',  # 作者
      packages=find_packages(),
      # package_data={'zxftools':['tknode/tklib/prompt/*','tknode/tklib/prompt/*']},
      # package_data={'zxftools': ['data/English/*']},
      py_modules=[],
      install_requires=['numpy<=1.26.2','setproctitle'],

      extras_require = {
            'project': ['chardet~=5.2.0','dill~=0.3.8','pyyaml','loguru'],
            'llms': ['azure-cognitiveservices-speech'],
            'rag': ['diskcache',
                           'llama-index~=0.10.26',
                           'langchain~=0.1.14',
                           'llama-index-retrievers-bm25~=0.1.3',
                           'paramiko~=3.4.0',
                           'beautifulsoup4~=4.12.3'
                           ],
      },
      description='一个工具包',
      include_package_data = True,
      entry_points = {},
      # ext_modules= cythonize(["aaa.pyx"],
      )
