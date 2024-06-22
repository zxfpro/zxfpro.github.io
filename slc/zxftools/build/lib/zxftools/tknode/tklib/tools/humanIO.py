import os
import time
from .base import BaseTools

class HumanIOTools(BaseTools):
    register_default = ['human_reviewer', 'demand_confirmation', 'question_rewriter']
    def __init__(self, llm, register=[]):

        super().__init__(register,self.register_default)
        self.llm = llm

    def human_reviewer(text: str) -> str:
        """
        Use it before the final submission to verify if your work meets the requirements.
        """
        print('***********check************')
        result = input(text)
        if result == 'q':
            raise Exception('终止任务')
        return result

    def demand_confirmation(self,question: str) -> str:
        """
        If you feel that the requirements are unclear, you can use the tool to ask the user questions to clarify the requirements
        """
        result = input(question)
        return result

    def question_rewriter(self, question: str) -> str:
        """
        If the user's question is not clear enough, you can use this tool to get a clearer question description.
        """
        background = """

        """
        result = self.llm.complete(f"""
        Please provide a more specific and complete description of the user's question based on the background:
        {background}
        -------------------
        and the question asked by the user:
        {question}

        -------------------
        Make the user's problem more specific and complete
        """)
        return result.text
