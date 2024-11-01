from django.shortcuts import render,redirect
import time
from django.http import StreamingHttpResponse
import json
# Create your views here.
import google.generativeai as genai
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from myapp.models import ChatBody, ChatTitle

import google.generativeai as genai

#genai.configure(api_key="AIzaSyCa3TodvqZSSo3NlzLKzFfTuiEMrb73rbI")
genai.configure(api_key="AIzaSyDGGMfoKBHGPASaai4QerSIEudCE2x7ZoM")
#genai.configure(api_key="AIzaSyCRKIsZL-8UjLU_eLaHhNvSlVedIUDLb4g")
# print(genai.GenerativeModel.__init__.__code__.co_varnames)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 8192,
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
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config
  )

chat = model.start_chat(history=[])


def sentiment_add(request):
    offset = request.GET.get('offset')
    # mm = sentimentlma(offset)
    # user_input = input("You: ")
    my_list = [
        "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
        "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
        "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
        "Your task is to highlight and make alarm if there is anykind of suicidal intent"
        "According to the instructions above analyze the sentiment and intent of the following sentences"
        ]

    my_list.extend([offset])
    response = model.generate_content(my_list)

    # Print the bot response
    print("ssdsdsda:", response.text)

    chatbot_response = str(response)

    print('dcsdcs',chatbot_response)

    specific_words = ['Intent']
    for word in specific_words:
        chatbot_response = chatbot_response.replace(word, f'<br/>{word}')
    

    specific_wordsn = ['Intent', 'Sentiment']

    # Iterate through the specific words and apply bold formatting
    for wordn in specific_wordsn:
        chatbot_response = chatbot_response.replace(wordn, f'<strong>{wordn}</strong>')

    data = {
        'my': offset,
        'chatbot_response': chatbot_response,
    }

    return JsonResponse({'data': data})




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