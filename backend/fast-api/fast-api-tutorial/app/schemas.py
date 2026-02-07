'''
inside of here we're going to define the type of data that we want to accept in our various endpoints.
'''

from pydantic import BaseModel


class PostCreate(BaseModel):
    title:str
    content: str
    
class PostResponse(BaseModel):
    title:str
    content: str
    