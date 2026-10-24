import os
from dotenv import load_dotenv
load_dotenv()
import langchain
from langchain_anthropic import ChatAnthropic

claude = ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

result = claude.invoke("who is the best footballer of all time")
print(result.text)