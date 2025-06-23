from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

api_key = os.getenv("GEN_AI_API")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash')

system_instruction = """
You are a helpful, friendly chatbot for Ngamba Island Chimpanzee Sanctuary.
Provide information about chimpanzees, tours, donations, and the island itself.
"""


class ChatbotAPIView(APIView):
    def post(self, request):
        user_massage = request.data.get("message", "")

        if not user_massage:
            return Response({"error": "No message provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            response =  model.generate_content([
                system_instruction,
                user_massage
            ])

            return response({"reply": response.text}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)