from django.shortcuts import render,redirect
import time
from django.http import StreamingHttpResponse
import json
# Create your views here.
import google.generativeai as genai
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from myapp.models import ChatBody, ChatTitle

# genai.configure(api_key="AIzaSyBRAqorLHlWe3K7SHr8vf7LGHqBveIDm-s")
#genai.configure(api_key="AIzaSyCRKIsZL-8UjLU_eLaHhNvSlVedIUDLb4g")
genai.configure(api_key="AIzaSyA6h1GsXORwihtpjQVqrACZ9R-ny5yiXPg")


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
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def welcome(request):
    return render(request, 'welcome.html')


def dynamic(request,id):

    chatBodys = ChatBody.objects.filter(chatTitle_id=id).order_by('id')
    chatBodyscount = ChatTitle.objects.all().count()
    # print('chatBodyscount',chatBodyscount)

    chatTitles = ChatTitle.objects.all()
    request.session.flush()
    data ={
        'chatTitles':chatTitles,
        'chatBodys':chatBodys,
        'id':id,
        'chatBodyscount':chatBodyscount,
    }
    return render(request, 'a_mainchat.html',data)


def dynamic_delete(request,id):
    # chatTitles = ChatTitle.objects.all()
    
    # chatBodys = ChatBody.objects.all()

    # ll= ChatTitle.objects.filter(id=id).count()
    # print('dsfgdsgf',ll)

    ChatTitle.objects.filter(id=id).delete()

    return redirect('chatui')




    # previous_url = request.META.get('HTTP_REFERER')
    
    # return HttpResponseRedirect(previous_url)
   




def chat_addcc(request):

    # rr = ' jjj yhkyh yukyuk "Sensor 435"'

    # mydata = CustomChatGPT(rr)

    # print(mydata)
    # print('mydata')
    prompt_parts = [
        "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
        "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
        "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
        "Your task is to highlight and make alarm if there is anykind of suicidal intent"
        "According to the instructions above analyze the sentiment and intent of the following sentences"
        "Hi i am not feeling well. right now i am depressed. Everything becoming blury to me i dont know what to do."
        ]
    response = model.generate_content(prompt_parts)
    
    def generate_json():
        # main = 'Discover the innovative world of Apple and shop everything iPhone,plus explore accessories, entertainment'
        main = response.text
        for data in main:
            # print('bbbbb')
            print(data)
            # data = data.replace("\\n", "\n")
            modified_data = data.replace('\n', '<br>')
            time.sleep(0.05)
            yield json.dumps(modified_data)

    response = StreamingHttpResponse(streaming_content=generate_json(), content_type='application/json')

    # Set the content disposition header
    response['Content-Disposition'] = 'attachment; filename="streamed_data.json"'

    return response







def pricing(request):
    return render(request, 'pricing.html')


def reset(request):
    return render(request, 'reset.html')


def blog(request):
    return render(request, 'blog.html')

def price(request):
    return render(request, 'price.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')


def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')


def faq(request):
    return render(request, 'faq.html')

def profile(request):
    return render(request, 'profile.html')



# def sentimentui(request):
#     request.session.flush()
    
#     return render(request, 'sentimentui.html')


def sentimentui(request):
    request.session.flush()
    
    return render(request, 'a_sentiment.html')




def sentimentlma(question):
    my_list = [
        "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
        "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
        "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
        "Your task is to highlight and make alarm if there is anykind of suicidal intent"
        "According to the instructions above analyze the sentiment and intent of the following sentences"
        ]
    
    # my_list = [
    #     "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
    #     "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
    #     "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
    #     "Your task is to highlight and make alarm if there is anykind of suicidal intent"
    #     "According to the instructions above analyze the sentiment and intent of the following sentences"
    #     ]
    # print('question',question)
    # print('my_list',my_list)

    

    my_list.extend([question])

    # prompt_parts = my_list.append(question)

    # print('prompt_parts',my_list)
    hy = model.generate_content(my_list)

    # print(hy.text)
    response =hy.text
    # response ='Hi i am not feeling well.'
    return response