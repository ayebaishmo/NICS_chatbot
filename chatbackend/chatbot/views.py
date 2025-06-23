from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatbotRequestSerializer
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEN_AI_API')
print("Loaded API key:", api_key)  # Debug: is this None?

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

system_instruction = """
You are a helpful, friendly chatbot for Ngamba Island Chimpanzee Sanctuary.
Provide information about chimpanzees, tours, donations, and the island itself.
"""

class ChatbotAPIView(APIView):
    def post(self, request):
        print("Received data:", request.data)

        serializer = ChatbotRequestSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            print("User message:", user_message)

            try:
                response = model.generate_content([
                    system_instruction,
                    user_message
                ])
                print("AI response:", response.text)

                return Response({"reply": response.text}, status=status.HTTP_200_OK)

            except Exception as e:
                print("Error in AI model:", str(e))  # SHOW full AI errors
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            print("Serializer error:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
