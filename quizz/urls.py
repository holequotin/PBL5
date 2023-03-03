from django.urls import path,include
from .views import *\

app_name = 'quizz'
urlpatterns = [
    path('',landing_view,name = 'LandingPage'),
    path('login/',login_view,name='Login'),
    path('register/',register_view,name='Register')
]
