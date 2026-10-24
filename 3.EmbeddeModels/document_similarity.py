import langchain
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = OpenAIEmbeddings(
    base_url=os.environ["LLM_API_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    model=os.environ["LLM_MODEL"],
    tiktoken_enabled=False,
    check_embedding_ctx_length=False,
)


document=["spam issue","delivery issue","payment issue","account issue","technical issue"]
document_embeddings = embeddings.embed_documents(document)

user_query="I have a issue with my payment"
user_query_embedding = embeddings.embed_query(user_query)
similarities=cosine_similarity([user_query_embedding], document_embeddings)
print("Similarities:", similarities)
most_similar_document_index = similarities.argmax()
most_similar_document = document[most_similar_document_index]
print("Most similar document:", most_similar_document)
print("Similarity score:", similarities[0][most_similar_document_index])

