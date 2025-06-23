from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('GEN_AI_API')

client = genai.Client(api=api)

response =client.models.generate_content(
    model="gemini-2.0-flash",
    contents = "Tell me about Ngamba Island"
)

print(response.text)