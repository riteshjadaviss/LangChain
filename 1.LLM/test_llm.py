import langchain
import dotenv
import os
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
    temperature=1,
    max_completion_tokens=10
)

result = llm.invoke("tell me a fat joke")
print(result.text)
