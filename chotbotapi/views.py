

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer


from django.shortcuts import render
import time
from django.http import StreamingHttpResponse
import json
# Create your views here.
import google.generativeai as genai
from django.http import JsonResponse

genai.configure(api_key="AIzaSyBRAqorLHlWe3K7SHr8vf7LGHqBveIDm-s")

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },

]


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)



@api_view(['GET', 'POST'])
def answer_question(request):

    
    
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            my_list = [
                "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
                "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
                "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
                "Your task is to highlight and make alarm if there is anykind of suicidal intent"
                "According to the instructions above analyze the sentiment and intent of the following sentences"
                ]
            question = serializer.validated_data.get('question')
            my_list.extend([question])
            hy = model.generate_content(my_list)
            response =hy.text
            print('ffff', response)
            # Here you can process the question and generate an answer
            answer = " {}".format(response)
            return Response({'answer': answer})
        else:
            return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        # Handle GET requests if needed
        return Response({'message': 'GET requests are not supported.'}, status=405)

