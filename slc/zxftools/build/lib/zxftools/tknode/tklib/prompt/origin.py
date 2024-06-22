from llama_index.core.prompts.system import MARKETING_WRITING_ASSISTANT
from llama_index.core.prompts.system import IRS_TAX_CHATBOT
from llama_index.core.prompts.system import SHAKESPEARE_WRITING_ASSISTANT
from llama_index.core.prompts.chat_prompts import CHAT_REFINE_PROMPT
from llama_index.core.prompts.default_prompts import DEFAULT_REFINE_PROMPT

from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate

from llama_index.core import PromptTemplate
from enum import Enum

class PromptType(Enum):
    text_qa_template_str = (
        "Context information is"
        " below.\n---------------------\n{context_str}\n---------------------\nUsing"
        " both the context information and also using your own knowledge, answer"
        " the question: {query_str}\nIf the context isn't helpful, you can also"
        " answer the question on your own.\n"
    )
    refine_template_str = (
        "The original question is as follows: {query_str}\nWe have provided an"
        " existing answer: {existing_answer}\nWe have the opportunity to refine"
        " the existing answer (only if needed) with some more context"
        " below.\n------------\n{context_msg}\n------------\nUsing both the new"
        " context and your own knowledge, update or repeat the existing answer.\n"
    )
    #####
    qa_prompt_str = (
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "answer the question: {query_str}\n"
    )

    refine_prompt_str = (
        "We have the opportunity to refine the original answer "
        "(only if needed) with some more context below.\n"
        "------------\n"
        "{context_msg}\n"
        "------------\n"
        "Given the new context, refine the original answer to better "
        "answer the question: {query_str}. "
        "If the context isn't useful, output the original answer again.\n"
        "Original Answer: {existing_answer}"
    )

    react_system_header_str = """\

    You are designed to help with a variety of tasks, from answering questions \
        to providing summaries to other types of analyses.

    ## Tools
    You have access to a wide variety of tools. You are responsible for using
    the tools in any sequence you deem appropriate to complete the task at hand.
    This may require breaking the task into subtasks and using different tools
    to complete each subtask.

    You have access to the following tools:
    {tool_desc}

    ## Output Format
    To answer the question, please use the following format.

    ```
    Thought: I need to use a tool to help me answer the question.
    Action: tool name (one of {tool_names}) if using a tool.
    Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num_beams": 5}})
    ```

    Please ALWAYS start with a Thought.

    Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num_beams': 5}}.

    If this format is used, the user will respond in the following format:

    ```
    Observation: tool response
    ```

    You should keep repeating the above format until you have enough information
    to answer the question without using any more tools. At that point, you MUST respond
    in the one of the following two formats:

    ```
    Thought: I can answer without using any more tools.
    Answer: [your answer here]
    ```

    ```
    Thought: I cannot answer the question with the provided tools.
    Answer: Sorry, I cannot answer your query.
    ```

    ## Additional Rules
    - The answer MUST contain a sequence of bullet points that explain how you arrived at the answer. This can include aspects of the previous conversation history.
    - You MUST obey the function signature of each tool. Do NOT pass in no arguments if the function expects arguments.

    ## Current Conversation
    Below is the current conversation consisting of interleaving human and assistant messages.

    """

    GPT_BUILDER_SYS_STR = """\
    You are helping to construct an agent given a user-specified task. You should generally use the tools in this order to build the agent.

    1) Create system prompt tool: to create the system prompt for the agent.
    2) Get tools tool: to fetch the candidate set of tools to use.
    3) Create agent tool: to create the final agent.
    """


class PromptFactory:
    def __new__(cls, prompt_type:PromptType,types, **kwargs):
        if types == 'prompttemplate':
            print(prompt_type.name)
            return PromptTemplate(prompt_type.value)
        else:
            print(prompt_type.name)
            msgs = [
                ChatMessage(
                    role=MessageRole.SYSTEM,
                    content="Always answer the question, even if the context isn't helpful.",
                ),
                ChatMessage(role=MessageRole.USER, content=prompt_type.value),
            ]
            return ChatPromptTemplate(msgs)


