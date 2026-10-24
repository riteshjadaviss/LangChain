import langchain
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

chat = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)

template1=PromptTemplate(
    input_variables=["cuisine"],
    template="Describe the cuisine: {cuisine}"
)
template2 = PromptTemplate(
    input_variables=["cuisine"],
    template="summarize the topic in 2 lines: {cuisine}"
)
parser=StrOutputParser()

chain=template1 | chat | parser |template2 |chat |parser

result =chain.invoke({"cuisine": "Italian"})
print(result)