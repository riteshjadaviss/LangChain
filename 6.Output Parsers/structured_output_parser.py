import langchain
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser ,ResponseSchema
load_dotenv()

chat = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)
response_schemas = [
    ResponseSchema(name="description", description="Description of the cuisine"),
    ResponseSchema(
        name="ingredients",
        description="Ingredients of the cuisine",
        type="List[string]",
    ),
    ResponseSchema(name="cooking_method", description="Cooking method of the cuisine")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template1=PromptTemplate(
    input_variables=["cuisine"],
    template="Describe the cuisine:{cuisine} \n {format_template}",
    partial_variables={"format_template": parser.get_format_instructions()}
)

chain=template1|chat|parser
result = chain.invoke({"cuisine": "Italian"})
print(result)