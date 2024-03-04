import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") 
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = "2023-05-15"

response = openai.ChatCompletion.create(
    engine="gpt-35-turbo-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        # {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        # {"role": "user", "content": "Do other Azure AI services support this too?"}
        {"role": "user", "content": "What is the current temperature in Georgetown Ontario?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])