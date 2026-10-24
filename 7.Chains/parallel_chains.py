import langchain
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model1 = ChatOpenAI(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
)

model2 = ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

template1=PromptTemplate(
    input_variables=["topic1"],
    template="Write a detailed explanation about the topic: {topic1}"
)

template2=PromptTemplate(
    input_variables=["topic2"],
    template="Write a quiz about the topic: {topic2}"
)

template3=PromptTemplate(
    input_variables=["explaination", "quiz"],
    template="Merge the given topic and quiz together: topic:{explaination} quiz:{quiz}"
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
    "explaination":template1 | model1 | parser,
    "quiz":template2 | model2 |parser
})

merged_chain = template3 | model1 | parser

chain=parallel_chain | merged_chain
result =chain.invoke({"topic1": "Artificial Intelligence", "topic2": "System Design"})
print(result)
chain.get_graph().print_ascii()
