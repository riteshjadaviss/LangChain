import langchain
import os
import json
from dotenv import load_dotenv
load_dotenv()   
from langchain_core.prompts import load_prompt


from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)  


template = load_prompt("summary_template.json")

user_input = {
    "paper_input": "Attention is all you need",
    "style_input": "Concise",
    "length_input": "Short"
}

chain=template | model

result=chain.invoke(user_input)
print(result.content)
