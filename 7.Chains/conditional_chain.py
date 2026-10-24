import langchain
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel ,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
load_dotenv()


model = ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the text")

parser = PydanticOutputParser(pydantic_object=Sentiment)
parser2 = StrOutputParser()


prompt = PromptTemplate(
    input_variables=["feedback"],
    template="Determine the sentiment of the following text: {feedback} \n {format_instruction}",
    partial_variables={"format_instruction": parser.get_format_instructions()}
)


classifer_chain = prompt | model | parser

prompt2 = PromptTemplate(input_variables=["sentiment"], template="product feedback is {sentiment} provide response to user")
prompt3 = PromptTemplate(input_variables=["sentiment"], template="product feedback is {sentiment} provide response to user")

conditional_chain = RunnableBranch(
    (
        lambda inputs: inputs.sentiment == "positive", prompt3 | model | parser2,
    ),
    (
        lambda inputs: inputs.sentiment == "negative",prompt2 | model | parser2,
    ),
    RunnableLambda(lambda x:"colud not find sentiments")
)

chain = classifer_chain | conditional_chain

result = chain.invoke({"feedback":"This is an awesome phone"})
print(result)
