from django.shortcuts import render,redirect
import time
import json
# Create your views here.
import google.generativeai as genai
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from myapp.models import ChatBody, ChatTitle

import google.generativeai as genai

genai.configure(api_key="AIzaSyDGGMfoKBHGPASaai4QerSIEudCE2x7ZoM")



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
    "threshold": "LOW"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "LOW"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "LOW"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "LOW"
  },
]


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
from django.http import JsonResponse

def sentiment_add(request):
    offset = request.GET.get('offset')
    
    try:
        # Attempt to call sentimentlma and process the response
        mm = sentimentlma(offset)
        chatbot_response = str(mm)
        
        # Format specific words with <br/> and <strong> tags
        specific_words = ['Intent']
        for word in specific_words:
            chatbot_response = chatbot_response.replace(word, f'<br/>{word}')
        
        specific_wordsn = ['Intent', 'Sentiment']
        for wordn in specific_wordsn:
            chatbot_response = chatbot_response.replace(wordn, f'<strong>{wordn}</strong>')
        
        # Prepare data for the response
        data = {
            'chatbot_response': chatbot_response,
        }
        return JsonResponse({'data': data})

    except Exception as e:
        chatbot_response = 'HARASSMENT, HATE_SPEECH , SEXUALLY_EXPLICIT, DANGEROUS_CONTENT not analysis.'
        # Handle the exception and return an error response
        data = {
            'chatbot_response': chatbot_response,
        }
        return JsonResponse({'data': data})



def sentimentlma(question):
    my_list = [
        "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
        "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
        "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
        "Your task is to highlight and make alarm if there is anykind of suicidal intent"
        "According to the instructions above analyze the sentiment and intent of the following sentences"
        ]
    # print('question',question)
    # print('my_list',my_list)

    

    my_list.extend([question])

    # prompt_parts = my_list.append(question)

    # print('prompt_parts',my_list)
    hy = model.generate_content(my_list)

    print(hy.text)
    response =hy.text
    # response ='Hi i am not feeling well.'
    return response

# def sentimentlma(question):
#     my_list = [
#         "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
#         "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
#         "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
#         "Your task is to highlight and make alarm if there is anykind of suicidal intent"
#         "According to the instructions above analyze the sentiment and intent of the following sentences"
#         ]
    
#     # my_list = [
#     #     "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
#     #     "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
#     #     "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
#     #     "Your task is to highlight and make alarm if there is anykind of suicidal intent"
#     #     "According to the instructions above analyze the sentiment and intent of the following sentences"
#     #     ]
#     print('question',question)
#     print('my_list',my_list)

    

#     my_list.extend([question])

#     # prompt_parts = my_list.append(question)

#     # print('prompt_parts',my_list)
#     hy = model.generate_content(my_list)

#     # print(hy.text)
#     response =hy.text
#     # response ='Hi i am not feeling well.'
#     return response