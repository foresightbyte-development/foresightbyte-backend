# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from myapp.views import *
from myapp.chatviews import *
from myapp.apiviews import *

# Routing Implement
urlpatterns = [
       path('registration/', registration, name='registration'),
       path('login/', login, name='login'),
       path('faq/', faq, name='faq'),
       path('price/', price, name='price'),
       path('reset/', reset, name='reset'),
       path('about/', about, name='about'),
       path('contact/', contact, name='contact'),
       path('blog/', blog, name='blog'),
       path('service/', service, name='service'),
       path('pricing/', pricing, name='pricing'),
       path('', welcome, name='welcome'),
       path('dynamic/<int:id>', dynamic, name='dynamic'),
       path('dynamic_delete/<int:id>', dynamic_delete, name='dynamic_delete'),
       path('myapp/chatui/', chatui, name='chatui'),
       path('sentimentui/', sentimentui, name='sentimentui'),
       path('faq/', faq, name='faq'),
       path('profile/', profile, name='profile'),
       path('chat_add/', chat_add, name='chat_add'),
       path('sentiment_add/', sentiment_add, name='sentiment_add'),
       path('ask/', ask_question, name='ask_question'),


    
]


