
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
from unittest.mock import patch, MagicMock,Mock
from zxftools.llms import get_llm
import zxftools

class TestGetLLM(unittest.TestCase):
    def setUp(self):
        print(1234)


    def test_openai_api(self):
        pass

    @patch("zxftools.llms.llms.qet_openai")
    def test_wildcard(self,qet_openai):
        qet_openai.return_value = '1'
        llm = get_llm(type='openai_wildcard')
        print('llm',llm,'llm')
        # qet_openai.assert_called()


    def test_default_parameters(self):
        llm = get_llm()
        self.assertIsNotNone(llm)
        # 根据实际实现，验证模型名称是否为默认值
        self.assertEqual(llm.model, "gpt-3.5-turbo-0613")


    @patch('zxftools.llms.llms.qet_openai')
    def test_custom_model_parameter(self, mock_qet_openai):
        llm = get_llm(model="custom-model-name")
        mock_qet_openai.assert_called_with(
            model="custom-model-name",
            temperature=0.1,
            max_tokens=None,
            **{}
        )

    @patch('zxftools.llms.llms.os.environ.get')
    def test_environment_variable_reading(self, mock_get):
        mock_get.return_value = "test-api-key"
        llm = get_llm(type='openai_wildcard')
        # 检查输入是否为 WildCard_API_KEY
        mock_get.assert_called_with('WildCard_API_KEY')
        # 验证API密钥是否使用了环境变量的值
        self.assertEqual(llm.api_key, "test-api-key")

    @patch('zxftools.llms.llms.qet_openai')
    def test_openai_api_llm_instantiation(self, mock_qet_openai):
        get_llm(type='openai_api')
        # 至少被调用过一次
        mock_qet_openai.assert_called()

    # 为其他类型的LLM实例化添加类似的测试用例

if __name__ == '__main__':
    unittest.main()
