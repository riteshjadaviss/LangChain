import langchain
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("who is the best footballer of all time")
print(result.text)
