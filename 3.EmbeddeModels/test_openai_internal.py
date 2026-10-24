import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai  import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
    tiktoken_enabled=False,
    check_embedding_ctx_length=False,
)

result= embeddings.embed_query("Hello world")
print(result)
