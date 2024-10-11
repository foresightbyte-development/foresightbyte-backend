# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from chotbotapi.views import answer_question


# Routing Implement
urlpatterns = [
        path('api/answer/', answer_question, name='answer_question'),
    
    
]


