from llama_index.core.agent.react.output_parser import *
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import AgentRunner, ReActAgentWorker, ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.llms import MessageRole
from llama_index.core.llms import ChatMessage
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
        agents = {'react':ReActAgent,'openai':OpenAIAgent}
        output_parser = output_parser or SuperReActOutputParser()
        agent_obj = agents.get(type)
        if agent_obj:
            agent = agent_obj.from_tools(self.tools, llm=self.llm, verbose=self.verbose,
                                          max_iterations=self.max_iterations,output_parser=output_parser,
                                          chat_history=[ChatMessage(role=MessageRole.SYSTEM, content=system_content)])

            return agent
        else:
            return 'type 不存在'
