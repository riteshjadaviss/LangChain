import langchain
import os
from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)
prompt_template = ChatPromptTemplate([
    SystemMessage(content="You are a \"{expertise}\" expert and answer users question in 1-2 sentences max"),
    MessagesPlaceholder(variable_name="history"),
    ('human', "{user_input}")
])

history=[]


while True:
    user_input = input("You: ")
    if(user_input.lower() in ["exit", "quit"]):
        break
    response = chat.invoke(prompt_template.invoke({"history": history, "user_input": user_input, "expertise": "cuisine"}))
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response.content))
    print("Bot:", response.content)

print(history)