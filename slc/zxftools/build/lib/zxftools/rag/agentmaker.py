from llama_index.core.agent.react.output_parser import *
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import AgentRunner, ReActAgentWorker, ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.agent.react.output_parser import ReActOutputParser
import re

class SuperReActOutputParser(ReActOutputParser):
    def parse(self, output: str, is_streaming: bool = False) -> BaseReasoningStep:
        """Parse output from ReAct agent.

        We expect the output to be in one of the following formats:
        1. If the agent need to use a tool to answer the question:
            ```
            Thought: <thought>
            Action: <action>
            Action Input: <action_input>
            ```
        2. If the agent can answer the question without any tools:
            ```
            Thought: <thought>
            Answer: <answer>
            ```
        """
        if "Thought:" not in output:
            # NOTE: handle the case where the agent directly outputs the answer
            # instead of following the thought-answer format

            return ResponseReasoningStep(
                thought="(Implicit) I can answer without any more tools!",
                response=output,
                is_streaming=is_streaming,
            )

        if "Answer:" in output:
            thought, answer = extract_final_response(output)
            return ResponseReasoningStep(
                thought=thought, response=answer, is_streaming=is_streaming
            )

        if "Action:" in output:


            if "Action: None" in output or 'Action: No tool' in output:
                def get_Thought(text):
                    thought_pattern = r"Thought: (.*)"
                    thought_match = re.search(thought_pattern, text)
                    if thought_match:
                        thought_content = thought_match.group(1)
                        return thought_content
                    else:
                        return None

                return get_Thought(output)

            return parse_action_reasoning_step(output)

        if "Thought:" in output and "Answer:" not in output:

            thought_content = re.findall(r'Thought: (.+)', output)[0]
            llm = OpenAI(
                model='gpt-3.5-turbo-0613',
                api_base="https://api.gptsapi.net/v1",
                api_key="sk-oKa1dff374b671b4e4a84e9760156485b820e40c9f8sgD1B", )

            output_prompt = f"""
            Thought: {thought_content}
            Answer:
            """

            output_answer = llm.complete(output_prompt).text
            output_1 = f"""
            Thought: {thought_content}
            Answer: {output_answer}
            """
            thought, answer = extract_final_response(output_1)
            return ResponseReasoningStep(
                thought=thought, response=answer, is_streaming=is_streaming
            )

        raise ValueError(f"v1 Could not parse output: {output}")

class ReactAgentMaker:
    # engine = reactagent

    help = lambda :print("""

for example:
    maker = ReactAgentMaker(model_name='gpt-4-turbo-preview')
    maker.add_tools(tools)
    agent = maker.create_agent(output_parser=MyReActOutputParser())
    """)

    def __init__(self, llm=None, max_iterations=50, verbose=True):
        self.llm = llm or OpenAI(
                        model='gpt-3.5-turbo-0613',
                        api_base="https://api.gptsapi.net/v1",
                        api_key="sk-oKa1dff374b671b4e4a84e9760156485b820e40c9f8sgD1B",)
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.tools = []

    def clean_tools(self):
        self.tools = []

    def add_tool(self, function,from_type='default'):
        if from_type == 'default':
            tool = FunctionTool.from_defaults(fn=function)
            self.tools.append(tool)

    def add_tools(self, functions):
        for func in functions:
            self.add_tool(func)

    def add_tools_origin(self,origin_Spec):
        self.tools += origin_Spec.to_tool_list()

    def add_tool_class(self,class_object,**obj_kwargs):
        instance = class_object(**obj_kwargs)
        [self.add_tool(getattr(instance, registered_func)) for registered_func in instance.register]
        return "success"

    def create_agent(self, type='react',system_content='',output_parser=None):
        """
        tool_choice='useless_tool'
        tool_choice="none"
        tool_choice="auto"
        只对openai的模式有效果

        :param type:
        :param system_content:
        :param output_parser:
        :return:
        """
        agents = {'react':ReActAgent,'openai':OpenAIAgent}
        output_parser = output_parser or SuperReActOutputParser()
        agent_obj = agents.get(type)
        if agent_obj:
            # agent = agent_obj.from_tools(self.tools, llm=self.llm, verbose=self.verbose,
            #                               max_iterations=self.max_iterations,output_parser=output_parser,
            #                               chat_history=[ChatMessage(role=MessageRole.SYSTEM, content=system_content)])
            agent = agent_obj.from_tools(self.tools, llm=self.llm, verbose=self.verbose,
                                          max_iterations=self.max_iterations,output_parser=output_parser,
                                          system_prompt=system_content,
                                         # tool_retriever=obj_index.as_retriever(similarity_top_k=2),
                                         )

            ## 多工具的连续使用

            return agent
        else:
            return 'type 不存在'

    def create_assistant(self):
        from llama_index.agent.openai import OpenAIAssistantAgent
        from llama_index.core.agent import ReActAgent
        from llama_index.llms.openai import OpenAI
        agent = OpenAIAssistantAgent.from_new(
            name="SEC Analyst",
            instructions="You are a QA assistant designed to analyze sec filings.",
            openai_tools=[{"type": "retrieval"}],
            instructions_prefix="Please address the user as Jerry.",
            files=["data/10k/lyft_2021.pdf"],
            verbose=True,
            # tools=[summary_tool, vector_tool],
            # run_retrieve_sleep_time=1.0,

        )

"""
class YourOpenAIAgent:
    def __init__(
        self,
        tools: Sequence[BaseTool] = [],
        llm: OpenAI = OpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        chat_history: List[ChatMessage] = [],
    ) -> None:
        self._llm = llm
        self._tools = {tool.metadata.name: tool for tool in tools}
        self._chat_history = chat_history

    def reset(self) -> None:
        self._chat_history = []

    def chat(self, message: str) -> str:
        chat_history = self._chat_history
        chat_history.append(ChatMessage(role="user", content=message))
        tools = [
            tool.metadata.to_openai_tool() for _, tool in self._tools.items()
        ]

        ai_message = self._llm.chat(chat_history, tools=tools).message
        additional_kwargs = ai_message.additional_kwargs
        chat_history.append(ai_message)

        tool_calls = additional_kwargs.get("tool_calls", None)
        # parallel function calling is now supported
        if tool_calls is not None:
            for tool_call in tool_calls:
                function_message = self._call_function(tool_call)
                chat_history.append(function_message)
                ai_message = self._llm.chat(chat_history).message
                chat_history.append(ai_message)

        return ai_message.content

    def _call_function(
        self, tool_call: ChatCompletionMessageToolCall
    ) -> ChatMessage:
        id_ = tool_call.id
        function_call = tool_call.function
        tool = self._tools[function_call.name]
        output = tool(**json.loads(function_call.arguments))
        return ChatMessage(
            name=function_call.name,
            content=str(output),
            role="tool",
            additional_kwargs={
                "tool_call_id": id_,
                "name": function_call.name,
            },
        )

"""


"""

# start task
task = agent.create_task("What is (121 * 3) + 42?")


step_output = agent.run_step(task.task_id)

step_output = agent.run_step(task.task_id)

print(step_output.is_last)


 # now that the step execution is done, we can finalize response
response = agent.finalize_response(task.task_id)
print(str(response))

"""

"""

 from llama_index.core.tools import QueryEngineTool, ToolMetadata

individual_query_engine_tools = [
    QueryEngineTool(
        query_engine=index_set[year].as_query_engine(),
        metadata=ToolMetadata(
            name=f"vector_index_{year}",
            description=(
                "useful for when you want to answer queries about the"
                f" {year} SEC 10-K for Uber"
            ),
        ),
    )
    for year in years
]



"""

'''
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata

llm = OpenAI(model="gpt-4o", temperature=0)
vectara_tool = QueryEngineTool(
    query_engine=index.as_query_engine(
        summary_enabled=True,
        summary_num_results=5,
        summary_response_lang="en",
        summary_prompt_name="vectara-summary-ext-24-05-large",
        reranker="mmr",
        rerank_k=50,
        mmr_diversity_bias=0.2,
    ),
    metadata=ToolMetadata(
        name="Vectara",
        description="Vectara Query Engine that is able to answer Questions about AI regulation.",
    ),
)
agent = ReActAgent.from_tools(
    tools=[vectara_tool],
    llm=llm,
    context="""
        You are a helpful chatbot that answers any user questions around AI regulations using the Vectara tool.
        You break down complex questions into simpler ones.
        You use the Vectara query engine to help provide answers to simpler questions.
    """,
    verbose=True,
)

'''