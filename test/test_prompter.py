import pytest
from PSPrompter import PromptCollector, Prompt, Variables

def test_prompter():

    var= "VERY IMPORTANT INFORMATION"

    text= Variables(name= "text",
                    value= var)
    
    prompt= Prompt(prompt_path= './prompts/long_summary.md',
              prompt_vars= [text])
    
    all_prompt= PromptCollector(prompt= prompt).full_prompt()

    assert var in all_prompt, f"Could not find find {var} into the prompt"
    

