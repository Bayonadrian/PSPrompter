from .d_classes import Prompt
import re

class PromptCollector:

    def __init__(self, prompt: Prompt):
        
        self.prompt= prompt

    @property
    def __get_prompt(self) -> str:

        with open(self.prompt.prompt_path, 'r', encoding= 'utf-8') as r:

            return r.read()
        
    def full_prompt(self):

        prompt= self.__get_prompt   

        for _ in self.prompt.prompt_vars:

            prompt = re.sub(rf'{{{{{_.name}}}}}', _.value, prompt, count= 0)

        return prompt

            

            
 