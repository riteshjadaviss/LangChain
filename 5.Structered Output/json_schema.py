import langchain
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
load_dotenv()
chat = ChatAnthropic(
    api_key=os.environ["CLAUDE_API_KEY"],
    model="claude-haiku-5-5",
)

cuise_schema = {
    "title": "Cuisine",
    "description": "Information about a cuisine",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the cuisine",
        },
        "country": {
            "type": "string",
            "description": "Country of origin",
        },
        "specialty": {
            "type": "string",
            "description": "Specialty dish of the cuisine",
        },
        "ingredients": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of main ingredients",
        },
    },
    "required": ["name", "country", "specialty"],
    "additionalProperties": False,
}

structured_output = chat.with_structured_output(cuise_schema)
result=structured_output.invoke("Italian cuisine is famous for its simple, fresh ingredients and rich flavors. Popular dishes include pizza, pasta, risotto, and tiramisu. Olive oil, tomatoes, cheese, and herbs like basil are commonly used. Each region of Italy has its own unique cooking style and specialties")
print(result)
