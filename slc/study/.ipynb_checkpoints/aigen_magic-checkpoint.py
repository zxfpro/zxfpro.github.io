from IPython.core.magic import register_line_cell_magic
import re
import os
import inspect
import difflib
import colorama
from llama_index.llms.openai import OpenAI as _openai
def get_llm(model = 'gpt-3.5-turbo-0613',temperature=0.1,**kwargs):
    llm_name = os.environ.get('aigen_llm') or model
    temperature = float(os.environ.get('aigen_temperature')) or temperature
    llm = _openai(llm_name,temperature=temperature,**kwargs)
    return llm


c_prompt = """
{detail_prompt}

Modify the existing code according to the new requirements and output the new code that meets the requirements
---------------
the existing code:
{cell}
---------------
new requirements:
{prompt}
---------------
Modified new code:
"""
w_prompt = """
{detail_prompt}
please write a piece of code as requested above
----------------
{prompt} 
"""

r_prompt = """
{prompt}
{detail_prompt}
----------------
code:
{cell}
----------------
Check the existing code, please follow the above tips, fix the error and explain the reason, keep the original comment and correct content

right code:

"""
a_prompt = """
{prompt}
{detail_prompt}

"""

t_prompt = """
{prompt}
{detail_prompt}

Those are the tips
----------------
code:
{cell}
----------------
Follow the code provided and write a test code for this function with the prompts.

test code:
"""

d_prompt = """
{prompt}
{detail_prompt}

Those are the tips
----------------
code:
{cell}
----------------

Follow the code provided and document the API in markdown's format. The code part uses 
```python   <code>```

API document:
"""


def modify_code(text):
    if text.startswith('-'):
        modified_text = colorama.Fore.RED + text + colorama.Style.RESET_ALL
    elif text.startswith('+'):
        modified_text = colorama.Fore.GREEN + text + colorama.Style.RESET_ALL
    elif text.startswith('?'):
        modified_text = colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL
    else:
        modified_text = text
    return modified_text


def show_diff(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))
    return '\n'.join([modify_code(i) for i in diff])


def get_python_code(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)

    for match in matches:
        yield match.strip()


def split_cell(cell, separator="<PROMPT END>"):
    if separator not in cell:
        prompts = ''
    else:
        prompts, cell = cell.split(separator)

    return prompts, cell


def postprocessing(func_name, resp, line, cell, detail_prompt):
    if '```' in resp:
        codes = [i for i in get_python_code(resp)]
    else:
        codes = [resp]

    if len(codes) == 1:
        resp_back = codes[0]
    else:
        resp_back = '\n#****** nap ******** \n'.join(codes)

    resp_back = resp_back[:10].replace("code:", "") + resp_back[10:]

    detail_prompt_annotation_list = ['#' + line for line in detail_prompt.split('\n')]

    detail_prompt_annotation = '\n'.join(detail_prompt_annotation_list) + '<PROMPT END>\n'

    detail_prompt_annotation = detail_prompt_annotation if detail_prompt != '' else ''

    content = f'# %%{func_name} {line}\n' + detail_prompt_annotation + resp_back

    print(show_diff(cell, resp_back))  # TODO
    get_ipython().set_next_input(content, replace=True)


def postprocessing2(func_name, detail_prompt, cell, line, resp):
    content_ = '\n'.join([detail_prompt, cell])

    content = f'# %%{func_name} {line}\n' + content_

    get_ipython().set_next_input(content, replace=True)
    get_ipython().set_next_input(resp)


@register_line_cell_magic
def aigen(line, cell=None):
    """
    -h 查看help
    """
    llm = get_llm()  # llm
    inputs = line.split(' ', 1)
    params = inputs[0]
    prompt = inputs[-1]

    if not cell:
        complete_prompt = a_prompt.format(detail_prompt='', prompt=prompt)
        resp = llm.complete(complete_prompt).text
        print(resp)
        return

    if not params.startswith('-'):
        params = '-c'
        prompt = line

    detail_prompt, cell = split_cell(cell)
    func_name = inspect.currentframe().f_code.co_name
    # llm params prompt
    # detail_prompt cell

    if params == '-c':
        complete_prompt = c_prompt.format(detail_prompt=detail_prompt, cell=cell, prompt=prompt)
        resp = llm.complete(complete_prompt).text
        postprocessing(func_name, resp, line, cell, detail_prompt)

    elif params == '-w':
        # 提需求 加一个需求分析的mode
        complete_prompt = w_prompt.format(detail_prompt=detail_prompt, prompt=prompt)
        resp = llm.complete(complete_prompt).text
        postprocessing(func_name, resp, line, cell, detail_prompt)

    elif params == '-r':
        complete_prompt = r_prompt.format(detail_prompt=detail_prompt, cell=cell, prompt=prompt)
        resp = llm.complete(complete_prompt).text
        postprocessing(func_name, resp, line, cell, detail_prompt)

    elif params == '-a':
        complete_prompt = a_prompt.format(detail_prompt=detail_prompt, prompt=prompt)
        print(colorama.Fore.GREEN + complete_prompt + colorama.Style.RESET_ALL)
        resp = llm.complete(complete_prompt).text
        print(resp)

    elif params == '-t':
        complete_prompt = t_prompt.format(detail_prompt=detail_prompt, cell=cell, prompt=prompt)
        resp = llm.complete(complete_prompt).text
        postprocessing2(func_name, detail_prompt, cell, line, resp)

    elif params == '-d':
        complete_prompt = d_prompt.format(detail_prompt=detail_prompt, cell=cell, prompt=prompt)
        resp = llm.complete(complete_prompt).text
        postprocessing2(func_name, detail_prompt, cell, line, resp)

    elif params == '-h':
        print(f"""标识符:
<PROMPT END>

参数:
-c 根据需求修改代码 默认
-w 直接编写代码
-r 检查代码是否有错误
-a 直接提问交流
-t 在下一个cell中生成测试代码
-d 在下一个cell中生成API描述

更细节的描述:
如果想添加更加细节的描述,可以将细节描述加到最开始,并在结束时添加 <PROMPT END> 标识符

配置:
    llm: {os.environ.get('aigen_llm') or 'gpt-3.5-turbo-0613'}
    llm: {os.environ.get('aigen_temperature') or '0.1'}
    """)
        return

    else:
        print('参数不存在')
        return



