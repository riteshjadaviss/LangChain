import langchain
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
load_dotenv()
import typing
from typing import TypedDict ,Annotated ,Optional
from langchain_openai import ChatOpenAI
chat = ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

class Cuise(TypedDict):
    name: Annotated[str, "Name of the cuisine"]
    country: Annotated[str, "Country of origin"]
    specialty: Annotated[str, "Specialty dish of the cuisine"]
    ingredients: Annotated[Optional[list[str]], "List of main ingredients"]

structured_output = chat.with_structured_output(Cuise)
result=structured_output.invoke("Italian cuisine is famous for its simple, fresh ingredients and rich flavors. Popular dishes include pizza, pasta, risotto, and tiramisu. Olive oil, tomatoes, cheese, and herbs like basil are commonly used. Each region of Italy has its own unique cooking style and specialties")
print(result)
