import unittest

from .engine_baidu import BaiduLLM
from .llms import get_llm
from .multi_modal_llms import get_multi_modal_llms

"""
单元测试的目的是验证代码的每个部分是否按预期工作。对于`get_llm`函数，测试将集中在以下几个方面：

1. **参数验证**：确保函数能够处理各种输入参数，包括默认值和可选参数。
2. **环境变量读取**：验证函数能否正确读取环境变量。
3. **实例化逻辑**：确保根据不同的`type`参数，正确实例化了对应的语言模型（LLM）类。
4. **错误处理**：验证在缺少必要参数或环境变量时，函数是否能抛出或处理异常。

以下是单元测试的基本思路：

### 测试类：`get_llm`函数测试

#### 测试用例 1：验证默认参数
- **目的**：测试函数在不提供任何参数时的行为。
- **步骤**：
  1. 调用`get_llm()`。
  2. 验证返回的LLM实例是否符合预期（例如，使用默认模型和参数）。

#### 测试用例 2：验证自定义模型参数
- **目的**：测试函数能否接受并使用自定义模型名称。
- **步骤**：
  1. 定义一个自定义模型名称。
  2. 调用`get_llm(model="custom-model-name")`。
  3. 验证返回的LLM实例使用的模型名称是否为自定义名称。

#### 测试用例 3：验证环境变量读取
- **目的**：测试函数能否从环境变量读取API密钥。
- **步骤**：
  1. 设置环境变量`WildCard_API_KEY`为一个测试值。
  2. 调用`get_llm(type='openai_wildcard')`。
  3. 验证返回的LLM实例的API密钥是否为环境变量的值。

#### 测试用例 4：验证特定类型的LLM实例化
- **目的**：测试每种类型的LLM是否能够被正确实例化。
- **步骤**：
  1. 对于每种`type`（如`openai_api`, `baidu`, `ollama`等），调用`get_llm(type=type)`。
  2. 验证返回的实例是否是相应类型的LLM类。

#### 测试用例 5：验证错误处理
- **目的**：测试在缺少必要参数时函数的行为。
- **步骤**：
  1. 尝试调用`get_llm(type='invalid-type')`。
  2. 验证是否抛出了异常或返回了错误信息。

#### 测试用例 6：验证温度和最大令牌数参数
- **目的**：测试温度和最大令牌数参数是否被正确应用。
- **步骤**：
  1. 定义非默认的温度和最大令牌数。
  2. 调用`get_llm(temperature=0.5, max_tokens=50)`。
  3. 验证返回的LLM实例的温度和最大令牌数是否与输入匹配。

#### 测试用例 7：验证API基础URL
- **目的**：测试自定义API基础URL是否被正确应用。
- **步骤**：
  1. 定义一个自定义API基础URL。
  2. 调用`get_llm(type='openai_wildcard', api_base=custom_base_url)`。
  3. 验证返回的LLM实例的API基础URL是否为自定义URL。

#### 测试用例 8：验证HuggingFace LLM的特殊参数
- **目的**：测试HuggingFace LLM的特定参数（如`system_prompt`）是否被正确应用。
- **步骤**：
  1. 定义自定义的`system_prompt`。
  2. 调用`get_llm(type='huggingface', system_prompt=custom_system_prompt)`。
  3. 验证返回的LLM实例的`system_prompt`是否与输入匹配。

这些测试用例提供了一个全面的测试计划，确保`get_llm`函数在各种情况下都能正常工作。在实际编写测试代码时，可以使用`unittest`框架和`unittest.mock`库来模拟外部依赖和环境变量。

"""

import os
import unittest
from unittest.mock import patch, MagicMock
from your_module import get_llm  # 假设上述函数保存在 your_module.py 文件中

class TestGetLLM(unittest.TestCase):

    def setUp(self):
        # 清除环境变量，防止测试受到外部环境变量的影响
        os.environ.pop('WildCard_API_KEY', None)
        os.environ.pop('bianxieai_API_KEY', None)

    def test_default_parameters(self):
        llm = get_llm()
        self.assertIsNotNone(llm)
        # 根据实际实现，验证模型名称是否为默认值
        self.assertEqual(llm.model, "gpt-3.5-turbo-0613")

    @patch('your_module.qet_openai')
    def test_custom_model_parameter(self, mock_qet_openai):
        llm = get_llm(model="custom-model-name")
        mock_qet_openai.assert_called_with(
            model="custom-model-name",
            temperature=0.1,
            max_tokens=None,
            **{}
        )

    @patch('your_module.os.environ.get')
    def test_environment_variable_reading(self, mock_get):
        mock_get.return_value = "test-api-key"
        llm = get_llm(type='openai_wildcard')
        mock_get.assert_called_with('WildCard_API_KEY')
        # 验证API密钥是否使用了环境变量的值
        self.assertEqual(llm.api_key, "test-api-key")

    @patch('your_module.qet_openai')
    def test_openai_api_llm_instantiation(self, mock_qet_openai):
        get_llm(type='openai_api')
        mock_qet_openai.assert_called()

    # 为其他类型的LLM实例化添加类似的测试用例

    @patch('your_module.qet_openai')
    def test_invalid_llm_type(self, mock_qet_openai):
        with self.assertRaises(Exception):
            get_llm(type='invalid-type')

    @patch('your_module.qet_openai')
    def test_temperature_and_max_tokens_parameter(self, mock_qet_openai):
        get_llm(temperature=0.5, max_tokens=50)
        mock_qet_openai.assert_called_with(
            model="gpt-3.5-turbo-0613",
            temperature=0.5,
            max_tokens=50,
            **{}
        )

    @patch('your_module.Anthropic')
    def test_claude_wildcard_llm_with_custom_base_url(self, mock_anthropic):
        custom_base_url = "https://custom-base-url.com"
        get_llm(type='claude_wildcard', api_base=custom_base_url)
        mock_anthropic.assert_called_with(
            base_url=custom_base_url,
            api_key=None,
            model="claude-3-sonnet-20240229",
            temperature=0.1,
            max_tokens=100000,
            **{}
        )

    # 为HuggingFace LLM的特殊参数添加测试用例

if __name__ == '__main__':
    unittest.main()

"""

针对`BaiduLLM`类，单元测试应该验证类属性、构造函数、元数据属性和完成方法的正确性。以下是编写测试的步骤和思路：

### 测试类：`BaiduLLM`类测试

#### 测试用例 1：验证类属性的默认值
- **目的**：确保所有类属性在初始化时具有正确的默认值。
- **步骤**：
  1. 创建`BaiduLLM`类的实例，不传递任何参数。
  2. 验证每个属性是否具有预期的默认值。

#### 测试用例 2：验证构造函数参数传递
- **目的**：确保构造函数能够接收自定义参数并正确设置实例属性。
- **步骤**：
  1. 定义一组自定义参数，包括API密钥、模型名称等。
  2. 创建`BaiduLLM`类的实例，传递自定义参数。
  3. 验证实例属性是否与传递的参数匹配。

#### 测试用例 3：验证元数据属性
- **目的**：确保`metadata`属性返回正确的元数据。
- **步骤**：
  1. 创建`BaiduLLM`类的实例。
  2. 获取`metadata`属性的值。
  3. 验证返回的元数据对象包含正确的属性值。

#### 测试用例 4：测试完成方法
- **目的**：确保`complete`方法能够调用API并返回正确的响应。
- **步骤**：
  1. 创建`BaiduLLM`类的实例。
  2. 定义一个测试提示（prompt）。
  3. 调用`complete`方法并传递测试提示。
  4. 验证返回的响应格式和内容是否正确。

#### 测试用例 5：测试流式完成方法
- **目的**：确保`stream_complete`方法能够生成流式的响应。
- **步骤**：
  1. 创建`BaiduLLM`类的实例。
  2. 定义一个测试提示。
  3. 调用`stream_complete`方法并传递测试提示。
  4. 验证生成的每个响应片段是否正确，并检查最终的响应是否完整。

#### 测试用例 6：测试异常处理
- **目的**：确保`BaiduLLM`能够处理并可能抛出API调用过程中的异常。
- **步骤**：
  1. 模拟API调用失败的情况。
  2. 调用`complete`或`stream_complete`方法。
  3. 验证是否捕获了异常，并检查异常信息。

#### 测试用例 7：测试API参数传递
- **目的**：确保`complete`和`stream_complete`方法能够传递正确的参数给API。
- **步骤**：
  1. 使用模拟对象替换API调用。
  2. 调用`complete`或`stream_complete`方法，传递自定义参数。
  3. 验证API调用是否使用了正确的参数。

#### 测试用例 8：测试温度、top_p、top_k参数的影响
- **目的**：验证这些参数是否影响生成的响应。
- **步骤**：
  1. 创建`BaiduLLM`实例，设置不同的温度、top_p、top_k值。
  2. 调用`complete`方法。
  3. 根据API文档，验证这些参数是否按预期改变了响应。

### 测试代码示例

```python
# 测试代码略，需要根据实际项目结构和测试框架进行编写
```

请注意，测试用例中提到的`Baidu_API`和`LLMMetadata`需要根据实际的类定义和模块导入进行调整。测试代码示例需要根据实际的测试框架和项目结构进行编写，这里仅提供了测试思路。在实际编写测试代码时，可以使用`unittest`框架和`unittest.mock`库来模拟外部依赖和API调用。

"""

import unittest
from unittest.mock import Mock, patch
from your_module import BaiduLLM  # 假设BaiduLLM类定义在your_module.py中

class TestBaiduLLM(unittest.TestCase):

    def setUp(self):
        # 模拟Baidu_API类，防止实际API调用
        self.baidu_api_mock = Mock()
        self.baidu_api_mock.chat.return_value = "Mocked chat response"
        self.baidu_api_mock.stream_chat.return_value = ['M', 'o', 'c', 'k', 'e', 'd']

        # 用mock替换Baidu_API构造函数
        patcher = patch('your_module.Baidu_API', return_value=self.baidu_api_mock)
        self.addCleanup(patcher.stop)
        patcher.start()

    def test_default_class_attributes(self):
        baidu_llm = BaiduLLM()
        self.assertEqual(baidu_llm.context_window, 3900)
        self.assertEqual(baidu_llm.num_output, 256)
        self.assertEqual(baidu_llm.model_name, 'mixtral_8x7b')
        # 其他默认属性的测试...

    def test_custom_parameters(self):
        baidu_llm = BaiduLLM(temperature=0.5, model_name='custom_model')
        self.assertEqual(baidu_llm.temperature, 0.5)
        self.assertEqual(baidu_llm.model_name, 'custom_model')

    def test_metadata_property(self):
        baidu_llm = BaiduLLM()
        metadata = baidu_llm.metadata
        self.assertEqual(metadata.context_window, 3900)
        self.assertEqual(metadata.num_output, 256)
        self.assertEqual(metadata.model_name, 'mixtral_8x7b')

    def test_complete_method(self):
        baidu_llm = BaiduLLM()
        response = baidu_llm.complete("Hello, Baidu LLM!")
        self.assertEqual(response.text, "Mocked chat response")

    def test_stream_complete_method(self):
        baidu_llm = BaiduLLM()
        completion_response_gen = baidu_llm.stream_complete("Hello, Baidu LLM!")
        response_list = [cr.text for cr in completion_response_gen]
        self.assertEqual(''.join(response_list), "Mocked chat response")

    def test_api_parameters_passing(self):
        baidu_llm = BaiduLLM()
        prompt = "Test prompt"
        response = baidu_llm.complete(prompt)
        # 验证API是否接收到了正确的参数
        self.baidu_api_mock.chat.assert_called_with(
            prompt,
            [],
            model_name=baidu_llm.model_name,
            temperature=baidu_llm.temperature,
            top_p=baidu_llm.top_p,
            top_k=baidu_llm.top_k,
            penalty_score=baidu_llm.penalty_score,
            stop=baidu_llm.stop
        )

    # 其他测试用例...

if __name__ == '__main__':
    unittest.main()















class EngineBaiduTests(unittest.TestCase):
    def test_access_token(self):
        pass
        # Baidu_API().my_access_token

    def test_chat(self):
        result = baidu_chat('你好')
        self.assertIsInstance(result,str)
        self.assertLess(3,4)

    def test_history(self):
        result = baidu_chat('a+b=?', history=[['a=?', '3'], ['b=?', '4']])
        self.assertIn('7',result)
        self.assertIsInstance(result, str)
        self.assertLess(3, 4)

    def test_stream(self):
        for i in baidu_chat('你好', stream=True):
            print(i)

    def test_model(self):
        model_name = 'llama3-8b',
        result = baidu_chat('你好', model_name='llama3:70b')
        result = baidu_chat('你好', model_name='baidu1')
        result = baidu_chat('你好', model_name='mixtral_8x7b')

    def test_temperature(self):
        """
        待测
        temperature=0.95,
        top_p=0.8,
        top_k=50,
        penalty_score=1.0,
        stop=[],
        user_id=None,
        """

class EngineOllamaTests(unittest.TestCase):
    def test_ollama_list(self):
        result = ollama_list(host='http://192.168.8.125:11435')
        self.assertIsInstance(result,dict)
        print(result)

    def test_chat(self):
        result = ollama_chat('你好',model_name = 'llama3',ip_host='http://192.168.8.125:11435')
        self.assertIsInstance(result,str)
        self.assertLess(3,4)

    def test_stream(self):
        result = ollama_chat('你好', model_name='llama3',stream=True, ip_host='http://192.168.8.125:11435')
        for i in result:
            print(i)

    def test_model(self):
        result = ollama_chat('你好', model_name='llama3', ip_host='http://192.168.8.125:11435')
        # result = ollama_chat('你好', model_name='llama3:70b', ip_host='http://192.168.8.125:11435')

class EngineTritonTests(unittest.TestCase):
    def test_chat(self):
        result = triton_chat('你好', model_name='llama3-8b',ip_host='192.168.8.126:8001', stop='<|eot_id|>')
        print(result)
        self.assertIsInstance(result,str)
        self.assertLess(3,4)

    def test_history(self):
        result = triton_chat('a+b=?', history=[['a=?', '3'], ['b=?', '4']],ip_host='192.168.8.126:8001',stop='<|eot_id|>')
        self.assertIn('7',result)
        self.assertIsInstance(result, str)
        self.assertLess(3, 4)

    def test_stream(self):
        for i in triton_chat('你好', model_name='llama3-8b', stop='<|eot_id|>',ip_host='192.168.8.126:8001', stream=True):
            print(i)

    def test_output_type(self):
        for i in triton_chat('你好', model_name='llama3-8b',
                             stop='<|eot_id|>',
                                output_type ='sentence',
                                ip_host='192.168.8.126:8001', stream=True):
            print(i)



    def test_model(self):
        pass

    def test_temperature(self):
        """
        test_1_load.py
        temperature=0.95,
         top_p=0.95,
         max_tokens=200,
         user_id="1084",
        verbose=False,
         **sampling_parameters_kwargs,
        :return:
        """
        pass

from .llms import get_llm
class GetLlmTests(unittest.TestCase):
    def test_model(self):
        llm = get_llm()



# 运行所有测试
if __name__ == '__main__':
    unittest.main()