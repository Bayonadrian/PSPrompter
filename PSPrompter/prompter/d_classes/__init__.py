from pydantic import BaseModel, field_validator
from pydantic_core import PydanticCustomError

class Variables(BaseModel):

    name: str
    value: str

class Prompt(BaseModel):

    prompt_path: str
    prompt_vars: list[Variables]

    @field_validator("prompt_vars")
    def no_duplicated_vars(cls, var:list[Variables]):

        names= [_.name for _ in var]
        dedup_names= set(names)

        if len(names) != len(dedup_names):

            [names.remove(_) for _ in dedup_names]

            raise PydanticCustomError("duplicates on list", 
                                      "Make sure there are no duplicated variables {names}",
                                      {"names": names})

        return var