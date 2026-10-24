import langchain
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
load_dotenv()

chat = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)
class Cuisine(BaseModel):
    description: str = Field(..., description="Description of the cuisine")
    ingredients: list[str] = Field(..., description="Ingredients of the cuisine")
    cooking_method: str = Field(..., description="Cooking method of the cuisine")
    rating: float = Field(default=2.5, gt=0, lt=5, description="Rating of the cuisine")

parser = PydanticOutputParser(pydantic_object=Cuisine)

template1=PromptTemplate(
    input_variables=["cuisine"],
    template="Describe the cuisine:{cuisine} \n {format_template}",
    partial_variables={"format_template": parser.get_format_instructions()}
)

chain=template1|chat|parser
result = chain.invoke({"cuisine": "Italian"})
print(result)