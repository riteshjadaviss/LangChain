import langchain
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_docling import DoclingLoader
load_dotenv()

model1=ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

template = PromptTemplate(
    input_variables=["content"],
    template="Summarize the following content: {content}"
)
parser=StrOutputParser()
loader = DoclingLoader("8.Document loader\\System Design Interview An Insider’s Guide by Alex Xu.pdf")
documents=loader.load()

chain=template | model1 | parser
#result=chain.invoke({"content": ' '.join([doc.page_content for doc in documents])})
print(documents[0].metadata)

