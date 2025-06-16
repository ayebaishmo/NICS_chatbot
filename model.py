import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('GEN_AI_API')

genai.configure(api=api)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Tell me about Ngamba Island")

print(response.text)