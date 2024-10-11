# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from accounts.views import SignInView,register
from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [
    path('login/', SignInView, name='sign-in'),
    path('register/', register, name='register'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    
]


