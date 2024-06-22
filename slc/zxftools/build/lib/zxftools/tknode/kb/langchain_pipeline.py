from langchain import hub
from langchain.memory.chat_memory import BaseChatMemory, BaseMemory
from langchain.memory import CombinedMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationEntityMemory #实体记忆
from langchain.memory import ConversationKGMemory
from langchain.memory import ConversationSummaryMemory, ChatMessageHistory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, ZeroShotAgent
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_community.llms.human import HumanInputLLM
from langchain.callbacks import HumanApprovalCallbackHandler
from langchain.llms import BaseLLM,OpenAI
from langchain import LLMChain, PromptTemplate
from langchain.prompts import PromptTemplate

from enum import Enum
# 这里怎么做 融进去

def llms():
    llm = HumanInputLLM(
        prompt_func=lambda prompt: print(
            f"\n===PROMPT====\n{prompt}\n=====END OF PROMPT======"
        )
    )
    # from langchain import tools
# class_level SearchInput(BaseModel):
#     query: str = Field(description="should be a search query")
#
#
# @tool("search-tool", args_schema=SearchInput, return_direct=True)
# def search(query: str) -> str:
#     """Look up things online."""
#     return "LangChain"


class MemoryType(Enum):
    BUFFER = 'Buffer'
    ENTITY = 'Entity'
    KG = 'KG'
    SUMMARY = 'Summary'
    SUMMARY_BUFFER = 'SummaryBuffer'


class MemoryFactory():
    """
    :param type:
            'Buffer' or 'Entity' or 'KG' or 'Summary' or 'SummaryBuffer'
            'Entity': memory.entity_store.store 通过此命令查看 主体识别记忆结构

            'KG':   # 获取实体
                    memory.get_current_entities("what's Sams favorite color?")
                    # 获取三元组
                    memory.get_knowledge_triplets("her favorite color is red")
            'Summary':
    :param window True
    :param llm    None
    :param limit  None
    return_messages=False,
    memory.load_memory_variables({})

    """

    def __new__(self, type=MemoryType.BUFFER, window=False, return_messages=False, memory_key='chat_history', llm=None,
                limit=None, n=5, **kwargs):

        if type == MemoryType.BUFFER:  # 优
            if window:
                assert n
                memory = ConversationBufferWindowMemory(memory_key=memory_key, return_messages=return_messages, k=n,
                                                        **kwargs)
            else:
                memory = ConversationBufferMemory(memory_key=memory_key, return_messages=return_messages, **kwargs)
        elif type == MemoryType.ENTITY:  # 优
            llm = llm or OpenAI()
            memory = ConversationEntityMemory(chat_history_key=memory_key, llm=llm, return_messages=return_messages,
                                              **kwargs)

        elif type == MemoryType.KG:  # 优
            llm = llm or OpenAI()
            memory = ConversationKGMemory(memory_key=memory_key, llm=llm, return_messages=return_messages, **kwargs)
        elif type == MemoryType.SUMMARY:  # 差
            llm = llm or OpenAI()
            memory = ConversationSummaryMemory(memory_key=memory_key, llm=llm, return_messages=return_messages,
                                               **kwargs)
        elif type == MemoryType.SUMMARY_BUFFER:  # 中
            llm = llm or OpenAI()
            assert n
            memory = ConversationSummaryBufferMemory(memory_key=memory_key, llm=llm, return_messages=return_messages,
                                                     max_token_limit=n, **kwargs)
        else:
            memory = None
            # ConversationTokenBufferMemory
        return memory

    @staticmethod
    def load_memory(memory: BaseChatMemory):
        memory.load_memory_variables({})

    @staticmethod
    def comb(*Memory_list):
        Memorylist = list(Memory_list)
        memory = CombinedMemory(memories=Memorylist)
        return memory



class AgentFactory(AgentExecutor):

    @classmethod
    def for_openai_functions_agent(cls, tools,llm,verbose=False):
        prompt = hub.pull("hwchase17/openai-functions-agent")
        agent = create_openai_functions_agent(llm, tools, prompt)
        return cls(agent=agent, tools=tools, verbose=verbose)

    @classmethod
    def from_memory(cls, tools: list, llm=ChatOpenAI(), memory=None, verbose=True):
        prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
        suffix = """Begin!"
        {chat_history}
        Question: {input}
        {agent_scratchpad}"""
        prompt = ZeroShotAgent.create_prompt(
            tools,
            prefix=prefix,
            suffix=suffix,
            input_variables=["input", "chat_history", "agent_scratchpad"],
        )
        agent = ZeroShotAgent(llm_chain=LLMChain(llm=llm, prompt=prompt),
                              tools=tools, verbose=verbose)

        return cls(agent=agent, tools=tools, verbose=verbose, memory=memory)

    @classmethod
    def from_llm(cls, tools: list, llm=ChatOpenAI(), memory=None, verbose=True,
                 callbacks=None,
                 ):
        """
        callbacks = [HumanApprovalCallbackHandler(should_check=_should_check, approve=_approve)]
        parser = parser or StrOutputParser()
        """

        def _should_check(serialized_obj: dict) -> bool:
            # Only require approval on ShellTool.
            return serialized_obj.get("name") == "terminal"

        def _approve(_input: str) -> bool:
            if _input == "echo 'Hello World'":
                return True
            msg = (
                "Do you approve of the following input? "
                "Anything except 'Y'/'Yes' (case-insensitive) will be treated as a no."
            )
            msg += "\n\n" + _input + "\n"
            resp = input(msg)
            return resp.lower() in ("yes", "y")

        callbacks = [HumanApprovalCallbackHandler(should_check=_should_check, approve=_approve)]

        agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=verbose,
            callbacks=callbacks,
            memory=memory,
        )
        return cls(agent=agent, tools=tools, verbose=verbose, memory=memory)

    @classmethod
    def run(cls, executor):
        executor.invoke({"input": "12*6-6*12+76=?"})

# for step in agent_executor.iter({"input": question}):
#     if output := step.get("intermediate_step"):


class ChainFactory(LLMChain):
    # prompt = prompt if not partial else prompt.partial(**partial)
    # check_memorys(memory,prompt)
    # parser = parser or StrOutputParser()

    @classmethod
    def from_memory(cls, llm: BaseLLM = ChatOpenAI(), memory=None, verbose: bool = True, **kwargs) -> LLMChain:
        template = """
        你是一个python程序员.我们可以讨论很多关于代码和程序的问题,你也擅长编写代码.
        {chat_history}
        Human: {input}
        Chatbot:
        """
        input_variables = ["input", "chat_history", ]
        prompt = PromptTemplate(
            template=template,
            input_variables=input_variables
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose, memory=memory, **kwargs)

