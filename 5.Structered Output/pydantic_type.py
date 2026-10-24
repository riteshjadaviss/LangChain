import langchain
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
load_dotenv()
import typing
from typing import TypedDict ,Annotated ,Optional
from pydantic import BaseModel ,Field
from langchain_openai import ChatOpenAI
chat = ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

class Cuise(BaseModel):
    name: str = Field(..., description="Name of the cuisine")
    country: str = Field(..., description="Country of origin")
    specialty: str = Field(..., description="Specialty dish of the cuisine")
    ingredients: Optional[list[str]] = Field(None, description="List of main ingredients")

structured_output = chat.with_structured_output(Cuise)
result=structured_output.invoke("Italian cuisine is famous for its simple, fresh ingredients and rich flavors. Popular dishes include pizza, pasta, risotto, and tiramisu. Olive oil, tomatoes, cheese, and herbs like basil are commonly used. Each region of Italy has its own unique cooking style and specialties")
print(result)
