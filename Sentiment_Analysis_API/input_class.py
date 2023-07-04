from pydantic import BaseModel

#class that includes the input and its type
class input_class(BaseModel):
    text : str