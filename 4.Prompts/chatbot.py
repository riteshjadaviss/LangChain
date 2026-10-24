import langchain
import os
from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.messages import ChatPromptTemplete
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)

history=[SystemMessage(content="You are a sports expert and answer users question in 1-2 sentences max")]


while True:
    user_input = input("You: ")
    if(user_input.lower() in ["exit", "quit"]):
        break
    history.append(HumanMessage(content=user_input))
    response = chat.invoke(history)
    history.append(AIMessage(content=response.content))
    print("Bot:", response.content)

print(history)